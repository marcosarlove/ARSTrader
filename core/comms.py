"""
ARSTrader - Inter-Process Communication & Traffic Controller (comms.py)
========================================================================
Gerencia o barramento de comunicação assíncrona (IPC) entre os Módulos e o Core.

Regras Operacionais:
1. Intercepta os sinais brutos emitidos pelos processos dos módulos através de filas multiprocessamento não-bloqueantes.
2. Aplica a Regra de Obsolescência Temporal: descarta o sinal instantaneamente se a latência interna (IPC) for superior ao limite configurado.
3. Aplica a Política 'Drop-on-Busy': verifica o estado do lock de execução do Orquestrador. Se o Core estiver ocupado executando
   uma ordem ou calculando risco, o sinal entrante é sumariamente descartado (sem filas de espera para sinais).
"""



