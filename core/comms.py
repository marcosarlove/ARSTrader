"""
ARSTrader - Inter-Process Communication & Traffic Controller (comms.py)
========================================================================
Gerencia a validação de tráfego, obsolescência de rede e padronização de schemas.

Regras Operacionais:
1. Intercepta os sinais brutos e realiza SEMPRE o parse JSON (se legível) para
   garantir que nenhuma tentativa de ordem seja perdida para a base de dados.
2. Aplica a Regra de Obsolescência Temporal contra o timestamp de origem.
3. Valida a presença de GUIDs e a consistência de alvos dinâmicos (ignore_fields).
4. Alimenta a telemetria do `storage.comms` em tempo real.
"""

import json
import logging
import time
from typing import Optional, Tuple
from core import storage
from core.logger import STATUS_LEVEL_NUM

logger = logging.getLogger("ARSTrader.Comms")


class TrafficController:
    """
    Controlador de Tráfego de Sinais. Atua como o primeiro crivo do Core,
    sanitizando dados e aplicando carimbos de status antes do roteamento.
    """

    def __init__(self, max_latency_seconds: float = 2.0):
        """
        :param max_latency_seconds: Janela máxima de tolerância temporal do sinal (IPC).
        """
        self.max_latency = max_latency_seconds

        # Campos estruturais mínimos para que o sinal seja considerado legível e auditável
        self._base_required_fields = {
            "guid",
            "strategy_name",
            "symbol",
            "exchange",
            "operation",
            "price",
            "timestamp",
        }

    def process_incoming_packet(
        self, raw_data: str
    ) -> Tuple[bool, Optional[dict], str]:
        """
        Realiza o parse obrigatório e valida o ciclo de vida inicial do sinal.

        :param raw_data: String/Bytes brutos recebidos diretamente do Socket TCP.
        :return: Tuple[Sucesso(bool), PayloadPadronizado(dict ou None), Veredito(str)]
        """
        agora = time.time()

        # 1. Tenta o parse bruto do JSON. Se falhar aqui, o dado é lixo ilegível (Único caso de não-persistência)
        try:
            raw_json = json.loads(raw_data)
        except (json.JSONDecodeError, TypeError) as e:
            logger.critical(
                f"[Comms] Falha crítica de decodificação de rede. Dados corrompidos: {e}"
            )
            return False, None, "CRITICAL_PARSE_ERROR"

        # 2. Validação de Schema Base (Campos fundamentais para salvar na DB)
        missing_fields = self._base_required_fields - raw_json.keys()
        if missing_fields:
            storage.comms.signals_dropped += 1
            # Retorna o dicionário cru para o Orchestrator persistir o erro com o máximo de dados que restou
            return False, raw_json, "INVALID_SCHEMA"

        # 3. Extração e cálculo de latência física do sinal
        try:
            sinal_timestamp = float(raw_json["timestamp"])
            latencia_interna = agora - sinal_timestamp
            latency_ms = latencia_interna * 1000.0
        except (ValueError, TypeError):
            storage.comms.signals_dropped += 1
            return False, raw_json, "INVALID_TIMESTAMP_FORMAT"

        # 4. Processamento do campo flexível 'ignore_fields' e alvos (SL / TP)
        ignore_fields = raw_json.get("ignore_fields", [])
        if not isinstance(ignore_fields, list):
            ignore_fields = []

        # Determina se Stop Loss e Take Profit devem ser extraídos ou anulados na unha
        sl_ignorado = "stop_loss" in ignore_fields
        tp_ignorado = "take_profit" in ignore_fields

        stop_loss = None if sl_ignorado else raw_json.get("stop_loss")
        take_profit = None if tp_ignorado else raw_json.get("take_profit")

        # 5. Validação Estrita para Estratégias Dinâmicas (Sem Alvos)
        # Se a estratégia ignora alvos e está a mandar um fechamento (SELL), ela DEVE enviar o target_guid
        target_guid = raw_json.get("target_guid")
        if (
            (sl_ignorado or tp_ignorado)
            and not target_guid
            and str(raw_json["operation"]).upper() == "SELL"
        ):
            storage.comms.signals_dropped += 1
            return False, raw_json, "MISSING_TARGET_GUID_FOR_DYNAMIC_CLOSE"

        # 6. Montagem do Payload Padronizado e Tipado para o Core
        # Repara que amount e wallet_balance_before nascem explicitamente como None (NULL no DB)
        standardized_payload = {
            "guid": str(raw_json["guid"]).strip(),
            "target_guid": str(target_guid).strip() if target_guid else None,
            "strategy_name": str(raw_json["strategy_name"]).strip().lower(),
            "symbol": str(raw_json["symbol"]).strip().upper(),
            "exchange": str(raw_json["exchange"]).strip().lower(),
            "operation": str(raw_json["operation"]).strip().upper(),  # BUY ou SELL
            "market": str(raw_json.get("market", "SPOT")).strip().upper(),
            "current_price": float(raw_json["price"]),
            "stop_loss": float(stop_loss) if stop_loss is not None else None,
            "take_profit": float(take_profit) if take_profit is not None else None,
            "ignore_fields": ignore_fields,
            "timestamp": sinal_timestamp,
            "latency_ms": latency_ms,
            "amount": None,
            "wallet_balance_before": None,
        }

        # 7. Regra de Obsolescência Temporal
        if latencia_interna > self.max_latency:
            storage.comms.signals_dropped += 1
            logger.error(
                f"[Comms] Sinal [{standardized_payload['guid']}] REJEITADO por Obsolescência Temporal: "
                f"{latencia_interna:.3f}s (Max tolerado: {self.max_latency}s)"
            )
            return False, standardized_payload, "SIGNAL_OBSOLETE"

        # 8. Sucesso: Sinal limpo e pronto para entrar na Fila do Wallet
        storage.comms.signals_processed += 1
        storage.comms.latency_ms = latency_ms

        logger.log(
            STATUS_LEVEL_NUM,
            f"[Comms] Sinal [{standardized_payload['guid']}] validado e padronizado. "
            f"Latência IPC: {latency_ms:.2f}ms"
        )

        return True, standardized_payload, "VALIDATED"

    def process_control_packet(
        self, raw_data: str
    ) -> Tuple[bool, Optional[dict], str]:
        """
        Realiza o parse e a validação de pacotes de sinal do tipo CONTROL.

        :param raw_data: String bruta recebida do Socket TCP.
        :return: Tuple[Sucesso(bool), PayloadPadronizado(dict ou None), Veredito(str)]
        """
        try:
            raw_json = json.loads(raw_data)
        except (json.JSONDecodeError, TypeError) as e:
            logger.critical(
                f"[Comms] Falha de decodificação do sinal de controle: {e}"
            )
            return False, None, "CRITICAL_PARSE_ERROR"

        # Campos obrigatórios para o sinal do tipo CONTROL
        required_fields = {"type", "action", "strategy_name"}
        missing_fields = required_fields - raw_json.keys()
        if missing_fields:
            return False, raw_json, "INVALID_CONTROL_SCHEMA"

        standardized_payload = {
            "type": str(raw_json["type"]).strip().upper(),
            "action": str(raw_json["action"]).strip().upper(),
            "strategy_name": str(raw_json["strategy_name"]).strip().lower(),
            "pid": int(raw_json.get("pid", 0)),
            "details": str(raw_json.get("details", "")).strip(),
        }

        # Validação das ações permitidas
        allowed_actions = {"BOOT", "READY", "HEARTBEAT", "SHUTDOWN", "ERROR"}
        if standardized_payload["action"] not in allowed_actions:
            return False, standardized_payload, "INVALID_CONTROL_ACTION"

        return True, standardized_payload, "VALIDATED"

