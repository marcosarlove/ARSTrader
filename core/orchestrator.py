"""
ARSTrader - Global Orchestrator / Sovereign Engine (orchestrator.py)
=====================================================================
Dono único da instância de conexão ativa com a API da Exchange via CCXT.Pro e comandante supremo do fluxo macro.

Regras Operacionais:
1. Inicializa o loop de eventos assíncrono principal (`asyncio`) e comanda os subcomponentes (`config`, `loader`, `comms`).
2. Centraliza a execução de rede: nenhuma ordem toca o mercado sem passar por sua chamada final direta à API.
3. Garante a exclusividade do pipeline através de travas não-bloqueantes. Se o sinal for validado pela triagem temporal do `comms`
   e pelas travas financeiras do `wallet`, o Orquestrador despacha a ordem de mercado instantaneamente para a exchange.
"""


