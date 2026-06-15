"""
ARSTrader - Strategy Process Engine (runner.py)
===============================================
Gerencia o ciclo de vida interno da estratégia e consome os dados públicos do mercado.

Regras Operacionais:
1. Executa o laço assíncrono infinito do processo filho isolado.
2. Abre e mantém a conexão única de WebSocket assíncrona (via CCXT.Pro) para coletar dados de mercado em tempo real.
3. Alimenta a memória local ('state.py') com os novos ticks/candles e invoca a validação matemática ('indicators.py').
4. Quando um padrão é confirmado, dispara o sinal IPC em modo Fire-and-Forget com timestamp de alta precisão para o Core.
"""

