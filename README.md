# ARSTrader — Sovereign Algorithmic Trading Engine

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

O **ARSTrader** é um motor de trading algorítmico proprietário de ultra-alta performance, orientado a eventos e totalmente assíncrono. Projetado para operar em mercados de criptoativos de alta volatilidade (com foco nativo em derivativos/futuros via CCXT Pro), o sistema adota uma arquitetura de microsserviços monolíticos baseada em **isolamento estrito de processos**, **comunicação de baixa latência** e **persistência desacoplada**.

A premissa do ARSTrader é simples, mas intransigente: **a execução de ordens e a gestão de risco devem ser tratadas em tempo real na velocidade da RAM, blindadas contra falhas de rede, travamentos de estratégias ou gargalos de banco de dados.**

---

## 🎯 Filosofia de Design e Engenharia

A arquitetura do ARSTrader foi moldada sob quatro pilares fundamentais de engenharia de software de alta confiabilidade:

### 1. Isolamento Físico de Falhas (Process Isolation)
As estratégias de trading (como as baseadas em padrões *Morning Star* ou *Evening Star*) não rodam dentro da mesma thread ou processo do Core do robô. Elas operam como subprocessos independentes do Linux (processos filhos gerenciados). 
* Se uma estratégia apresentar um vazamento de memória (*memory leak*), crashar, falhar a conexão com a internet ou travar em um loop infinito, **o núcleo do robô permanece 100% operacional**. 
* Um mecanismo ativo de **Watchdog** monitora os PIDs físicos e batimentos cardíacos (*heartbeats*) lógicos via TCP. Se um processo falha, ele é eliminado com `SIGKILL` e reiniciado automaticamente do zero, sem perder o estado operacional consolidado.

### 2. Execução Não-Bloqueante (Non-Blocking Engine)
Qualquer operação que envolva entrada/saída (I/O) lenta — como gravação de logs em disco, commits no banco de dados PostgreSQL ou renderização de páginas de telemetria — é sumariamente removida do Event Loop principal do motor de trading.
* **Database Assíncrono:** As escritas no banco utilizam o padrão *Worker Pattern* acoplado a uma fila em memória RAM (`asyncio.Queue`). O Core insere as operações na fila de forma instantânea e continua sua execução, enquanto um worker síncrono consome a fila em background.
* **Logs Não-Bloqueantes:** As mensagens de log são encapsuladas em buffers através do `logging.handlers.QueueHandler` e despachadas para arquivos rotativos (`RotatingFileHandler`) por uma thread dedicada em segundo plano.
* **Event Loop Limpo:** O fluxo principal é dedicado unicamente a escutar sinais da rede local, avaliar riscos em RAM e disparar requisições para a exchange.

### 3. Gestão de Risco na Velocidade da RAM (Zero-Latency Risk Checks)
Antes de enviar qualquer ordem para a exchange, o motor de risco do robô valida três travas fundamentais de segurança:
1. **Limite de Drawdown Diário:** Trava financeira que bloqueia novas operações se o prejuízo acumulado do dia (reconciliado com precisão) atingir o teto parametrizado.
2. **Limite de Ordens Simultâneas:** Controle que impede a sobre-exposição de capital.
3. **Locks de Ativos Temporários:** Estrutura rápida na memória RAM que impede que estratégias concorrentes enviem ordens duplicadas para o mesmo par no exato mesmo milissegundo.

Nenhum desses testes faz chamadas à rede ou consultas ao banco de dados durante o processamento do sinal. Toda a telemetria, saldos de carteira e posições abertas são cacheados e manipulados diretamente em estruturas de dados thread-safe na RAM.

### 4. Rastreabilidade Estrita para Auditoria
O robô é um sistema soberano de decisão. Absolutamente todo sinal recebido é categorizado, auditado e persistido no PostgreSQL:
* **`OperationModel`:** Registra a intenção, latência física do sinal, saldo prévio, preços de mercado, alvos e o veredito final do motor de risco (`EXECUTED`, `IGNORED`, `FAILED`).
* **`TradeResultModel`:** Registra o desfecho financeiro exato (PnL nominal, rendimento percentual e status de vitória/derrota) para auditoria e análise de performance matemática.

---

## 🛠️ Constituição Arquitetural

