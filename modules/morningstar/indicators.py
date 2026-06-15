"""
ARSTrader - Mathematical & Technical Analysis (indicators.py)
=============================================================
Responsável estritamente pelo processamento numérico, cálculo de indicadores e reconhecimento de padrões gráficos.

Regras Operacionais:
1. Deve ser totalmente 'Stateless' (Sem estado). Recebe arrays ou deques de dados brutos e retorna apenas booleanos ou valores fixos.
2. Não possui consciência de conexões de rede, APIs ou filas de comunicação.
3. Não possui acesso ou conhecimento sobre o saldo da conta ou tamanho de ordens.
4. Projetado para isolamento total, facilitando testes unitários e simulações em sandbox.
"""

