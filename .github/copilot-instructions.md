# Copilot instructions for ARSTrader

Purpose
-------
Short, actionable guidance so Copilot sessions quickly find build/test/run steps and the repo's cross-file architecture.

Build / run / test / migrations
------------------------------
- Run the app (development):
  - Ensure .env contains DATABASE_URL (required). Then from repo root:
    python main.py --config global_config.yaml
  - main.py also supports: --create-user / --delete-user CLI helpers.

- Run a single module locally (for development):
  python modules/<module_name>/runner.py --name <module_name> --class <class_name> --core-host 127.0.0.1 --core-port 8888 --heartbeat-interval 5.0
  (Loader spawns modules with the same CLI args; use these to reproduce module behavior locally.)

- Tests:
  - Run full suite: pytest
  - Run a single test: pytest path/to/test_file.py::test_name (pyproject.toml sets pythonpath = ".")

- Database migrations (Alembic):
  - Apply migrations: alembic upgrade head
  - Create autogen migration: alembic revision --autogenerate -m "message"

- Linting: No project lint/formatter config detected (no flake8/black/ruff configs present).

High-level architecture (big picture)
-------------------------------------
- Core (core/): orchestrator, loader, server, DB, comms, web, telemetry/storage.
  - GlobalOrchestrator (boot entrypoint called by main.py) composes DB, SignalServer, ModuleLoader and web/dashboard.
  - SignalServer (core/server.py) is an async TCP IPC server that accepts JSON line messages from subprocess modules. It routes two main types: CONTROL and ORDER. ORDERs are validated by core.comms.TrafficController and handled by the Orchestrator; responses are sent back over the same socket using an asyncio.Future (promise) pattern.
  - ModuleLoader (core/loader.py) launches strategies as isolated subprocesses (uses sys.executable), collects stdout/stderr into core logs, tracks heartbeats and restarts crashed or frozen modules. Heartbeat timeout defaults to 15s and is configurable in the system config.
- Modules (modules/<strategy>/): each strategy is self-contained and follows a pattern: runner.py (entrypoint), strategy.py (strategy logic), indicators.py, state.py, config.yaml and tests. Modules communicate with the Core via the SignalServer JSON protocol.
- Persistence: Async SQLAlchemy + asyncpg; models in core.models; migrations in alembic/.
- Web: templates/ with core.web handling the dashboard UI; authentication backed by UserModel and DATABASE_URL.

Key repository conventions (repo-specific)
-----------------------------------------
- IPC JSON: messages are newline-delimited JSON. Two canonical types are CONTROL and ORDER. ORDER handlers expect/return a payload that may include a GUID to correlate responses.
- Heartbeats and recovery: ModuleLoader expects regular HEARTBEAT CONTROL packets. If no heartbeat for > heartbeat_timeout the module is considered crashed and will be killed and restarted.
- Process isolation: Modules run in their own OS process; rely on the same Python interpreter as the Core (loader uses sys.executable). Changes affecting subprocess args or runner behaviour require updating both modules/*/runner.py and core/loader.py.
- Configuration:
  - global_config.yaml at repo root controls enabled modules and system settings.
  - modules/<name>/config.yaml contains per-module settings including enabled, path, class_name, heartbeat_interval.
- Environment: main.py requires DATABASE_URL available in .env; it will abort if missing.
- Tests assume project root is on PYTHONPATH (see pyproject.toml pytest settings).

Notes for Copilot sessions
-------------------------
- When patching IPC behavior, search core/server.py and core/comms.py (TrafficController) and modules/*/runner.py for the JSON schema.
- When altering models or DB schema, remember to add an alembic revision and run migrations in CI and locally.
- Avoid leaking .env secrets; DATABASE_URL should not be committed.

Other AI assistant / agent configs
---------------------------------
No CLAUDE.md, .cursorrules, AGENTS.md, CONVENTIONS.md, .windsurfrules or similar assistant config files were found; nothing to incorporate.

If anything here should be expanded (e.g., specific test targets, additional run examples, or adding linting/CI instructions), say which area to expand.