A estrutura do ARSTrader é constituída por duas grandes zonas desacopladas que se comunicam através de um protocolo local robusto:

```mermaid
graph TD
    subgraph Módulos Isolados [Processos Filhos - Estratégias]
        M1[MorningStar Strategy] -- "HEARTBEAT / ORDER (JSON)" --> IPC[Porta TCP Local]
        M2[EveningStar Strategy] -- "HEARTBEAT / ORDER (JSON)" --> IPC
    end

    subgraph Core [Processo Principal - Sovereign Engine]
        Server[SignalServer TCP] --> Traffic[Traffic Controller]
        Traffic --> Orchestrator[Global Orchestrator]
        Orchestrator --> Wallet[Wallet & Risk Manager]
        Wallet --> Exchange[CCXT Pro WS / REST]
        
        Orchestrator --> DB[Database Manager]
        DB --> RAM_Queue[asyncio.Queue]
        RAM_Queue --> Postgres[(PostgreSQL DB)]
        
        Storage[Global Storage RAM] <--> WebServer[Telemetry Web Server]
        WebServer -- "WebSockets" --> Dashboard[Dashboard UI]
    end
    
    classDef coreStyle fill:#1a1a2e,stroke:#162447,stroke-width:2px,color:#fff;
    classDef moduleStyle fill:#1b1b22,stroke:#3b3b4f,stroke-width:1px,color:#bbb;
    class Server,Orchestrator,Wallet,DB,Storage,WebServer coreStyle;
    class M1,M2 moduleStyle;
```

### O Protocolo IPC (Inter-Process Communication)
Para garantir máxima velocidade de processamento, as estratégias e o core utilizam um socket TCP bidirecional persistente (keep-alive) na interface de loopback (`127.0.0.1`).
* O tráfego de dados adota JSON delimitados por quebra de linha (`\n`).
* **Padrão de Promessas (Futures):** Ao receber uma ordem, o `SignalServer` cria um `asyncio.Future`. Ele interrompe a leitura daquela conexão específica e "aguarda" a conclusão da ordem sem travar a thread. Uma vez que o `WalletController` executa a ordem e a exchange confirma o preenchimento, a promessa é resolvida e o resultado de execução (incluindo preço de entrada médio e quantidade real) é enviado imediatamente de volta para a estratégia através do mesmo socket.

### Telemetria Reativa e Pub/Sub
O estado operacional do ARSTrader é unificado em um **Singleton Central de Telemetria** (`GlobalStorage`). 
* Implementado com propriedades observáveis, ele dispara atualizações para todos os listeners inscritos de forma assíncrona sempre que qualquer dado é alterado.
* O **TelemetryWebServer** utiliza esse ecossistema para escutar alterações globais (ex: variação de saldo ou alteração de status de processos) e empurrar as informações via **WebSockets** em tempo real para o dashboard web, consumindo zero I/O do banco de dados.

---

## 📈 Foco Absoluto em Performance

O ARSTrader foi otimizado para lidar com regimes de negociação de alta frequência e baixa latência de execução no nível de aplicação:

| Recurso | Técnica de Otimização | Objetivo de Performance |
| :--- | :--- | :--- |
| **Logging Central** | `QueueHandler` nativo + `ContextFilter` otimizado | Evita a gravação síncrona em disco no Event Loop e remove varreduras de pilhas de frames (`sys._getframe`), economizando microsegundos críticos por log. |
| **Reconciliação de Boot** | Boot assíncrono e paralelo com `asyncio.gather` | Quando o robô é reiniciado, ele sincroniza o estado de dezenas de ordens ativas e calcula drawdowns acumulados em paralelo via REST na exchange, reduzindo o tempo de boot ao mínimo absoluto. |
| **Persistência de Dados** | Bufferização de RAM + Worker assíncrono dedicada | Protege as operações de mercado contra latências repentinas de escrita no disco ou de conexão com o banco de dados. |
| **WebSocket Keep-Alive** | Monitoramento de saldo e ordens em tempo real via CCXT Pro | Evita polling excessivo de requisições HTTP REST na API da Exchange, mantendo o robô sempre atualizado com a menor latência de rede possível. |
| **Isolamento de CPU** | Subprocessos reais nativos | Permite o aproveitamento real de múltiplos cores de CPU da máquina host para o processamento de indicadores técnicos de múltiplas estratégias em paralelo. |

