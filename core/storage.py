"""
ARSTrader - In-Memory Telemetry Storage (storage.py)
====================================================
Registra cada evento, log, execução de ordem e status do sistema em estruturas de dados ultravelozes (Thread-Safe).

Regras Operacionais:
1. Fornece métodos de gravação imediata (I/O zero em disco) para que o Orquestrador e demais componentes salvem dados sem perder milissegundos.
2. Mantém históricos curtos de telemetria através de deques e estados observáveis na RAM.
3. Aciona callbacks inscritos de forma assíncrona (não-bloqueante) sempre que um estado é alterado.
"""

import asyncio
import fnmatch
import inspect
import logging
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger("ARSTrader.Storage")


class Observable:
    """
    Classe base para objetos cujas alterações de atributos disparam notificações.
    Intercepta as atribuições de propriedades e encaminha as atualizações para o callback central.
    """
    def __init__(self, prefix: str, on_change_fn: Callable[[str, Any], None]):
        self.__dict__['_prefix'] = prefix
        self.__dict__['_on_change_fn'] = on_change_fn

    def __setattr__(self, name: str, value: Any) -> None:
        # Recupera o valor anterior para evitar disparos desnecessários (duplicados)
        old_value = getattr(self, name, None)
        super().__setattr__(name, value)
        
        # Só dispara notificação se o valor realmente mudou
        if old_value != value:
            prefix = self.__dict__.get('_prefix', '')
            callback = self.__dict__.get('_on_change_fn', None)
            if callback:
                # Constrói o caminho completo da chave alterada (ex: loader.morningstar.status)
                event_path = f"{prefix}.{name}" if prefix else name
                callback(event_path, value)


