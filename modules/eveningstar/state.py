"""
ARSTrader - Local Market Memory Manager (state.py)
==================================================
Organiza e retém as estruturas de dados temporárias necessárias para a tomada de decisão da estratégia.

Regras Operacionais:
1. Utiliza estruturas eficientes e seguras para concorrência (como 'collections.deque' com tamanho máximo fixo).
2. Limita rigidamente a retenção de dados históricos (ex: manter apenas os últimos 100 candles) para evitar vazamento de memória (Memory Leaks).
3. Fornece métodos de leitura ultrarrápidos para alimentar o arquivo 'indicators.py' a cada tick do mercado.
"""