---

## 🧩 Componentes do Sistema (Detalhamento Teórico)

O ecossistema do ARSTrader é constituído por peças altamente especializadas que seguem princípios rígidos de responsabilidade única e acoplamento fraco. Abaixo, detalhamos o papel conceitual, a mecânica e a lógica por trás de cada componente.

### ⚙️ Camada de Configuração e Ambiente

#### 1. [global_config.yaml](file:///home/marcosarlove/projetos/ARSTrader/global_config.yaml)
É a declaração mestre do estado estático do robô. Sua função teórica é agir como a fonte de verdade para parametrização pré-boot.
* **Mapeamento de Ambiente e Limites de Processo:** Define se o robô opera em modo simulado (*demo*) ou real (*production*), além de fixar o tempo limite de ausência de sinais de vida tolerados para processos filhos.
* **Abstração de Conexões (Exchanges):** Modula as exchanges ativas, parâmetros de conexões privadas (como ajustes diferenciais de tempo para evitar erros de sincronismo com servidores remotos) e opções de mercados padrão (como a preferência automática por contratos de derivativos futuros perpétuos).
* **Parâmetros Centrais de Risco:** Estabelece os limites fundamentais de perdas operacionais diárias (drawdowns), a fração exata de saldo alocada por trade para position sizing e o teto máximo de trades concorrentes na exchange.
* **Registro de Módulos:** Define quais estratégias estão autorizadas a rodar, seus caminhos físicos no sistema e restrições de mercados ou fusos horários de ativação.
* **Suporte à Injeção Dinâmica:** Não armazena dados sensíveis brutos; em vez disso, utiliza marcadores de interpolação no padrão `${VAR_NAME:DEFAULT}` para puxar segredos diretamente do sistema operacional.

#### 2. [.env](file:///home/marcosarlove/projetos/ARSTrader/.env)
Responsável por delimitar a fronteira de segredos locais. Concentra credenciais de banco de dados (`DATABASE_URL`) e segredos de API da corretora (`BINANCE_API_KEY`, `BINANCE_SECRET`), garantindo que dados confidenciais nunca sejam commitados no controle de versão e permitindo a transição ágil de credenciais sem alteração do código ou da estrutura do YAML.

---

### 🧠 Camada de Núcleo (Core Engine)

#### 1. [core/config.py](file:///home/marcosarlove/projetos/ARSTrader/core/config.py) (`ConfigManager`)
Responsável pelo carregamento, conversão e disponibilização das diretivas de boot contidas no YAML.
* **Segurança e Isolamento de IO:** Executa a leitura do arquivo no disco de forma assíncrona, delegando a tarefa a um pool de threads isolado para não bloquear o Event Loop principal.
* **Motor de Interpolação:** Utiliza expressões regulares para varrer o arquivo cru e substituir as variáveis de ambiente em tempo real antes de enviar os dados ao parser YAML.
* **Tipagem Estrita e Imutabilidade:** Converte o dicionário gerado pelo YAML em instâncias de dados tipadas e congeladas (*frozen dataclasses*), evitando que bugs em outras partes do sistema consigam reescrever configurações críticas na RAM em tempo de execução.

#### 2. [core/database.py](file:///home/marcosarlove/projetos/ARSTrader/core/database.py) (`DatabaseManager`)
Gerencia o ciclo de conexões com o PostgreSQL de forma totalmente assíncrona baseada no padrão de projeto **Worker Pattern** com bufferização de RAM.
* **Proteção de Event Loop (Worker Assíncrono):** Para evitar que os tempos de latência e processamento do PostgreSQL bloqueiem a thread de trading, o banco de dados expõe uma fila assíncrona em memória RAM (`asyncio.Queue`). Ao requisitar uma persistência, o robô insere a instância do modelo na fila e continua seu fluxo. Um worker em background consome os registros dessa fila sequencialmente, abrindo sessões e consolidando as transações físicas.
* **Isolamento de Erros de Escrita:** Em caso de queda do banco, a fila absorve o choque temporário e o worker protege a aplicação contra quebras abruptas, tentando reconectar de forma automática.
* **Consultas de Apoio à Decisão:** Fornece rotinas otimizadas para calcular perdas diárias ocorridas e mapear operações ativas remanescentes para fins de conciliação.

