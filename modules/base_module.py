"""
ARSTrader - Abstract Base Module Contract (base_module.py)
===========================================================
Define a interface abstrata e as propriedades obrigatórias que toda estratégia ou módulo filho deve herdar e respeitar.

Regras Operacionais:
1. Padroniza o recebimento de recursos do Core (Filas IPC dedicadas e dicionário de configurações local).
2. Gerencia de forma automatizada e invariável o envio de batimentos cardíacos (Heartbeats) em background,
   desacoplando essa obrigação do desenvolvedor da estratégia.
3. Força a implementação do ponto de entrada assíncrono principal que governará o laço do processo isolado.
"""


