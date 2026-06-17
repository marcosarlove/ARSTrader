"""
ARSTrader - Wallet & Risk Manager (wallet.py)
=============================================
Detém o monopólio absoluto sobre os dados privados da conta e cálculos de tamanho de posição.

Regras Operacionais:
1. Sincroniza e armazena localmente o saldo real e as posições abertas na Exchange.
2. Valida se o sinal entrante viola os limites globais e estritos: teto de perda diária (Daily Drawdown) e limite de ordens simultâneas.
3. Executa a inteligência de Sizing: calcula o lote exato a ser boletado e determina os alvos de Stop Loss e Take Profit se a estratégia não fornecê-los ou fornecer inválidos.
4. Se o sinal falhar em qualquer validação matemática deste módulo, a operação é abortada.
"""