#### 3. [core/models.py](file:///home/marcosarlove/projetos/ARSTrader/core/models.py) (Modelos ORM)
Define os schemas relacionais projetados para auditoria completa e análise de desempenho matemático:
* **`OperationModel`:** Registra o histórico de decisões do robô. Armazena o GUID exclusivo de rastreamento do sinal, o GUID alvo de encerramento (se aplicável), carimbos de tempo precisos de latência física do socket local, ativos, valores nocionais de capital, saldos de carteira antes da operação, limites dinâmicos de parada configurados e o status final de processamento acompanhado da justificativa literal de aceitação ou descarte.
* **`TradeResultModel`:** Acoplado a operações executadas com sucesso, rastreia o desfecho financeiro exclusivo. Registra o preço de fechamento final, o PnL nominal obtido (positivo ou negativo), o rendimento percentual exato da operação em relação ao capital empregado e a classificação de resultado (ganho, perda ou empate).
* **Indexação Avançada:** Possui índices compostos e únicos para campos de busca frequentes (GUIDs, símbolos e carimbos temporais) garantindo que consultas em tempo real para tomada de decisão sejam concluídas em milissegundos.

#### 4. [core/comms.py](file:///home/marcosarlove/projetos/ARSTrader/core/comms.py) (`TrafficController`)
Atua como o primeiro crivo de validação física dos dados que chegam da rede local antes que o robô tome qualquer decisão de investimento.
* **Sanitização de Schema:** Valida se o sinal entrante possui todos os atributos mínimos necessários para que seja uma operação auditável e compreensível para o banco de dados.
* **Controle de Obsolescência Temporal:** Calcula a latência física real de tráfego subtraindo o timestamp gerado no subprocesso da estratégia pelo relógio do core. Se o sinal demorou mais que a janela limite configurada para chegar pelo socket, ele é descartado instantaneamente, impedindo execuções de ordens defasadas por congestionamento de CPU.
* **Resolução de Metadados de Alvos:** Trata campos dinâmicos e flexíveis (como a supressão de alvos para fechamentos dinâmicos de ordens) e valida que sinais de encerramento obrigatoriamente apontem para o GUID da operação original correspondente.

#### 5. [core/server.py](file:///home/marcosarlove/projetos/ARSTrader/core/server.py) (`SignalServer`)
Implementa o servidor de sockets TCP local responsável por ouvir a comunicação inter-processo (IPC) das estratégias sob um modelo Keep-Alive persistente.
* **Tratamento Diferenciado de Mensagens:**
  * **Heartbeats:** Sinais leves de presença. São processados de forma síncrona diretamente na RAM para evitar o overhead de criação de tarefas e promessas, atualizando os registros de vida instantaneamente.
  * **Orders:** Sinais complexos de negociação. Disparam tarefas assíncronas concorrentes de modo a permitir que o canal leia outras mensagens enquanto a ordem está sendo processada.
* **Padrão de Promessas Assíncronas (Futures):** A conexão de rede é mantida em estado de suspensão segura (`await promise`) enquanto o Core decide o tamanho da ordem e a executa na corretora. Assim que a corretora responde, o status final é escrito de volta no socket da estratégia correspondente, garantindo feedback imediato para o loop analítico da estratégia.

#### 6. [core/loader.py](file:///home/marcosarlove/projetos/ARSTrader/core/loader.py) (`ModuleLoader`)
O gestor absoluto do ciclo de vida físico das estratégias.
* **Isolamento de Execução:** Levanta os runners das estratégias em subprocessos separados do sistema operacional.
* **Redirecionamento de Streams:** Captura de forma assíncrona e não-bloqueante a saída padrão (`stdout`) e de erro (`stderr`) dos processos filhos, injetando-os de volta no logger do Core de forma estruturada, facilitando a depuração unificada.
* **Watchdog de Segurança Ativo:** Varre os batimentos cardíacos lógicos em background. Se um processo morre a nível de sistema operacional, ou deixa de enviar dados a nível de aplicação pelo tempo limite, o loader limpa os resíduos da tabela de processos do OS e restabelece a estratégia levantando uma nova instância limpa.

