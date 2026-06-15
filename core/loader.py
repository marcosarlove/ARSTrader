"""
ARSTrader - Process Loader & Watchdog (loader.py)
==================================================
O Gestor de Ciclo de Vida dos Súditos.
Responsável pelo isolamento físico, inicialização e monitoramento contínuo dos processos filhos (Módulos).

Regras Operacionais:
1. Lê as diretivas de 'config.py' e instancia dinamicamente cada estratégia habilitada em seu próprio 'multiprocessing.Process'.
2. Mantém o registro centralizado de PIDs (Process IDs) e filas de controle.
3. Executa o Watchdog ativo: se o batimento cardíaco (heartbeat) de um módulo falhar ou expirar o tempo limite,
   este componente elimina o processo zumbi e o reinicia do zero imediatamente.
"""