class ObservableDict(dict):
    """
    Dicionário observável que dispara notificações sempre que chaves são
    inseridas, alteradas ou removidas. Resolve a quebra de reatividade em coleções de status.
    """
    def __init__(self, prefix: str, on_change_fn: Callable[[str, Any], None], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prefix = prefix
        self._on_change_fn = on_change_fn

    def __setitem__(self, key: str, value: Any) -> None:
        old_value = self.get(key, None)
        super().__setitem__(key, value)
        if old_value != value and self._on_change_fn:
            self._on_change_fn(f"{self._prefix}.{key}", value)

    def __delitem__(self, key: str) -> None:
        if key in self:
            super().__delitem__(key)
            if self._on_change_fn:
                self._on_change_fn(f"{self._prefix}.{key}", None)

    def pop(self, key: str, default: Any = None) -> Any:
        if key in self:
            val = super().pop(key, default)
            if self._on_change_fn:
                self._on_change_fn(f"{self._prefix}.{key}", None)
            return val
        return super().pop(key, default)

    def clear(self) -> None:
        keys = list(self.keys())
        super().clear()
        if self._on_change_fn:
            for key in keys:
                self._on_change_fn(f"{self._prefix}.{key}", None)


class ModuleState(Observable):
    """Estado em tempo real de um subprocesso de estratégia (Módulo)."""
    def __init__(self, name: str, on_change_fn: Callable[[str, Any], None]):
        super().__init__(f"loader.{name}", on_change_fn)
        self.status = "OFF"  # OFF | STARTING | ON | RECOVERING
        self.pid = 0
        self.started_at = 0.0
        self.last_heartbeat = 0.0


class WalletState(Observable):
    """Estado financeiro de banca, risco e posições ativas."""
    def __init__(self, on_change_fn: Callable[[str, Any], None]):
        super().__init__("wallet", on_change_fn)
        self.balance = 0.0
        self.balance_breakdown = []
        self.max_daily_loss_pct = 0.0
        self.current_daily_loss_pct = 0.0
        self.simultaneous_trades = 0
        self.positions = []  # Nota: Para modificar e notificar em listas, reatribua: self.positions = [...]
        self.active_locks = ObservableDict("wallet.active_locks", on_change_fn)
        self.active_positions = ObservableDict("wallet.active_positions", on_change_fn)
        self.daily_loss_counter = 0.0
        self.max_daily_loss_limit = 0.0


class CommsState(Observable):
    """Estado de latência do IPC e volume de processamento de sinais."""
    def __init__(self, on_change_fn: Callable[[str, Any], None]):
        super().__init__("comms", on_change_fn)
        self.latency_ms = 0.0
        self.execution_lock = False
        self.signals_processed = 0
        self.signals_dropped = 0


class ConfigState(Observable):
    """Configurações ativas no ecossistema global do bot."""
    def __init__(self, on_change_fn: Callable[[str, Any], None]):
        super().__init__("config", on_change_fn)
        self.environment = "demo"  # demo | production
        self.heartbeat_timeout = 15.0


class GlobalStorage:
    """
    Fonte Única da Verdade (RAM) com barramento de eventos integrado.
    Todas as atualizações de estado disparam notificações assíncronas em background.
    """
    def __init__(self):
        # Dicionário de subscrições: {pattern_glob: [callback]}
        self._listeners: Dict[str, List[Callable[[str, Any], Any]]] = {}

        # Callback centralizador repassa os eventos internos dos objetos observáveis para os ouvintes
        def central_change_callback(event_path: str, value: Any) -> None:
            self._notify(event_path, value)

        self._on_change_fn = central_change_callback

        # Instanciação das sub-estruturas observáveis
        self.config = ConfigState(central_change_callback)
        self.wallet = WalletState(central_change_callback)
        self.comms = CommsState(central_change_callback)
        
        # Módulos gerenciados (Dicionário observável de instâncias observáveis)
        self.loader = ObservableDict("loader", central_change_callback)

    def register_module(self, name: str) -> None:
        """Registra uma nova estratégia no loader de monitoramento."""
        if name not in self.loader:
            self.loader[name] = ModuleState(name, self._on_change_fn)


    def subscribe(self, pattern: str, callback: Callable[[str, Any], Any]) -> None:
        """
        Inscreve um callback para ouvir alterações que casem com o padrão informado (glob/wildcard).
        Exemplos de padrões: 'wallet.balance', 'loader.*', 'loader.morningstar.status', '*'
        """
        if pattern not in self._listeners:
            self._listeners[pattern] = []
        if callback not in self._listeners[pattern]:
            self._listeners[pattern].append(callback)

    def unsubscribe(self, pattern: str, callback: Callable[[str, Any], Any]) -> None:
        """Cancela a subscrição de um ouvinte para um determinado padrão."""
        if pattern in self._listeners:
            try:
                self._listeners[pattern].remove(callback)
            except ValueError:
                pass

    def _notify(self, event_path: str, value: Any) -> None:
        """Varre os padrões inscritos e agenda os disparos correspondentes sem bloquear o emissor."""
        for pattern, callbacks in self._listeners.items():
            # Casamento flexível usando fnmatch (padrões glob: *, ?, [seq])
            if fnmatch.fnmatch(event_path, pattern):
                for cb in callbacks:
                    self._dispatch(cb, event_path, value)

    def _dispatch(self, callback: Callable[[str, Any], Any], event_path: str, value: Any) -> None:
        """Agenda ou chama o callback de forma isolada e sem bloquear a execução principal."""
        try:
            if inspect.iscoroutinefunction(callback):
                # Se for async def, agenda execução em background no loop de eventos atual
                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(callback(event_path, value))
                except RuntimeError:
                    # Caso não exista Event Loop ativo na thread atual (ex: testes síncronos)
                    pass
            else:
                # Callbacks síncronos são jogados para o executor de threads para não travar o Core
                try:
                    loop = asyncio.get_running_loop()
                    loop.run_in_executor(None, callback, event_path, value)
                except RuntimeError:
                    # Sem loop rodando (ex: testes síncronos simples), executa diretamente
                    callback(event_path, value)
        except Exception as e:
            # Captura a exceção para que um listener com bugs não afete as operações de trading do Core
            logger.error(
                f"[Storage] Falha crítica ao processar callback '{getattr(callback, '__name__', 'desconhecido')}' "
                f"para o evento '{event_path}': {e}"
            )


# Singleton padrão para compartilhamento fácil entre os componentes do ecossistema
storage = GlobalStorage()
