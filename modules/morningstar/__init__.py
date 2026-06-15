"""
ARSTrader - Strategy Facade Gateway (__init__.py)
==================================================
Responsável exclusivo por expor a classe principal de execução para o Core Loader.

Regras Operacionais:
1. Atua como um ponto de afunilamento de importação (Design Pattern Facade).
2. Oculta a complexidade de arquivos internos da estratégia (runner, indicators, state),
   permitindo que o Core a enxergue e instancie como se fosse um arquivo único.
"""