#### 7. [core/logger.py](file:///home/marcosarlove/projetos/ARSTrader/core/logger.py) (`LogManager`)
Centralizador e otimizador de logs não-bloqueantes.
* **Padrão de Fila Assíncrona:** Move a gravação física dos arquivos de texto e renderizações de console para um QueueListener em thread separada.
* **Otimização de Contexto:** Substitui inspeções pesadas de pilha do interpretador Python (`sys._getframe`) por um mapeamento otimizado na memória que calcula caminhos relativos de arquivos a partir de um cache do diretório do projeto, reduzindo consideravelmente a latência de processamento interno do interpretador.

#### 8. [core/storage.py](file:///home/marcosarlove/projetos/ARSTrader/core/storage.py) (`GlobalStorage`)
A Fonte Única da Verdade sobre o estado corrente do ecossistema. Funciona como um cache de telemetria altamente otimizado e reativo na memória RAM.
* **Propriedades Observáveis:** Implementa invólucros especiais em torno de propriedades e dicionários. Qualquer escrita ou alteração de chaves (ex: atualização de saldo, mudança de PID ou alteração de status) aciona automaticamente barramentos de notificação sem que o emissor precise invocar disparadores manuais.
* **Barramento Pub/Sub de Baixo Acoplamento:** Módulos e servidores podem assinar tópicos de dados usando expressões coringas (ex: `wallet.*` ou `loader.morningstar.status`). Os disparos de callbacks associados são escalonados assincronamente ou movidos para executors de threads, assegurando que um ouvinte lento (como o servidor web de telemetria) nunca atrase a tomada de decisão principal do motor de trading.

#### 9. [core/wallet.py](file:///home/marcosarlove/projetos/ARSTrader/core/wallet.py) (`WalletController`)
O cérebro financeiro do robô. Detém o controle total das contas, cálculos de exposição e comunicação de negociação com a Exchange.
* **Locks de Ativos Temporários:** Gerencia um dicionário de locks em RAM. Quando uma operação é aberta para um determinado par, o símbolo é travado imediatamente. Isso previne que variações rápidas de mercado façam com que múltiplos sinais concorrentes operem de forma duplicada no mesmo ativo.
* **Validação de Risco Tripla:** Executa de forma síncrona testes contra limites de drawdown financeiro diário, limite de posições simultâneas e locks repetidos de ativos antes do envio de ordens.
* **Dimensionamento de Lote Dinâmico (Sizing):** Calcula o tamanho ótimo da posição comparando a porcentagem de risco parametrizada com o patrimônio livre em carteira. Ajusta as quantidades baseando-se estritamente nas regras mínimas de negociação e tamanhos de lotes reportados pela exchange por meio de seus dados cadastrais (CCXT local metadata).
* **Loops WebSocket de Sincronismo:** Roda loops persistentes utilizando as conexões WebSockets do CCXT Pro para receber atualizações instantâneas de ordens preenchidas e saldos livres. Isso elimina polling desnecessário de rede e garante reconciliações imediatas (como o fechamento automático de posições por ativação de Stop Loss na corretora).
* **De-duplicação de Mensagens:** Mantém controle de IDs processados para evitar que instabilidades na rede da corretora gerem duplicidade de tratamento de fechamentos de ordens.

#### 10. [core/web.py](file:///home/marcosarlove/projetos/ARSTrader/core/web.py) (`TelemetryWebServer`)
O provedor visual e de dados externos.
* **Desacoplamento Visual:** Não faz conexões ou buscas na base de dados para renderizar a telemetria. Em vez disso, se inscreve no barramento global de telemetria (`GlobalStorage`) na RAM.
* **Canal WebSocket de Baixo Overhead:** Envia o estado completo consolidado apenas no momento do aperto de mão (*handshake*) inicial. A partir daí, envia apenas pequenas mensagens de variação (delts) conforme o barramento de telemetria reativa dispara atualizações de propriedades, garantindo tráfego web irrisório e alta reatividade para o dashboard UI.

