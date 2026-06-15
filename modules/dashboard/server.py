"""
ARSTrader - Web Dashboard & Telemetry Server (server.py)
========================================================
Roda um servidor Web minimalista de alta performance isolado em seu próprio processo filho.

Regras Operacionais:
1. Inicializa o servidor FastAPI alimentado pelo servidor ASGI Uvicorn.
2. Consome de forma contínua a fila IPC de telemetria enviada pelo componente 'storage.py' do Core.
3. Transmite atualizações de estado, logs, balanço de carteira e batimentos cardíacos para o frontend via WebSockets.
4. Possui privilégio estritamente de leitura: é incapaz de emitir ordens ou alterar configurações de risco do Core.
"""

