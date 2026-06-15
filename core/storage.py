"""
ARSTrader - In-Memory Telemetry Storage (storage.py)
====================================================
Registra cada evento, log, execução de ordem e status do sistema em estruturas de dados ultravelozes (Thread-Safe).

Regras Operacionais:
1. Fornece métodos de gravação imediata (I/O zero em disco) para que o Orquestrador e demais componentes salvem dados sem perder milissegundos.
2. Mantém históricos curtos de telemetria através de filas circulares limitadas (deques) na RAM.
3. Alimenta o canal de transmissão assíncrono que envia atualizações de estado em tempo real para o processo isolado do Dashboard Web.
"""