#### 11. [core/orchestrator.py](file:///home/marcosarlove/projetos/ARSTrader/core/orchestrator.py) (`GlobalOrchestrator`)
O comandante supremo do Sovereign Engine. Seu papel conceitual é unificar o ciclo de vida operacional global e coordenar a transição entre os estados do sistema.
* **Boot Reconciliation Loop:** Ao inicializar, antes de levantar as estratégias, o orquestrador realiza o processo de reconciliação de concorrência. Ele busca todas as operações salvas no banco de dados que constavam como abertas no momento do desligamento anterior e consulta seu status real diretamente na exchange em paralelo. Se alguma ordem foi fechada (ex: por Stop Loss/Take Profit da própria corretora) enquanto o robô estava offline, ele calcula os resultados definitivos, consolida no banco de dados e ajusta o saldo da carteira e o drawdown acumulado do dia atual na RAM.
* **Roteamento IPC e Gestão de Promessas:** Recebe os sinais brutos validados do `SignalServer`, abre as instâncias de persistência correspondentes, comanda a execução física das operações no `WalletController` e repassa as respostas finais para os respectivos sockets, resolvendo as promessas criadas.
* **Encerramento Ordenado de Dependências (Graceful Shutdown):** Coordena o desligamento do ecossistema de forma limpa, seguindo uma ordem estrita de interdependência:
  1. Interrompe o Loader de estratégias (para interromper a entrada de novos sinais).
  2. Desliga o servidor de telemetria web.
  3. Encerra o servidor de sinais TCP.
  4. Finaliza as tarefas WebSocket da wallet.
  5. Fecha as conexões HTTP/WS físicas da Exchange.
  6. Permite o escoamento de todos os commits pendentes na fila do DatabaseManager e finaliza a engine de banco de dados física.

---

### 🧩 Camada de Estratégias (Trading Modules)

As estratégias no ARSTrader operam de forma isolada do Core para garantir segurança matemática e estabilidade de execução.

#### 1. O Contrato de Comunicação IPC (JSON sobre TCP)
Como as estratégias são executadas em subprocessos dedicados, elas devem estabelecer uma conexão TCP keep-alive com o `SignalServer` do Core (usando o host e porta passados por argumento) e respeitar o protocolo de mensagens em formato JSON estruturado, sempre finalizando cada payload com uma quebra de linha `\n`.

##### A. Batimento Cardíaco (HEARTBEAT)
Para evitar que o Watchdog do Core elimine o processo da estratégia, esta deve enviar um sinal de presença de forma recorrente (recomendado a cada 2 a 5 segundos):
```json
{
  "type": "HEARTBEAT",
  "strategy_name": "morningstar",
  "pid": 12345
}
```

##### B. Envio de Ordem (ORDER - Abertura)
Quando a estratégia identifica uma entrada lógica, ela envia a ordem para o socket e aguarda a resposta (bloqueando apenas a leitura daquela promessa local):
```json
{
  "type": "ORDER",
  "guid": "c8b939fa-5b12-4217-a0e2-a0d01d1c1b1a",
  "strategy_name": "morningstar",
  "symbol": "BTC/USDT",
  "exchange": "binance",
  "operation": "BUY",
  "market": "FUTURES",
  "price": 67250.50,
  "stop_loss": 66240.00,
  "take_profit": 69260.00,
  "timestamp": 1781293214.234
}
```

##### C. Envio de Ordem (ORDER - Fechamento Dinâmico)
Caso a estratégia possua inteligência própria para fechar a operação antes que ela atinja os alvos estáticos (SL/TP) definidos na abertura, ela dispara a ordem oposta informando o GUID original para que o Core faça o encerramento do trade:
```json
{
  "type": "ORDER",
  "guid": "d9c040fb-6c23-5328-b1f3-b1e12e2d2c2b",
  "target_guid": "c8b939fa-5b12-4217-a0e2-a0d01d1c1b1a",
  "strategy_name": "morningstar",
  "symbol": "BTC/USDT",
  "exchange": "binance",
  "operation": "SELL",
  "market": "FUTURES",
  "price": 68100.00,
  "ignore_fields": ["stop_loss", "take_profit"],
  "timestamp": 1781293500.567
}
```

#### 2. Estrutura Recomendada para o Desenvolvedor
Toda estratégia cadastrada no sistema possui uma estrutura interna modular que oculta sua complexidade do Core por meio do padrão **Facade**:
* **`__init__.py`:** Expõe unicamente a classe ou a interface de boot necessária para o loader, agindo como fachada.
* **`state.py`:** Mantém o cache local de velas e ticks em memória RAM para as tomadas de decisão internas do processo.
* **`indicators.py`:** Concentra os algoritmos e cálculos analíticos da estratégia (cruzamentos, estatísticas, padrões gráficos).
* **`runner.py`:** Arquivo executável principal do subprocesso. Deve ler argumentos de linha de comando (`--name`, `--class`, `--core-host`, `--core-port`), conectar-se ao socket TCP, disparar a thread de heartbeats em background e conectar-se à exchange via WebSockets para colher preços públicos.

##### Exemplo de Estrutura Inicial para o `runner.py`:
```python
import argparse
import asyncio
import json
import os
import sys

async def send_heartbeats(writer, strategy_name):
    """Loop infinito de envio de batimentos cardíacos."""
    pid = os.getpid()
    while True:
        try:
            payload = {
                "type": "HEARTBEAT",
                "strategy_name": strategy_name,
                "pid": pid
            }
            writer.write(json.dumps(payload).encode("utf-8") + b"\n")
            await writer.drain()
        except Exception:
            break
        await asyncio.sleep(3)

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--class", required=True)
    parser.add_argument("--core-host", required=True)
    parser.add_argument("--core-port", type=int, required=True)
    args = parser.parse_args()

    # 1. Conexão Keep-Alive com o Core SignalServer
    reader, writer = await asyncio.open_connection(args.core_host, args.core_port)
    
    # 2. Inicia o loop de Heartbeats em background
    asyncio.create_task(send_heartbeats(writer, args.name))

    # 3. Exemplo de escuta/análise e disparo de ordens
    # (Adicione sua conexão WebSocket de dados públicos e lógica de indicadores aqui)
    try:
        while True:
            # Mantém a estratégia rodando analisando mercado...
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🚀 Guia de Inicialização (Primeira Execução)

Siga o passo a passo abaixo para clonar, configurar e executar o ARSTrader do zero no seu ambiente de desenvolvimento local.

### 📋 Pré-requisitos
Certifique-se de ter os seguintes componentes instalados e configurados na sua máquina:
* **Python 3.13 ou superior**
* **PostgreSQL** (com serviço ativo local ou remotamente)
* **Git**

### 🔧 1. Clonagem e Instalação de Dependências
Clone o repositório do projeto e entre no diretório:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd ARSTrader
```

Crie um ambiente virtual nativo e ative-o:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale todas as dependências requeridas do ecossistema:
```bash
pip install -r requirements.txt
```

### 🗄️ 2. Configuração de Banco de Dados e Ambiente (.env)
Crie o banco de dados no PostgreSQL chamado `arstrader`:
```sql
CREATE DATABASE arstrader;
```

Crie o arquivo de ambiente `.env` na raiz do diretório do projeto e defina a URL de conexão e suas credenciais de trading:
```env
# Banco de Dados PostgreSQL
DATABASE_URL=postgresql+asyncpg://seu_usuario:sua_senha@localhost:5432/arstrader

# Credenciais de Trading (Ex: Binance Futures)
BINANCE_API_KEY=sua_api_key_aqui
BINANCE_SECRET=seu_secret_aqui
```

### ⚡ 3. Execução das Migrações de Banco (Alembic)
O robô utiliza o **Alembic** para versionamento de schemas de banco de dados. Execute a migração para criar as tabelas `operations` e `trade_results` com os índices correspondentes:
```bash
alembic upgrade head
```

### ⚙️ 4. Ajuste das Configurações Globais
Abra o arquivo [global_config.yaml](file:///home/marcosarlove/projetos/ARSTrader/global_config.yaml) e parametrize os limites de risco ou ative os módulos de estratégia que deseja testar.
* Por exemplo, para ativar o módulo `morningstar`, certifique-se de que a flag `enabled` sob `modules -> morningstar` esteja definida como `true`.

### 🏁 5. Execução do Robô
Com o ambiente ativado, execute o ponto de entrada soberano:
```bash
python3 main.py
```

### 📊 6. Acesso ao Dashboard de Telemetria
Assim que o robô inicializar, o servidor web local subirá no host e porta configurados no YAML (padrão: `127.0.0.1:8080`).
* Abra seu navegador web e acesse: **[http://127.0.0.1:8080](http://127.0.0.1:8080)**.
* Você verá a telemetria, conexões ativas, logs dos subprocessos das estratégias e evolução do drawdown diário atualizados em tempo real via WebSockets.
