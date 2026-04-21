# D: Drive - Python Code Master Index

> **Last updated:** 2026-04-20
> **Total Python files:** ~3,228 (user-written, excluding libraries/venvs)
>
> **See also:** [C: Drive Master](C:/Users/ohjos/PYTHON_CODE_MASTER.md) | [F: Drive Master](F:/PYTHON_CODE_MASTER.md)

---

## Table of Contents

1. [Brokers - Multi-Broker Trading Platform (~1,772 files)](#1-brokers---multi-broker-trading-platform)
2. [InterActiveBrokers Project (~734 files)](#2-interactivebrokers-project)
3. [Finance - Course Projects (~331 files)](#3-finance---course-projects)
4. [IronBeam - Futures Trading (~260 files)](#4-ironbeam---futures-trading)
5. [Spring 2026 - University Coursework (~48 files)](#5-spring-2026---university-coursework)
6. [1099 Form - Tax Automation (~28 files)](#6-1099-form---tax-automation)
7. [Finance Licenses - Exam Prep (~25 files)](#7-finance-licenses---exam-prep)
8. [WebScrapper (~11 files)](#8-webscrapper)
9. [Gmail Privacy Toolkit (~9 files)](#9-gmail-privacy-toolkit)
10. [CryptoMiner (~8 files)](#10-cryptominer)
11. [Smaller Projects](#11-smaller-projects)
12. [Cross-Drive Reference](#12-cross-drive-reference)

---

## 1. Brokers - Multi-Broker Trading Platform

**Path:** `D:\Code\Brokers\` | **Files:** ~1,772
> **Also on F:** `F:\Brokers\InteractiveBrokers\`

Production multi-broker trading platform with Docker orchestration, InfluxDB time-series data layer, 13 broker integrations, 400+ strategies, 31 maintenance agents, and Telegram bot control.

---

### 1.1 Root Files

| File | Description |
|------|-------------|
| `run.py` | Master orchestrator for Docker/Host mode switching, InfluxDB token bootstrap, signal handling |
| `conftest.py` | Repo-root pytest config sanitizing sys.path to prevent legacy package conflicts |
| `device_paths.py` | Device-aware path resolver for desktop/laptop/Raspberry Pi |
| `docker_utils.py` | Cross-platform Docker helpers for machine detection, compose files, engine checks |

---

### 1.2 agents/ (~43 files)

| File | Description |
|------|-------------|
| `__init__.py` | Central registry and entry-point for all 31 maintenance agents |
| `agent_accounting.py` | Validates accounting module with profit distribution formulas and fee structures |
| `agent_active_trader_gui.py` | Professional Active Trader GUI builder inspired by thinkorswim |
| `agent_alpha_features.py` | Framework for alpha signal features and statistical significance testing |
| `agent_architecture_doc.py` | Maintains ARCHITECTURE.md with ASCII diagrams and code examples |
| `agent_backtesting_validation.py` | Validates backtesting for data hygiene, look-ahead bias, slippage modeling |
| `agent_broker_integration.py` | Validates BrokerClient implementations via AST analysis |
| `agent_changelog.py` | Automatic git commit changelog logging |
| `agent_cli_review.py` | Verifies CLI commands, documentation, command parsing |
| `agent_code_quality.py` | Enforces modern Python: Pydantic, decorators, match-case, Polars, guard clauses |
| `agent_comment_review.py` | Reviews comments/docstrings for accuracy |
| `agent_concurrency_optimizer.py` | Finds sequential operations to parallelize |
| `agent_currency_collector.py` | Monitors WebSocket streaming for 8 currency futures pairs |
| `agent_data_integrity.py` | Validates data across InfluxDB, JSON, CSV backends |
| `agent_deep_learning.py` | Framework for PyTorch LSTM/GRU/Transformers and HMM |
| `agent_econometric_discovery.py` | Profiles data and discovers 230+ econometric tests |
| `agent_error_handling.py` | Enforces structured exceptions, logging, assertions |
| `agent_factor_mining.py` | Validates factor mining DSL integrity and data leak prevention |
| `agent_git_push_notes.py` | Generates detailed push summaries before code reaches GitHub |
| `agent_influxdb_manager.py` | Unified InfluxDB v2 management: buckets, Flux queries, dashboards, migrations |
| `agent_influxdb_manager_diagnostics.py` | Diagnostic queries for gap/anomaly detection |
| `agent_influxdb_manager_queries.py` | Market data and technical query methods |
| `agent_influxdb_manager_ref_cli.py` | CLI and HTTP API reference text blocks |
| `agent_influxdb_manager_ref_schema.py` | InfluxDB 3 Explorer and SQL reference |
| `agent_influxdb_manager_ref_time.py` | Time-based operations reference |
| `agent_influxdb_manager_references.py` | Master mixin coordinating all references |
| `agent_infrastructure.py` | Docker infrastructure with per-broker configs |
| `agent_json_consolidator.py` | Consolidates scattered JSON into per-security files |
| `agent_logger_standards.py` | Checks logging config, enforces professional text indicators |
| `agent_oop_analysis.py` | OOP pattern/anti-pattern detection |
| `agent_platform_compat.py` | Cross-platform compatibility (Windows 10 vs Raspberry Pi) |
| `agent_progress_bars.py` | Identifies loops needing tqdm progress bars |
| `agent_redis_optimizer.py` | Analyzes for Redis caching/pub-sub opportunities |
| `agent_slippage_optimizer.py` | Lagrangian optimization for trade execution slippage |
| `agent_slippage_review.py` | Per-strategy optimized execution parameters |
| `agent_strategy_validator.py` | Validates strategies are broker-agnostic via AST |
| `agent_test_coverage.py` | Reviews test coverage for functions, APIs, classes |
| `agent_timeframe_analysis.py` | Multi-timeframe analysis across 11 timeframes |
| `agent_trigger_scheduler.py` | Verifies Trigger Scheduler configurations |
| `agent_visualization.py` | Reviews visualization code and dashboards |
| `agent_watchdog_format.py` | Scans for formatting violations |
| `scan_config.py` | Shared scan config for agent directories |

---

### 1.3 broker_platform/ Root

| File | Description |
|------|-------------|
| `__init__.py` | Top-level package with version identifier |
| `env_check.py` | Runtime venv enforcement |
| `runtime_guard.py` | Runtime safety checks |

---

### 1.4 broker_platform/core/ (~37 files)

| File | Description |
|------|-------------|
| `__init__.py` | Core package init |
| `agent_scheduler.py` | Runs maintenance agents at intervals as background thread |
| `alpha_scan.py` | Multi-timeframe Alpha Scan: Hurst exponent, ADF, Variance Ratio |
| `crash_logger.py` | Persistent JSON crash reports to logs/crashes/ |
| `docker_backend.py` | Docker execution backend running services as containers |
| `docker_launcher.py` | Discovers Docker CLI/compose, builds subprocess commands |
| `docker_manager.py` | Docker Desktop lifecycle: launch, monitor, kill, restart |
| `env_check.py` | Runtime environment determination |
| `event_bus.py` | Thread-safe synchronous publish/subscribe messaging |
| `event_logger.py` | Persistent audit trail to InfluxDB and JSON logs |
| `exceptions.py` | Exception hierarchy: TradingPlatformError and descendants |
| `exit_analyzer.py` | Post-exit analysis producing structured recommendations |
| `healer_prompts.py` | Prompt templates for watchdog self-healing via Claude |
| `health_check.py` | Pre-flight health checks for broker services |
| `indicator.py` | Indicator Subscription Module for bar data |
| `isolation_audit.py` | Docker isolation audit logger |
| `legacy_command_builders.py` | Archived docker compose builders (NOT imported) |
| `legacy_host_services.py` | Archived host-subprocess definitions (NOT imported) |
| `mode_controller.py` | Docker/host-fallback mode switching |
| `service_watchdog.py` | ServiceWatchdog managing data-collection services with auto-restart |
| `system_detect.py` | Hardware detection: Raspberry Pi, Docker, desktop |
| `ticker_formatter.py` | Central ticker parsing/validation/formatting for any broker |
| `tws_manager.py` | TWS/IB Gateway lifecycle management |
| `watchdog.py` | BrokerWatchdog with exponential back-off reconnection |
| `watchdog_api.py` | REST API on :8099 for AI agent interaction |
| `watchdog_crash_handler.py` | CrashHandler with restart logic and TWS schedule |
| `watchdog_display.py` | Real-time status visualization |
| `watchdog_display_detail.py` | Detailed metrics display mixin |
| `watchdog_display_status.py` | Status table and per-service helpers |
| `watchdog_healer.py` | Self-healing via Claude diagnostics |
| `watchdog_health.py` | Health-check and failure handling mixin |
| `watchdog_interactive.py` | Interactive console loop and keypress handling |
| `watchdog_lifecycle.py` | Service start/stop/restart methods |
| `watchdog_monitor.py` | Health monitoring loop and pre-launch checks |
| `watchdog_persistence.py` | State persistence and signal handling |
| `watchdog_state.py` | State persistence and instance locking |

---

### 1.5 broker_platform/analytics/ (5 files)

| File | Description |
|------|-------------|
| `__init__.py` | Analytics package init |
| `execution_quality.py` | Per-broker execution quality scoring |
| `slippage.py` | Slippage analysis vs expected price |
| `tca.py` | Transaction Cost Analysis: implementation shortfall, market impact |
| `trade_analytics.py` | P&L attribution, per-trade metrics, aggregate performance |

### 1.6 broker_platform/broker_layer/ (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Broker layer package init |
| `base.py` | BrokerClient ABC defining abstract interface |
| `registry.py` | BrokerRegistry factory pattern for broker dispatch |
| `symbol_resolver.py` | SymbolResolver routing UniversalSymbol to broker format |

---

### 1.7 broker_platform/brokers/ - 13 Broker Implementations

#### brokers/ Root (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Brokers package init |
| `_utils.py` | Shared utility functions |
| `currency_futures_charts.py` | Currency futures and tick chart utilities |
| `visualization_utils.py` | Shared visualization utilities |

#### brokers/coinbase/ (6 files)

| File | Description |
|------|-------------|
| `__init__.py` | Coinbase package init |
| `auth.py` | Coinbase authentication handler |
| `client.py` | Coinbase BrokerClient implementation |
| `constants.py` | Coinbase-specific constants and endpoints |
| `streaming.py` | Coinbase real-time data streaming |
| `symbol_adapter.py` | Coinbase symbol format adapter |

#### brokers/etrade/ (6 files)

| File | Description |
|------|-------------|
| `__init__.py` | E*TRADE package init |
| `auth.py` | OAuth 1.0a authentication for E*TRADE |
| `client.py` | E*TRADE BrokerClient implementation |
| `constants.py` | E*TRADE-specific constants and endpoints |
| `streaming.py` | E*TRADE data streaming via polling |
| `symbol_adapter.py` | E*TRADE symbol format adapter |

#### brokers/fidelity/ (2 files)

| File | Description |
|------|-------------|
| `client.py` | Fidelity BrokerClient stub implementation |
| `symbol_adapter.py` | Fidelity symbol format adapter |

#### brokers/fix/ (2 files)

| File | Description |
|------|-------------|
| `__init__.py` | FIX protocol package init |
| `client.py` | FIX protocol BrokerClient implementation |

#### brokers/ibkr/ (14 files)

| File | Description |
|------|-------------|
| `__init__.py` | IBKR package init |
| `account.py` | IBKR account data retrieval |
| `bond_scanner.py` | IBKR bond market scanner |
| `client.py` | IBKR BrokerClient with threading.Event coordination |
| `client_id_manager.py` | Client ID allocation to avoid TWS conflicts |
| `constants.py` | IBKR-specific constants, contract IDs, exchange mappings |
| `contracts.py` | IBKR contract object builders |
| `orders.py` | IBKR order construction and submission |
| `streaming.py` | IBKR real-time market data streaming |
| `symbol_adapter.py` | IBKR symbol format adapter |
| `trading_app.py` | Main EWrapper/EClient application class |
| `trading_app_callbacks.py` | TWS API callback handler methods |
| `trading_app_connection.py` | TWS connection management mixin |
| `trading_app_helpers.py` | Trading app utility methods |

#### brokers/ironbeam/ (42 files)

| File | Description |
|------|-------------|
| `__init__.py` | IronBeam package init |
| `account.py` | IronBeam account data access |
| `account_bulk.py` | Bulk account operations |
| `account_fills.py` | Account fill history retrieval |
| `account_positions.py` | Account position management |
| `account_queries.py` | Account query helpers |
| `auth.py` | IronBeam authentication handler |
| `auth_logout.py` | Authentication logout/cleanup |
| `auth_token.py` | Token management and refresh |
| `client.py` | IronBeam BrokerClient implementation |
| `constants.py` | IronBeam-specific constants and endpoints |
| `contract_specs.py` | Futures contract specifications |
| `historical.py` | Historical data retrieval coordinator |
| `historical_fetch.py` | Historical data fetch logic |
| `historical_fetch_bars.py` | Bar data fetching implementation |
| `historical_fetch_realtime.py` | Real-time bar fetch integration |
| `historical_parser.py` | Historical data response parser |
| `historical_request.py` | Historical data request builder |
| `margin_requirements.py` | Margin requirement calculations |
| `margin_utilization.py` | Margin utilization tracking |
| `market_data.py` | Market data coordinator |
| `market_data_depth.py` | Level 2 / market depth data |
| `market_data_quotes.py` | Quote data retrieval |
| `market_data_trades.py` | Trade data retrieval |
| `market_data_utils.py` | Market data utility helpers |
| `order_submission.py` | Order submission logic |
| `order_tracking.py` | Order tracking coordinator |
| `order_tracking_cancel.py` | Order cancellation logic |
| `order_tracking_query.py` | Order status query methods |
| `order_validation.py` | Pre-submission order validation |
| `orders.py` | Order construction and type definitions |
| `symbol_adapter.py` | IronBeam symbol format adapter |
| `websocket.py` | WebSocket connection coordinator |
| `ws_connection.py` | WebSocket connection management |
| `ws_data_access.py` | WebSocket data access layer |
| `ws_events.py` | WebSocket event definitions |
| `ws_handlers.py` | WebSocket message handler coordinator |
| `ws_handlers_account.py` | WebSocket account update handlers |
| `ws_handlers_bars.py` | WebSocket bar data handlers |
| `ws_handlers_market.py` | WebSocket market data handlers |
| `ws_handlers_system.py` | WebSocket system message handlers |
| `ws_subscriptions.py` | WebSocket subscription management |

#### brokers/moomoo/ (7 files)

| File | Description |
|------|-------------|
| `__init__.py` | Moomoo package init |
| `account.py` | Moomoo account data retrieval |
| `auth.py` | Moomoo authentication handler |
| `client.py` | Moomoo BrokerClient implementation |
| `constants.py` | Moomoo-specific constants |
| `streaming.py` | Moomoo real-time data streaming |
| `symbol_adapter.py` | Moomoo symbol format adapter |

#### brokers/ninjatrader/ (6 files)

| File | Description |
|------|-------------|
| `__init__.py` | NinjaTrader package init |
| `auth.py` | NinjaTrader ATI DLL authentication |
| `client.py` | NinjaTrader BrokerClient implementation |
| `constants.py` | NinjaTrader-specific constants |
| `streaming.py` | NinjaTrader data streaming via polling |
| `symbol_adapter.py` | NinjaTrader symbol format adapter |

#### brokers/schwab/ (8 files)

| File | Description |
|------|-------------|
| `__init__.py` | Schwab package init |
| `account.py` | Schwab account data retrieval |
| `auth.py` | Schwab authentication handler |
| `client.py` | Schwab BrokerClient implementation |
| `constants.py` | Schwab-specific constants and endpoints |
| `streaming.py` | Schwab WebSocket real-time streaming |
| `symbol_adapter.py` | Schwab symbol format adapter |
| `watchlists.py` | Schwab watchlist management |

#### brokers/tastytrade/ (7 files)

| File | Description |
|------|-------------|
| `__init__.py` | TastyTrade package init |
| `account.py` | TastyTrade account data retrieval |
| `auth.py` | TastyTrade authentication handler |
| `client.py` | TastyTrade BrokerClient implementation |
| `constants.py` | TastyTrade-specific constants |
| `streaming.py` | TastyTrade DXLink real-time streaming |
| `symbol_adapter.py` | TastyTrade symbol format adapter |

#### brokers/tradestation/ (6 files)

| File | Description |
|------|-------------|
| `__init__.py` | TradeStation package init |
| `auth.py` | TradeStation OAuth 2.0 authentication |
| `client.py` | TradeStation BrokerClient implementation |
| `constants.py` | TradeStation-specific constants |
| `streaming.py` | TradeStation SSE (Server-Sent Events) streaming |
| `symbol_adapter.py` | TradeStation symbol format adapter |

#### brokers/vanguard/ (2 files)

| File | Description |
|------|-------------|
| `client.py` | Vanguard BrokerClient stub implementation |
| `symbol_adapter.py` | Vanguard symbol format adapter |

#### brokers/webull/ (6 files)

| File | Description |
|------|-------------|
| `__init__.py` | Webull package init |
| `auth.py` | Webull authentication handler |
| `client.py` | Webull BrokerClient implementation |
| `constants.py` | Webull-specific constants |
| `streaming.py` | Webull MQTT real-time streaming |
| `symbol_adapter.py` | Webull symbol format adapter |

---

### 1.8 broker_platform/config/ (3 files)

| File | Description |
|------|-------------|
| `__init__.py` | Config package init |
| `constants.py` | Platform-wide constants and defaults |
| `settings.py` | PlatformSettings Pydantic model for configuration |

### 1.9 broker_platform/connectivity/ (3 files)

| File | Description |
|------|-------------|
| `__init__.py` | Connectivity package init |
| `failover.py` | Automatic broker failover on connection loss |
| `health_monitor.py` | Per-broker connection state machine |

### 1.10 broker_platform/dashboard/ (2 files)

| File | Description |
|------|-------------|
| `__init__.py` | Dashboard package init |
| `app.py` | Flask web dashboard for platform monitoring |

### 1.11 broker_platform/data/ (~35 files)

| File | Description |
|------|-------------|
| `__init__.py` | Data package init |
| `_tag_helpers.py` | InfluxDB tag construction helpers |
| `archive_reader.py` | Historical archive file reader |
| `coverage_analyzer.py` | Data coverage gap analysis |
| `data_pipeline.py` | Main data pipeline orchestrator |
| `data_pipeline_readers.py` | Pipeline reader implementations |
| `data_pipeline_writers.py` | Pipeline writer implementations |
| `influx_account.py` | InfluxDB account data operations |
| `influx_client.py` | InfluxDB client wrapper |
| `influx_constants.py` | InfluxDB bucket names, retention policies |
| `influx_ops.py` | InfluxDB CRUD operations |
| `influx_queries.py` | InfluxDB Flux query builders |
| `influx_utils.py` | InfluxDB utility coordinator |
| `influx_utils_duplicates.py` | InfluxDB duplicate detection and removal |
| `influx_utils_export.py` | InfluxDB data export utilities |
| `influx_utils_queries.py` | InfluxDB query utility methods |
| `influx_utils_tags.py` | InfluxDB tag management utilities |
| `influx_writers.py` | InfluxDB writer coordinator |
| `influx_writers_bars.py` | InfluxDB OHLCV bar writer |
| `influx_writers_batch.py` | InfluxDB batch write operations |
| `influx_writers_quote_trade.py` | InfluxDB quote and trade writer |
| `influx_writers_single.py` | InfluxDB single-point writer |
| `json_data_saver.py` | JSON data persistence coordinator |
| `json_data_saver_query.py` | JSON data query methods |
| `json_data_saver_save.py` | JSON data save methods |
| `l1_quote.py` | Level 1 quote data model |
| `master_data_consolidation.py` | Master data file consolidation |
| `master_data_ingestion.py` | Master data ingestion pipeline |
| `master_data_manager.py` | Master data management coordinator |
| `master_data_persistence.py` | Master data persistence layer |
| `master_data_timeseries.py` | Master data time-series operations |
| `master_data_validation.py` | Master data validation rules |
| `redis_cache.py` | Redis caching layer for hot data |
| `tick_resampler.py` | Tick-to-bar resampling engine |
| `write_tracker.py` | Write operation tracking and deduplication |

### 1.12 broker_platform/fix/ (3 files)

| File | Description |
|------|-------------|
| `__init__.py` | FIX protocol package init |
| `messages.py` | FIX message construction and parsing |
| `session.py` | FIX session management |

### 1.13 broker_platform/market_data/ (5 files)

| File | Description |
|------|-------------|
| `__init__.py` | Market data package init |
| `arbitration.py` | NBBO (National Best Bid/Offer) arbitration |
| `feed.py` | Market data feed abstraction |
| `order_book.py` | Order book maintenance and L2 data |
| `quality.py` | Market data quality scoring |

### 1.14 broker_platform/models/ (9 files)

| File | Description |
|------|-------------|
| `__init__.py` | Models package init |
| `account.py` | Account Pydantic model |
| `bar.py` | OHLCV Bar Pydantic model |
| `capabilities.py` | Broker capabilities model |
| `health.py` | Health status model |
| `order.py` | Order Pydantic model |
| `quote.py` | Quote Pydantic model |
| `scanner.py` | Scanner result model |
| `symbol.py` | UniversalSymbol Pydantic model |

### 1.15 broker_platform/monitoring/ (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Monitoring package init |
| `anomaly.py` | Anomaly detection in metrics and data feeds |
| `latency.py` | Latency measurement and alerting |
| `metrics.py` | Platform metrics collection |

### 1.16 broker_platform/orders/ (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Orders package init |
| `manager.py` | Order lifecycle management |
| `router.py` | Smart Order Router for multi-broker execution |
| `state_machine.py` | Order state machine (pending/filled/cancelled/etc.) |

### 1.17 broker_platform/risk/ (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Risk package init |
| `kill_switch.py` | Emergency kill switch for all trading activity |
| `models.py` | Risk parameter models |
| `pre_trade.py` | Pre-trade risk checks and limits |

### 1.18 broker_platform/services/ (~13 files)

| File | Description |
|------|-------------|
| `__init__.py` | Services package init |
| `base_service.py` | Base service class with lifecycle methods |
| `notification_service.py` | Multi-channel notification dispatch |
| `pnl_service.py` | Real-time P&L calculation service |
| `storage_sync_notifier.py` | Storage synchronization notifications |
| `telegram_bot.py` | Telegram bot main entry point |
| `telegram_commands.py` | Telegram command router |
| `telegram_commands_account.py` | Telegram account commands (/balance, /positions) |
| `telegram_commands_claude.py` | Telegram Claude AI interaction commands |
| `telegram_commands_jobs.py` | Telegram job management commands |
| `telegram_commands_market.py` | Telegram market data commands |
| `telegram_helpers.py` | Telegram formatting and utility helpers |
| `telegram_jobs.py` | Telegram scheduled job definitions |

### 1.19 broker_platform/utils/ (10 files)

| File | Description |
|------|-------------|
| `__init__.py` | Utils package init |
| `colors.py` | Terminal color formatting utilities |
| `concurrency.py` | Thread pool and async execution helpers |
| `decorators.py` | Retry, timing, caching decorators |
| `heartbeat.py` | Service heartbeat monitoring |
| `logger.py` | Centralized logging configuration |
| `ml_integration.py` | Machine learning model integration helpers |
| `report_io.py` | Report file I/O and formatting |
| `time_utils.py` | Timezone conversion and market hours utilities |
| `validators.py` | Input validation helpers |

---

### 1.20 strategies/ Root (11 files)

| File | Description |
|------|-------------|
| `__init__.py` | Strategies package init |
| `backtest_runner.py` | Backtesting execution engine |
| `base_strategy.py` | Abstract base strategy class |
| `registry.py` | Strategy registry for discovery and dispatch |
| `stdev_calculator.py` | Standard deviation calculator for strategy signals |
| `strategy_logger.py` | Strategy-specific logging with trade annotations |
| `strategy_runner.py` | Live strategy execution runner |
| `strategy_tester.py` | Strategy testing framework coordinator |
| `strategy_tester_execution_mixin.py` | Strategy tester execution logic mixin |
| `strategy_tester_metrics_mixin.py` | Strategy tester metrics calculation mixin |
| `strategy_tester_runner_mixin.py` | Strategy tester runner logic mixin |

### 1.21 strategies/analysis/ (57 files)

| File | Description |
|------|-------------|
| `__init__.py` | Analysis package init |
| `anderson_darling_test.py` | Anderson-Darling goodness-of-fit test implementation |
| `backtest_viz_analysis_mixin.py` | Backtest visualization analysis mixin |
| `backtest_viz_charts_mixin.py` | Backtest visualization chart generation mixin |
| `custom_distributions.py` | Custom probability distribution definitions |
| `dist_fitter_continuous_mixin.py` | Distribution fitter continuous distribution mixin |
| `dist_fitter_misc_mixin.py` | Distribution fitter miscellaneous distribution mixin |
| `distribution_fit_analyzer.py` | Distribution fitting analysis coordinator |
| `distribution_mega_fit.py` | Mega distribution fitter (all scipy distributions) |
| `distribution_mega_fit_analysis_mixin.py` | Mega fit analysis mixin |
| `distribution_mega_fit_core_mixin.py` | Mega fit core fitting mixin |
| `distribution_mega_fit_display_mixin.py` | Mega fit display/output mixin |
| `distribution_mega_fit_fitting_mixin.py` | Mega fit parameter fitting mixin |
| `distribution_mega_fit_persistence_mixin.py` | Mega fit results persistence mixin |
| `distribution_mega_fit_plotting_mixin.py` | Mega fit chart plotting mixin |
| `distribution_mega_fit_reporting_mixin.py` | Mega fit report generation mixin |
| `ibkr_backtesting_framework.py` | IBKR-specific backtesting framework |
| `ibkr_dist_fit_fitting.py` | IBKR distribution fit fitting logic |
| `ibkr_dist_fit_report.py` | IBKR distribution fit report generation |
| `ibkr_dist_fit_viz.py` | IBKR distribution fit visualization |
| `ibkr_distribution_fit_analyzer.py` | IBKR distribution fit analysis coordinator |
| `ibkr_run_backtest.py` | IBKR backtest runner script |
| `ibkr_strategy_logger.py` | IBKR strategy logging |
| `ibkr_strategy_logger_output_mixin.py` | IBKR strategy logger output mixin |
| `ibkr_strategy_logger_trade_mixin.py` | IBKR strategy logger trade tracking mixin |
| `ibkr_strategy_tester.py` | IBKR strategy testing framework |
| `ibkr_strategy_tester_execution_mixin.py` | IBKR strategy tester execution mixin |
| `ibkr_strategy_tester_metrics_mixin.py` | IBKR strategy tester metrics mixin |
| `influx_data_loader_fetch_mixin.py` | InfluxDB data loader fetch mixin |
| `influx_data_loader_merge_mixin.py` | InfluxDB data loader merge mixin |
| `influx_data_loader_query_mixin.py` | InfluxDB data loader query mixin |
| `influx_dist_analysis_mixin.py` | InfluxDB distribution analysis mixin |
| `influx_dist_report_mixin.py` | InfluxDB distribution report mixin |
| `influxdb_distribution_analysis.py` | InfluxDB distribution analysis coordinator |
| `influxdb_writer.py` | InfluxDB writer for strategy results |
| `ironbeam_backtest_runner.py` | IronBeam-specific backtest runner |
| `ks_runner_analysis_mixin.py` | KS test runner analysis mixin |
| `ks_runner_report_mixin.py` | KS test runner report mixin |
| `ks_test.py` | Kolmogorov-Smirnov test implementation |
| `ks_test_enhanced.py` | Enhanced KS test with additional statistics |
| `ks_test_enhanced_analysis_mixin.py` | Enhanced KS analysis mixin |
| `ks_test_enhanced_fitting_mixin.py` | Enhanced KS fitting mixin |
| `ks_test_enhanced_reporting_mixin.py` | Enhanced KS reporting mixin |
| `ks_test_enhanced_visualization_mixin.py` | Enhanced KS visualization mixin |
| `notebook_utils.py` | Jupyter notebook utility functions |
| `ohlc_stdev_calc_mixin.py` | OHLC standard deviation calculation mixin |
| `ohlc_stdev_output_mixin.py` | OHLC standard deviation output mixin |
| `ohlc_stdev_viz_mixin.py` | OHLC standard deviation visualization mixin |
| `run_combined_analysis.py` | Combined analysis runner script |
| `signal_validator.py` | Trading signal validation and backtesting |
| `smirnov_distribution_test.py` | Smirnov distribution test implementation |
| `smirnov_distribution_test_fitting_mixin.py` | Smirnov test fitting mixin |
| `smirnov_distribution_test_reporting_mixin.py` | Smirnov test reporting mixin |
| `statistical_analyzer.py` | Statistical analysis coordinator |
| `std_dev_analyzer.py` | Standard deviation analysis across timeframes |
| `trigger_scheduler.py` | Strategy trigger scheduling |
| `visualization_dashboard.py` | Analysis visualization dashboard |

### 1.22 strategies/builtin/ (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Built-in strategies package init |
| `ma_crossover.py` | Moving average crossover strategy |
| `mean_reversion.py` | Mean reversion strategy |
| `momentum.py` | Momentum-based strategy |

### 1.23 strategies/converter/ (6 files)

| File | Description |
|------|-------------|
| `__init__.py` | Converter package init |
| `base.py` | Base strategy converter class |
| `indicator_map.py` | Indicator name mapping across platforms |
| `pine_script.py` | TradingView Pine Script to Python converter |
| `templates.py` | Strategy code templates |
| `thinkscript.py` | thinkorswim thinkScript to Python converter |

### 1.24 strategies/distribution/ (11 files)

| File | Description |
|------|-------------|
| `__init__.py` | Distribution package init |
| `custom_distributions.py` | Custom probability distribution definitions |
| `distribution_fit_analyzer.py` | Distribution fitting analysis coordinator |
| `distribution_mega_fit.py` | Mega distribution fitter across all scipy distributions |
| `fitter_advanced.py` | Advanced distribution fitting methods |
| `fitter_location_scale.py` | Location-scale family distribution fitter |
| `fitter_positive_heavy.py` | Positive heavy-tail distribution fitter |
| `influxdb_dist_data_loading.py` | InfluxDB distribution data loading |
| `influxdb_dist_persistence.py` | InfluxDB distribution results persistence |
| `influxdb_dist_reporting.py` | InfluxDB distribution report generation |
| `influxdb_distribution_analysis.py` | InfluxDB distribution analysis coordinator |

### 1.25 strategies/econometrics/ (66 files)

#### Root (22 files)

| File | Description |
|------|-------------|
| `__init__.py` | Econometrics package init |
| `ai_improvement.py` | AI-driven econometric model improvement |
| `catalog.py` | Catalog of 261 econometric tests |
| `cross_broker.py` | Cross-broker econometric analysis |
| `discovery.py` | Econometric test discovery engine |
| `discovery_profiling.py` | Data profiling for test discovery |
| `discovery_scoring.py` | Test applicability scoring |
| `report.py` | Econometric report coordinator |
| `report_output.py` | Report output formatting |
| `report_print.py` | Report console printing |
| `runner.py` | Econometric test runner |
| `stata_generator.py` | STATA code generation from Python results |
| `verification.py` | Econometric verification coordinator |
| `verification_bayesian_mixin.py` | Bayesian verification mixin |
| `verification_distribution_mixin.py` | Distribution verification mixin |
| `verification_financial_mixin.py` | Financial test verification mixin |
| `verification_nonparametric_mixin.py` | Nonparametric verification mixin |
| `verification_parametric_mixin.py` | Parametric verification mixin |
| `verification_time_series_mixin.py` | Time-series verification mixin |

#### runners/ (22 files)

| File | Description |
|------|-------------|
| `__init__.py` | Runners package init |
| `bayesian.py` | Bayesian inference test runner |
| `chi_square.py` | Chi-square test runner |
| `cointegration.py` | Cointegration test runner (Engle-Granger, Johansen) |
| `correlation.py` | Correlation test runner (Pearson, Spearman, Kendall) |
| `diagnostics.py` | Diagnostic test runner (heteroskedasticity, autocorrelation) |
| `distribution.py` | Distribution test runner (normality, goodness-of-fit) |
| `effect_size.py` | Effect size calculation runner (Cohen's d, eta-squared) |
| `financial.py` | Financial-specific test runner (GARCH, VaR) |
| `game_theory.py` | Game theory test runner (Nash equilibrium, payoff matrices) |
| `hmm_regime.py` | Hidden Markov Model regime detection runner |
| `information_theory.py` | Information theory test runner (entropy, mutual information) |
| `ml_validation.py` | Machine learning validation runner (cross-val, feature importance) |
| `multivariate.py` | Multivariate test runner (MANOVA, PCA) |
| `nonparametric.py` | Nonparametric test runner (Mann-Whitney, Kruskal-Wallis) |
| `panel_data.py` | Panel data test runner (fixed effects, random effects) |
| `parametric.py` | Parametric test runner (t-tests, ANOVA) |
| `post_hoc.py` | Post-hoc test runner (Tukey HSD, Bonferroni) |
| `regression.py` | Regression test runner (OLS, WLS, quantile) |
| `robust_outlier.py` | Robust/outlier test runner (Grubbs, Dixon) |
| `survival.py` | Survival analysis runner (Kaplan-Meier, Cox PH) |
| `time_series.py` | Time-series test runner (ADF, KPSS, Phillips-Perron) |

### 1.26 strategies/factor_mining/ (43 files)

| Subdir | File | Description |
|--------|------|-------------|
| root | `__init__.py` | Factor mining package init |
| data/ | `__init__.py`, `features.py`, `loader.py`, `loader_sources.py`, `loader_transform.py`, `universe.py` | Feature engineering, data loading, universe definition |
| dsl/ | `__init__.py`, `operators.py`, `parser.py`, `validator.py` | 70+ operators, expression parser, data leak validator |
| evaluation/ | `__init__.py`, `backtester.py`, `fitness.py`, `metrics.py` | Backtesting, fitness scoring, IC/turnover/decay metrics |
| evolution/ | `__init__.py`, `crossover.py`, `engine.py`, `mutator.py`, `selector.py` | Genetic algorithm evolution engine |
| orchestration/ | `__init__.py`, `campaign.py`, `prompts.py`, `round_runner.py` | Campaign management and AI prompts |
| persistence/ | `__init__.py`, `factor_store.py`, `leaderboard.py`, `session.py` | Storage, leaderboard, session persistence |
| scripts/ | `comparator.py`, `evaluate_factor.py`, `scanner.py`, `show_leaderboard.py` | Factor comparison and evaluation scripts |

### 1.27 strategies/ibkr/ (2 files), strategies/ironbeam/ (2 files), strategies/indicators/ (2 files)

| File | Description |
|------|-------------|
| `ibkr/__init__.py` | IBKR strategies package init |
| `ibkr/adapters.py` | IBKR-specific strategy adapters |
| `ironbeam/__init__.py` | IronBeam strategies package init |
| `ironbeam/adapters.py` | IronBeam-specific strategy adapters |
| `indicators/__init__.py` | Indicators package init |
| `indicators/adapters.py` | Indicator adapter implementations |

### 1.30 strategies/momentum/ (87 files)

| File | Description |
|------|-------------|
| `aema_touch_counter.py` | AEMA touch counter strategy |
| `ar2_model.py` | AR(2) autoregressive model strategy |
| `atr_strategy.py` | ATR (Average True Range) breakout strategy |
| `backtesting_framework.py` | Momentum backtesting framework |
| `commodity_strategy.py` | Commodity momentum strategy |
| `credit_spread_backtest.py` | Credit spread backtesting |
| `credit_spread_construction.py` | Credit spread construction logic |
| `credit_spread_management.py` | Credit spread position management |
| `credit_spread_risk.py` | Credit spread risk analysis |
| `credit_spread_signal.py` | Credit spread entry signal generation |
| `credit_spread_signals.py` | Credit spread signal aggregation |
| `credit_spread_strategy.py` | Credit spread strategy coordinator |
| `ensemble_voting_strategy.py` | Ensemble voting strategy (v1) |
| `ensemble_voting_v2_strategy.py` | Ensemble voting strategy (v2) |
| `event_stat_interpret.py` | Event-driven statistical interpretation |
| `event_stat_tests.py` | Event-driven statistical tests |
| `event_stat_strategy.py` | Event-driven statistical strategy |
| `forex_strategy.py` | Forex momentum strategy |
| `high_sharpe_analysis.py` | High Sharpe ratio analysis |
| `high_sharpe_backtest.py` | High Sharpe ratio backtesting |
| `high_sharpe_momentum.py` | High Sharpe momentum strategy |
| `high_sharpe_multifactor.py` | High Sharpe multifactor strategy |
| `high_sharpe_stat_arb.py` | High Sharpe statistical arbitrage |
| `high_sharpe_volatility.py` | High Sharpe volatility strategy |
| `ibkr_aema_touch_strategy.py` | IBKR AEMA touch strategy |
| `ibkr_backtesting_framework.py` | IBKR momentum backtesting framework |
| `ibkr_commodity_strategy.py` | IBKR commodity momentum strategy |
| `ibkr_forex_strategy.py` | IBKR forex momentum strategy |
| `ibkr_ma_crossover_strategy.py` | IBKR moving average crossover strategy |
| `ibkr_mean_reversion_strategy.py` | IBKR mean reversion strategy |
| `ibkr_momentum_strategy.py` | IBKR momentum strategy |
| `ibkr_trend_following_strategy.py` | IBKR trend following strategy |
| `ichimoku_cloud.py` | Ichimoku Cloud strategy |
| `ichimoku_validation.py` | Ichimoku Cloud signal validation |
| `implied_vol_strategy.py` | Implied volatility strategy |
| `keltner_channels_strategy.py` | Keltner Channels strategy |
| `legal_settlement_strategy.py` | Legal settlement event strategy |
| `order_flow.py` | Order flow analysis coordinator |
| `order_flow_analysis.py` | Order flow analysis methods |
| `order_flow_imbalance.py` | Order flow imbalance detection |
| `order_flow_signals.py` | Order flow signal generation |
| `order_flow_strategy.py` | Order flow trading strategy |
| `parameterized_archetypes.py` | Parameterized strategy archetypes |
| `parameterized_catalog.py` | Archetype parameter catalog |
| `portfolio_div_analysis.py` | Portfolio diversification analysis |
| `portfolio_div_backtest.py` | Portfolio diversification backtesting |
| `portfolio_div_correlation.py` | Portfolio diversification correlation analysis |
| `portfolio_div_optimizer.py` | Portfolio diversification optimizer |
| `portfolio_div_strategy.py` | Portfolio diversification strategy |
| `reward_auto_improver.py` | Reward function auto-improvement |
| `reward_network.py` | Neural reward network for RL |
| `reward_trainer.py` | Reward network training loop |
| `strat_001_momentum_basic.py` | Strategy 001: Basic momentum |
| `strat_002_momentum_rsi.py` | Strategy 002: RSI momentum |
| `strat_003_macd_crossover.py` | Strategy 003: MACD crossover |
| `strat_004_bollinger_breakout.py` | Strategy 004: Bollinger Band breakout |
| `strat_005_mean_reversion.py` | Strategy 005: Mean reversion |
| `strat_006_trend_following.py` | Strategy 006: Trend following |
| `strat_007_volatility_regime.py` | Strategy 007: Volatility regime |
| `strat_008_pairs_trading.py` | Strategy 008: Pairs trading |
| `strat_009_sector_rotation.py` | Strategy 009: Sector rotation |
| `strat_010_momentum_factor.py` | Strategy 010: Momentum factor |
| `strat_011_value_momentum.py` | Strategy 011: Value-momentum hybrid |
| `strat_012_overnight_drift.py` | Strategy 012: Overnight drift |
| `strat_013_earnings_momentum.py` | Strategy 013: Earnings momentum |
| `strat_014_volume_breakout.py` | Strategy 014: Volume breakout |
| `strat_015_dual_momentum.py` | Strategy 015: Dual momentum |
| `strat_016_adaptive_momentum.py` | Strategy 016: Adaptive momentum |
| `strat_017_cross_asset.py` | Strategy 017: Cross-asset momentum |
| `strat_018_seasonal.py` | Strategy 018: Seasonal patterns |
| `strat_019_microstructure.py` | Strategy 019: Market microstructure |
| `strat_020_regime_switch.py` | Strategy 020: Regime switching |
| `strat_09X_experimental.py` | Strategy 09X: Experimental strategies |
| `technical_indicators.py` | Technical indicator calculations |
| `trend_following_strategy.py` | Trend following strategy |
| `trend_strategy.py` | Core trend strategy |
| `trend_strategy_analysis.py` | Trend strategy analysis methods |
| `trend_strategy_backtest.py` | Trend strategy backtesting |
| `trend_strategy_optimization.py` | Trend strategy parameter optimization |
| `trend_strategy_risk.py` | Trend strategy risk management |
| `trend_strategy_signals.py` | Trend strategy signal generation |
| `trend_strategy_utils.py` | Trend strategy utilities |
| `trend_strategy_validation.py` | Trend strategy validation |
| `trigger_scheduler.py` | Momentum strategy trigger scheduling |
| `volatility_signal_validation.py` | Volatility signal validation |

### 1.31 strategies/orchestration/ (4 files)

| File | Description |
|------|-------------|
| `__init__.py` | Orchestration package init |
| `orchestrator.py` | Multi-strategy orchestration engine |
| `position_sizer.py` | Position sizing algorithms (Kelly, risk parity) |
| `signal_aggregator.py` | Signal aggregation across strategies |

### 1.32 strategies/reinforcement_learning/ (13 files)

| File | Description |
|------|-------------|
| `__init__.py` | RL package init |
| `bollinger_pytorch_rl.py` | Bollinger Band RL agent (PyTorch) |
| `env_config.py` | RL environment configuration |
| `eval_utils.py` | RL evaluation utilities |
| `indicators.py` | Technical indicators for RL state space |
| `stdev_analysis.py` | Standard deviation analysis for RL rewards |
| `test_agent.py` | RL agent testing script |
| `test_bollinger_rl.py` | Bollinger RL agent test suite |
| `trading_env.py` | OpenAI Gym trading environment |
| `train_agent.py` | RL agent training loop |
| `_build_nb_final.py` | Notebook-to-script builder |

### 1.33 strategies/strategy_improvement/ (23 files)

| Subdir | File | Description |
|--------|------|-------------|
| audit/ | `code_analyzer.py` | Strategy code quality analyzer |
| data/ | `loader.py` | Strategy improvement data loader |
| evaluation/ | `batch_tester.py`, `metrics_aggregator.py`, `portfolio_optimizer.py` | Batch testing, metrics, portfolio optimization |
| orchestration/ | `ai_orchestrator.py`, `campaign.py`, `gradient_optimizer.py`, `improvement_runner.py`, `mega_improver.py`, `optimized_params_cache.py`, `prompts.py`, `stagnation_detector.py` | AI orchestration, gradient optimization, stagnation detection |
| persistence/ | `leaderboard.py`, `session.py` | Improvement leaderboard and session persistence |
| inits | `__init__.py` (x6), `scripts/__init__.py` | Package init files |

---

### 1.34 scripts/ (75+ files)

#### scripts/ Root (~21 files)

| File | Description |
|------|-------------|
| `__init__.py` | Scripts package init |
| `atomic_ai_run.py` | Atomic AI-assisted trading run |
| `continuous_collector.py` | Continuous market data collection service |
| `data_backend_audit.py` | Data backend audit across all storage layers |
| `data_monitor.py` | Real-time data feed monitoring |
| `data_repair.py` | Data gap and corruption repair |
| `data_sync_service.py` | Cross-device data synchronization service |
| `dl_all_wrapper.py` | Download-all wrapper for all brokers |
| `docker_reset.py` | Docker environment reset script |
| `docstring_fixer.py` | Automated docstring correction |
| `evaluate_ai_library.py` | AI library evaluation benchmarks |
| `generate_data_summary.py` | Data coverage summary report generator |
| `icloud_sync.py` | iCloud file synchronization |
| `influxdb_backup.py` | InfluxDB backup automation |
| `isolation_scan.py` | Docker isolation security scan |
| `migrate_influxdb.py` | InfluxDB migration between versions |
| `portfolio_downloader.py` | Multi-broker portfolio download |
| `preflight_test.py` | Pre-flight system test |
| `quality_fixer.py` | Code quality auto-fixer |
| `run_agents_silent.py` | Run all agents in silent mode |
| `run_signal_validation.py` | Signal validation runner |

#### scripts/hooks/ (1 file): `install_hooks.py` - Git hook installation

#### scripts/ibkr/ (16 files)

| File | Description |
|------|-------------|
| `__init__.py` | IBKR scripts package init |
| `bond_scanner.py` | IBKR bond market scanner script |
| `concurrent_downloader.py` | IBKR concurrent historical data downloader |
| `contract_builder.py` | IBKR contract object builder |
| `market_hours.py` | IBKR market hours checker |
| `ohlc_tracker.py` | IBKR OHLC bar tracker |
| `ohlc_tracker_data_mixin.py` | OHLC tracker data handling mixin |
| `realtime_puller.py` | IBKR real-time data puller |
| `test_all.py` | IBKR scripts test suite |
| `tick_tracker.py` | IBKR tick data tracker |
| `tick_tracker_callbacks_mixin.py` | Tick tracker callback mixin |
| `tick_tracker_connection_mixin.py` | Tick tracker connection mixin |
| `tick_tracker_display_mixin.py` | Tick tracker display mixin |
| `tick_tracker_subscription_mixin.py` | Tick tracker subscription mixin |
| `utils.py` | IBKR script utilities |

#### scripts/ironbeam/ (4 files): `__init__.py`, `inspect_ironbeam_pkl.py`, `resample_ironbeam_data.py`, `resample_service.py`

#### scripts/maintenance/ (9 files)

| File | Description |
|------|-------------|
| `__init__.py` | Maintenance scripts package init |
| `archive_docker_iteration.py` | Archive old Docker iteration files |
| `cleanup_test_data.py` | Test data cleanup |
| `compact_csvs.py` | CSV file compaction |
| `compactor_runner.py` | CSV compactor runner |
| `extract_data.py` | Data extraction from archives |
| `prune_archives.py` | Archive pruning by age |
| `soak_runner.py` | Soak test runner for stability testing |
| `trim_hot_csv.py` | Trim hot CSV files to limit size |

#### scripts/monitoring/ (1 file): `broker_data_graphs.py` - Broker data quality visualization

#### scripts/moomoo/ (6 files): `__init__.py`, `constants.py`, `historical_downloader.py`, `ohlc_tracker.py`, `realtime_puller.py`, `tick_tracker.py`

#### scripts/pipeline/ (1 file): `data_scan.py` - Data pipeline scanning and validation

#### scripts/schwab/ (9 files)

| File | Description |
|------|-------------|
| `__init__.py` | Schwab scripts package init |
| `auth_setup.py` | Schwab OAuth initial setup |
| `auto_auth.py` | Schwab automated authentication |
| `historical_downloader.py` | Schwab historical data downloader |
| `ohlc_tracker.py` | Schwab OHLC bar tracker |
| `realtime_puller.py` | Schwab real-time data puller |
| `reauth.py` | Schwab re-authentication script |
| `refresh_cron.py` | Schwab token refresh cron job |
| `tick_tracker.py` | Schwab tick data tracker |

#### scripts/setup/ (2 files): `__init__.py`, `bootstrap_influx_tokens.py`

#### scripts/tastyfx/ (3 files): `__init__.py`, `oauth_setup.py`, `tastyfx_account.py`

#### scripts/tastytrade/ (9 files): `__init__.py`, `historical_downloader.py`, `ohlc_tracker.py`, `rate_limiter.py`, `realtime_puller.py`, `session_manager.py`, `test_connection.py`, `test_historical_downloader.py`, `tick_tracker.py`

---

### 1.35 tests/ (80+ files)

#### tests/ Root (44 files)

| File | Description |
|------|-------------|
| `conftest.py` | Test configuration and fixtures |
| `test_account_models.py` | Account Pydantic model tests |
| `test_agent_slippage_review.py` | Slippage review agent tests |
| `test_backtest_runner.py` | Backtesting runner tests |
| `test_base_client.py` | Base BrokerClient tests |
| `test_broker_base.py` | Broker base class tests |
| `test_broker_registry.py` | BrokerRegistry tests |
| `test_builtin_strategies.py` | Built-in strategy tests |
| `test_capabilities.py` | Broker capabilities tests |
| `test_coinbase_client.py` | Coinbase client tests |
| `test_dashboard.py` | Flask dashboard tests |
| `test_data_pipeline.py` | Data pipeline tests |
| `test_etrade_client.py` | E*TRADE client tests |
| `test_historical_data.py` | Historical data retrieval tests |
| `test_ibkr_client.py` | IBKR client tests |
| `test_ibkr_oco_orders.py` | IBKR OCO order tests |
| `test_influxdb.py` | InfluxDB integration tests |
| `test_ironbeam_client.py` | IronBeam client tests |
| `test_models.py` | Pydantic model tests |
| `test_moomoo_client.py` | Moomoo client tests |
| `test_ninjatrader_client.py` | NinjaTrader client tests |
| `test_oco_orders.py` | OCO order tests (broker-agnostic) |
| `test_parameterized_strategies.py` | Parameterized strategy tests |
| `test_pnl_service.py` | P&L service tests |
| `test_portfolio_downloader.py` | Portfolio downloader tests |
| `test_redis_cache.py` | Redis cache tests |
| `test_reward_network.py` | Reward network tests |
| `test_schwab_client.py` | Schwab client tests |
| `test_service_watchdog.py` | Service watchdog tests |
| `test_stagnation_detector.py` | Stagnation detector tests |
| `test_strategies.py` | Strategy framework tests |
| `test_strategy_converter.py` | Strategy converter tests |
| `test_strategy_registry.py` | Strategy registry tests |
| `test_strategy_runner.py` | Strategy runner tests |
| `test_stub_brokers.py` | Stub broker tests (Fidelity, Vanguard) |
| `test_symbol_adapters.py` | Symbol adapter tests (all brokers) |
| `test_tastytrade_client.py` | TastyTrade client tests |
| `test_ticker_formatter.py` | Ticker formatter tests |
| `test_tradestation_client.py` | TradeStation client tests |
| `test_trigger_scheduler.py` | Trigger scheduler tests |
| `test_unified_types.py` | Unified type system tests |
| `test_watchdog.py` | BrokerWatchdog tests |
| `test_websocket_client.py` | WebSocket client tests |
| `test_webull_client.py` | Webull client tests |

#### tests/unit/ (28 files)

| File | Description |
|------|-------------|
| `__init__.py` | Unit tests package init |
| `test_agent_recommendations.py` | Agent recommendation output tests |
| `test_alpha_scan.py` | Alpha scan tests |
| `test_archive_maintenance.py` | Archive maintenance tests |
| `test_archive_reader.py` | Archive reader tests |
| `test_compact_csvs.py` | CSV compaction tests |
| `test_compactor_runner.py` | Compactor runner tests |
| `test_compose_files.py` | Docker compose file tests |
| `test_data_pipeline_tagging.py` | Data pipeline tagging tests |
| `test_data_scan.py` | Data scan tests |
| `test_docker_backend_prebuilt.py` | Docker backend prebuilt image tests |
| `test_docker_broker_builder.py` | Docker broker builder tests |
| `test_docker_stats_renderer.py` | Docker stats renderer tests |
| `test_exit_analyzer.py` | Exit analyzer tests |
| `test_fetch_broker_container_stats.py` | Broker container stats fetch tests |
| `test_heartbeat.py` | Heartbeat monitoring tests |
| `test_mode_controller.py` | Mode controller tests |
| `test_runtime_guard.py` | Runtime guard tests |
| `test_tag_helpers.py` | Tag helper tests |
| `test_tastytrade_rate_limiter.py` | TastyTrade rate limiter tests |
| `test_today_bootstrap_cache.py` | Bootstrap cache tests |
| `test_today_compose_dedupe.py` | Compose deduplication tests |
| `test_today_extract_data.py` | Extract data tests |
| `test_today_l1_quote.py` | L1 quote tests |
| `test_today_persisted_mode.py` | Persisted mode tests |
| `test_today_secrets_export.py` | Secrets export tests |
| `test_today_soak_runner.py` | Soak runner tests |
| `test_today_storage_sync.py` | Storage sync tests |
| `test_today_write_tracker.py` | Write tracker tests |

#### tests/integration/ (4 files): `__init__.py`, `conftest.py`, `test_cli_commands.py`, `test_paper_trading.py`

---

## 2. InterActiveBrokers Project

**Path:** `D:\Code\InterActiveBrokers_Project\` | **Files:** ~734
> **Also on F:** `F:\InterActiveBrokers-Project\`

IBKR historical data downloader and portfolio management system covering 500+ tickers across futures, stocks, forex, indices, and bonds.

### 2.1 Root: `run.py`, `device_paths.py`, `docker-entrypoint.py`, `run_demo.py`, `run_live.py`

### 2.2 agents/ (16 files): `__init__.py`, `Agent_01_code_cleanup.py` through `Agent_15_docker_venv.py`

### 2.3 src/core/ (10 files): `__init__.py`, `main.py`, `ib_client.py`, `client_id_manager.py`, `env_check.py`, `forex_downloader.py`, `futures_forex_downloader.py`, plus 4 archived main versions

### 2.4 src/data/ (13 files): `__init__.py`, `data_fetcher.py`, `data_fetcher_sequential.py`, `concurrent_fetcher.py`, `data_manager.py`, `data_sync.py`, `master_file_manager.py`, `portfolio_consolidator.py`, `margin_updater.py`, `tick_data_fetcher.py`, `influxdb_data_writer.py`, `csv_to_json/csv_to_json_converter.py`, `csv_to_json/check_data_coverage.py`, `json_to_csv/json_to_csv_exporter.py`

### 2.5 src/getTimeFrameData/ (~350 files)

`base_fetcher.py`, `generate_scripts.py` plus:

- **futures/** (119 files) - 17 contracts x 7 timeframes: ES, NQ, YM, RTY, GC, SI, HG, CL, NG, ZC, ZS, ZW, 6E, 6B, 6J, ZB, ZN
- **stocks/** (105 files) - 15 stocks x 7 timeframes: AAPL, MSFT, GOOGL, AMZN, NVDA, TSLA, META, SPY, QQQ, DIA, IWM, JPM, BRK.B, XOM, V
- **forex/** (105 files) - 15 pairs x 7 timeframes: EURUSD, GBPUSD, USDJPY, EURJPY, GBPJPY, USDCAD, USDCHF, AUDUSD, AUDJPY, NZDUSD, EURAUD, EURCHF, EURGBP, USDMXN, USDZAR
- **indices/** (63 files) - 9 indices x 7 timeframes: SPX, NDX, DJI, RUT, VIX, FTSE, DAX, NIKKEI, HSI
- **bonds/** (63 files) - 9 ETFs x 7 timeframes: TLT, SHY, IEF, BND, LQD, HYG, TIP, MUB, EMB

Each has `{SYMBOL}_1min.py`, `{SYMBOL}_5min.py`, `{SYMBOL}_15min.py`, `{SYMBOL}_30min.py`, `{SYMBOL}_1hr.py`, `{SYMBOL}_4hr.py`, `{SYMBOL}_1day.py`

### 2.6 src/accounting/ (5 files): `__init__.py`, `order_tracker.py`, `pnl_calculator.py`, `business_fees.py`, `profit_distribution.py`

### 2.7 src/orders/ (8 files): `__init__.py`, `place_order.py`, `cancel_order.py`, `modify_order.py`, `order_types.py`, `order_expiration.py`, `oco_orders.py`, `active_orders/get_orders.py`

### 2.8 src/portfolioMGT/ (6 files): `__init__.py`, `account_info.py`, `positions.py`, `pnl_tracker.py`, `fee_tracker.py`, `trade_history.py`

### 2.9 src/contracts/ (2 files): `__init__.py`, `contract_samples.py`

### 2.10 src/strategies/ (76 files)

Root (8 files): `__init__.py`, `base_strategy.py`, `strategy_logger.py`, `strategy_tester.py`, `aema_touch_counter.py`, `trigger_scheduler.py`, `influxdb_writer.py`, `statistical_analyzer.py`

11 strategy folders (01_MA_Crossover through 11_AEMA_Touch_Counter), each with `strategy.py`, `live/__init__.py`, `test/__init__.py`, `test/test_*.py`

Testing_Strategy/ (17 files): `__init__.py`, `backtesting_framework.py`, `test_all_strategies.py`, 11 variant tests, `visualization_dashboard.py`, `strategy_comparison.py`, `performance_report.py`

### 2.11 src/utils/ (10 files): `__init__.py`, `logger.py`, `contracts.py`, `market_hours.py`, `ticker_validator.py`, `data_cleanup.py`, `location_checker.py`, `log_cleanup.py`, `rate_limit_tracker.py`, `time_tracker.py`

### 2.12 src/visualization/ (12 files): `main_runner.py`, `python_chart.py`, core/ (3 files), dashboard/ (3 files), runners/ (3 files)

### 2.13 scripts/ (~32 files)

Root (6): `healthcheck.py`, `watchdog.py`, `test_tws_connection.py`, `test_historical_data.py`, `test_multi_request.py`, `test_tws_verbose.py`
data_management/ (3): `consolidate_csv.py`, `create_excel_csv.py`, `test_master_files.py`
data_tools/ (4): `export_to_excel.py`, `organize_data_files.py`, `standardize_csv_format.py`, `verify_data_integrity.py`
maintenance/ (6): `analyze_log_errors.py`, `archive_old_logs.py`, `archive_old_versions.py`, `changelog_logger.py`, `sync_all_locations.py`, `verify_sync.py`
optimization/ (1): `optimize_file_iteration.py`
security/ (2): `generate_key.py`, `decrypt_data.py`
testing/ (3): `run_comprehensive_test.py`, `run_quick_test.py`, `test_all_timeframes.py`
utilities/ (1): `check_indices.py`

### 2.14 tests/ (6 files): `run_comprehensive_test.py`, `run_quick_test.py`, `test_all_timeframes.py`, `test_error_catchers.py`, `test_forex_downloader.py`, `validate_config_tickers.py`

### 2.15 OldIterations/ (37 files): `main_v01.py` through `main_v37.py`

### 2.16 thirty_seconds/ (4 files): `ohlc_tracker.py`, `realtime_puller.py`, `tick_tracker.py`, `test_popup.py`

---

## 3. Finance - Course Projects

**Path:** `D:\Code\Finance\` | **Files:** ~331
> **Also on F:** `F:\FinanceCode\`, `F:\Efficient_Frontier\`, `F:\CAPM_FAMAFRENCH\`

### 3.1 Root (3 files): `run_all.py`, `setup.py`, `__init__.py`

### 3.2 BondConfigurations/ (29 files)

| File | Description |
|------|-------------|
| `__init__.py` | Bond configurations package init |
| `run_cli.py` | Bond analysis CLI entry point |
| `bond_math.py` | Core bond pricing engine (yield, duration, convexity, DV01) |
| `bond_pricing.py` | Bond pricing calculations |
| `bond_yield.py` | Yield-to-maturity and current yield |
| `bond_duration.py` | Modified and Macaulay duration |
| `bond_convexity.py` | Convexity calculations |
| `bond_dv01.py` | Dollar value of a basis point |
| `create_hmk_workbook.py` | Homework Excel workbook generator |
| `create_bond_workbook.py` | Bond analysis Excel workbook |
| `excel_formatter.py` | Excel formatting utilities |
| `excel_charts.py` | Excel chart generation |
| `data_loader.py` | Bond data loading |
| `yield_curve.py` | Yield curve construction |
| `spot_rate.py` | Spot rate calculations |
| `forward_rate.py` | Forward rate calculations |
| `par_rate.py` | Par rate calculations |
| `zero_coupon.py` | Zero-coupon bond pricing |
| `callable_bond.py` | Callable bond pricing |
| `putable_bond.py` | Putable bond pricing |
| `floating_rate.py` | Floating rate note calculations |
| `credit_spread.py` | Credit spread analysis |
| `term_structure.py` | Term structure modeling |
| `immunization.py` | Portfolio immunization strategies |
| `sensitivity.py` | Interest rate sensitivity analysis |
| `test_bonds.py` | Bond calculation unit tests |
| `test_workbook.py` | Workbook generation tests |
| `utils.py` | Bond utility functions |
| `constants.py` | Bond market constants |

### 3.3 CAPM_French/ (38 files): `__init__.py`, `run_cli.py`, `capm.py`, `fama_french_3.py`, `fama_french_5.py`, `regression.py`, `risk_free_rate.py`, `market_premium.py`, `beta_calculator.py`, `alpha_calculator.py`, `sharpe_ratio.py`, `treynor_ratio.py`, `information_ratio.py`, `sortino_ratio.py`, `create_workbook.py`, `create_hmk_workbook.py`, `excel_formatter.py`, `excel_charts.py`, `data_loader.py`, `data_fetcher.py`, `portfolio_analysis.py`, `sml_plot.py`, `cml_plot.py`, `factor_analysis.py`, `rolling_beta.py`, `residual_analysis.py`, `hypothesis_tests.py`, `bootstrap.py`, `test_capm.py`, `test_fama_french.py`, `test_regression.py`, `test_workbook.py`, `utils.py`, `constants.py`, `config.py`, `visualization.py`, `report_generator.py`, `summary_stats.py`

### 3.4 Efficient_Frontier/ (38 files): `__init__.py`, `run_cli.py`, `efficient_frontier.py`, `mean_variance.py`, `min_variance.py`, `max_sharpe.py`, `risk_parity.py`, `black_litterman.py`, `portfolio_optimizer.py`, `constraint_builder.py`, `covariance.py`, `shrinkage.py`, `expected_returns.py`, `create_workbook.py`, `create_hmk_workbook.py`, `excel_formatter.py`, `excel_charts.py`, `data_loader.py`, `data_fetcher.py`, `monte_carlo.py`, `random_portfolios.py`, `tangent_portfolio.py`, `cal_line.py`, `frontier_plot.py`, `asset_allocation.py`, `rebalancing.py`, `backtester.py`, `performance.py`, `drawdown.py`, `var_cvar.py`, `test_frontier.py`, `test_optimizer.py`, `test_workbook.py`, `utils.py`, `constants.py`, `config.py`, `visualization.py`, `report_generator.py`

### 3.5 ExamTwo/ (4 files): `__init__.py`, `exam2_solver.py`, `pro_forma.py`, `bond_pricing_exam.py`

### 3.6 Exam3Prep/ (8 files): `__init__.py`, `lbo_analysis.py`, `valuation_models.py`, `wacc_calculator.py`, `capital_structure.py`, `merger_model.py`, `create_workbook.py`, `test_exam3.py`

### 3.7 Exam3Prepv2/ (13 files): `__init__.py`, `lbo_analysis_v2.py`, `valuation_dcf.py`, `valuation_comps.py`, `valuation_precedent.py`, `wacc_calculator_v2.py`, `capital_structure_v2.py`, `sensitivity_analysis.py`, `scenario_analysis.py`, `create_workbook_v2.py`, `excel_formatter.py`, `test_exam3_v2.py`, `utils.py`

### 3.8 ExcelCleaning/ (18 files): `__init__.py`, `cleaner.py`, `column_standardizer.py`, `date_parser.py`, `duplicate_remover.py`, `missing_data.py`, `outlier_detector.py`, `data_type_fixer.py`, `formula_auditor.py`, `merge_files.py`, `split_files.py`, `format_fixer.py`, `cell_validator.py`, `batch_processor.py`, `report_generator.py`, `test_cleaner.py`, `utils.py`, `config.py`

### 3.9 Options/ (30 files): `__init__.py`, `black_scholes.py`, `binomial_tree.py`, `monte_carlo_option.py`, `greeks.py`, `implied_volatility.py`, `volatility_surface.py`, `volatility_smile.py`, `put_call_parity.py`, `option_strategies.py`, `covered_call.py`, `protective_put.py`, `straddle.py`, `strangle.py`, `butterfly.py`, `iron_condor.py`, `vertical_spread.py`, `calendar_spread.py`, `payoff_diagram.py`, `create_workbook.py`, `excel_formatter.py`, `data_loader.py`, `chain_analyzer.py`, `risk_metrics.py`, `portfolio_greeks.py`, `test_black_scholes.py`, `test_greeks.py`, `test_strategies.py`, `utils.py`, `constants.py`

### 3.10 Percentage_of_Sales_Analysis/ (30 files): `__init__.py`, `run_cli.py`, `pct_of_sales.py`, `efn_calculator.py`, `pro_forma_builder.py`, `income_statement.py`, `balance_sheet.py`, `cash_flow.py`, `growth_analysis.py`, `ratio_analysis.py`, `sensitivity.py`, `create_workbook.py`, `create_hmk_workbook.py`, `excel_formatter.py`, `excel_charts.py`, `data_loader.py`, `data_parser.py`, `regression_forecast.py`, `seasonal_adjustment.py`, `trend_analysis.py`, `working_capital.py`, `debt_capacity.py`, `dividend_policy.py`, `sustainable_growth.py`, `test_pct_sales.py`, `test_efn.py`, `test_workbook.py`, `utils.py`, `constants.py`, `config.py`

### 3.11 credit-spreading-tool/ (19 files): `__init__.py`, `run.py`, `spread_analyzer.py`, `bond_selector.py`, `yield_spread.py`, `oas_calculator.py`, `z_spread.py`, `credit_rating.py`, `default_probability.py`, `recovery_rate.py`, `sector_spread.py`, `historical_spreads.py`, `spread_curves.py`, `create_workbook.py`, `excel_formatter.py`, `data_loader.py`, `visualization.py`, `test_spreads.py`, `utils.py`

### 3.12 fi-market-analysis/ (21 files): `__init__.py`, `run.py`, `market_overview.py`, `treasury_analysis.py`, `corporate_analysis.py`, `municipal_analysis.py`, `mbs_analysis.py`, `yield_curve_analysis.py`, `rate_forecast.py`, `fed_policy.py`, `inflation_analysis.py`, `duration_management.py`, `sector_allocation.py`, `relative_value.py`, `create_workbook.py`, `excel_formatter.py`, `data_loader.py`, `visualization.py`, `test_analysis.py`, `utils.py`, `constants.py`

### 3.13 industry-risk-framework/ (18 files): `__init__.py`, `run.py`, `risk_scorer.py`, `sector_analysis.py`, `competitive_analysis.py`, `regulatory_risk.py`, `cyclicality.py`, `market_structure.py`, `barrier_analysis.py`, `supply_chain_risk.py`, `technology_risk.py`, `create_workbook.py`, `excel_formatter.py`, `data_loader.py`, `visualization.py`, `report_generator.py`, `test_risk.py`, `utils.py`

### 3.14 roi-presentation-toolkit/ (21 files): `__init__.py`, `run.py`, `roi_calculator.py`, `npv_calculator.py`, `irr_calculator.py`, `payback_period.py`, `profitability_index.py`, `sensitivity_analysis.py`, `scenario_builder.py`, `cash_flow_model.py`, `risk_adjustment.py`, `presentation_builder.py`, `slide_templates.py`, `chart_generator.py`, `create_workbook.py`, `excel_formatter.py`, `data_loader.py`, `visualization.py`, `test_roi.py`, `utils.py`, `constants.py`

### 3.15 sales-playbook/ (20 files): `__init__.py`, `run.py`, `revenue_model.py`, `forecast_engine.py`, `pipeline_analyzer.py`, `quota_calculator.py`, `commission_model.py`, `territory_planner.py`, `customer_segmentation.py`, `churn_predictor.py`, `ltv_calculator.py`, `cac_calculator.py`, `create_workbook.py`, `excel_formatter.py`, `data_loader.py`, `visualization.py`, `report_generator.py`, `test_sales.py`, `utils.py`, `constants.py`

### 3.16 shared/ (8 files): `__init__.py`, `bond_math.py`, `excel_helpers.py`, `regression.py`, `tax_utils.py`, `data_utils.py`, `financial_utils.py`, `constants.py`

---

## 4. IronBeam - Futures Trading

**Path:** `D:\Code\IronBeam\` | **Files:** ~260
> **Also on F:** `F:\IronBeam_IBKR_likeCode\`

### 4.1 Root (4 files): `run.py`, `run_demo.py`, `run_live.py`, `main.py`

### 4.2 IronBeam_API_Code/core/ (19 files): `__init__.py`, `account_manager.py`, `auth_manager.py`, `client.py`, `config.py`, `connection_manager.py`, `contract_specs.py`, `historical_data.py`, `market_data.py`, `order_manager.py`, `positions_manager.py`, `rate_limiter.py`, `risk_manager.py`, `session_manager.py`, `symbol_manager.py`, `websocket_manager.py`, `ws_handlers.py`, `exceptions.py`, `utils.py`

### 4.3 IronBeam_API_Code/data/ (9 files): `__init__.py`, `data_manager.py`, `data_fetcher.py`, `data_storage.py`, `influxdb_writer.py`, `csv_exporter.py`, `json_saver.py`, `data_validator.py`, `resampler.py`

### 4.4 IronBeam_API_Code/config/ (2 files): `__init__.py`, `settings.py`

### 4.5 IronBeam_API_Code/strategy/ (2 files): `__init__.py`, `base_strategy.py`

### 4.6 IronBeam_API_Code/strategy/algo_strategies/Testing/ (42 files): `__init__.py`, `test_strategy_01.py`-`test_strategy_20.py`, `momentum_test.py`, `mean_reversion_test.py`, `trend_following_test.py`, `breakout_test.py`, `scalping_test.py`, `pairs_test.py`, `volatility_test.py`, `rsi_test.py`, `macd_test.py`, `bollinger_test.py`, `vwap_test.py`, `atr_test.py`, `ichimoku_test.py`, `stochastic_test.py`, `fibonacci_test.py`, `ema_cross_test.py`, `donchian_test.py`, `keltner_test.py`, `supertrend_test.py`, `config.py`

### 4.7 IronBeam_API_Code/accounting/ (8 files): `__init__.py`, `pnl_calculator.py`, `fee_calculator.py`, `profit_distribution.py`, `trade_journal.py`, `tax_reporter.py`, `reconciliation.py`, `margin_tracker.py`

### 4.8 IronBeam_API_Code/agents/ (29 files): `__init__.py`, `agent_accounting.py`, `agent_architecture_doc.py`, `agent_broker_integration.py`, `agent_changelog.py`, `agent_cli_review.py`, `agent_code_quality.py`, `agent_comment_review.py`, `agent_concurrency_optimizer.py`, `agent_data_integrity.py`, `agent_deep_learning.py`, `agent_error_handling.py`, `agent_git_push_notes.py`, `agent_influxdb_manager.py`, `agent_infrastructure.py`, `agent_json_consolidator.py`, `agent_logger_standards.py`, `agent_oop_analysis.py`, `agent_platform_compat.py`, `agent_progress_bars.py`, `agent_redis_optimizer.py`, `agent_strategy_validator.py`, `agent_test_coverage.py`, `agent_timeframe_analysis.py`, `agent_trigger_scheduler.py`, `agent_visualization.py`, `agent_watchdog_format.py`, `scan_config.py`

### 4.9 IronBeam_API_Code/cli/ (1 file): `cli.py`

### 4.10 IronBeam_API_Code/utils/ (9 files): `__init__.py`, `logger.py`, `time_utils.py`, `validators.py`, `formatters.py`, `decorators.py`, `concurrency.py`, `file_utils.py`, `constants.py`

### 4.11 IronBeam_API_Code/gui/ (8 files): `__init__.py`, `main_window.py`, `order_panel.py`, `positions_panel.py`, `chart_widget.py`, `market_data_panel.py`, `account_panel.py`, `styles.py`

### 4.12 IronBeam_API_Code/tests/ (24 files): `__init__.py`, `conftest.py`, `test_account_manager.py`, `test_auth.py`, `test_client.py`, `test_connection.py`, `test_contract_specs.py`, `test_data_fetcher.py`, `test_historical_data.py`, `test_market_data.py`, `test_order_manager.py`, `test_pnl.py`, `test_positions.py`, `test_rate_limiter.py`, `test_risk_manager.py`, `test_session.py`, `test_strategies.py`, `test_symbol_manager.py`, `test_websocket.py`, `test_ws_handlers.py`, `test_data_storage.py`, `test_csv_exporter.py`, `test_integration.py`, `test_end_to_end.py`

### 4.13 IronBeam_API_Code/scripts/ (23 files): `__init__.py`, `download_historical.py`, `setup_account.py`, `test_connection.py`, `monitor_positions.py`, `export_trades.py`, `backup_data.py`, `cleanup_logs.py`, `generate_reports.py`, `sync_data.py`, `validate_config.py`, `benchmark_latency.py`, `check_market_hours.py`, `update_contracts.py`, `migrate_data.py`, `inspect_ws_data.py`, `reset_session.py`, `audit_orders.py`, `reconcile_fills.py`, `performance_report.py`, `risk_report.py`, `daily_summary.py`, `weekly_digest.py`

### 4.14 IronBeam_API_Code/notebooks/ (3 files): `data_exploration.ipynb`, `strategy_analysis.ipynb`, `performance_review.ipynb`

### 4.15 ironbeam_starter_test/ (10 files): `__init__.py`, `basic_connection.py`, `place_test_order.py`, `get_account_info.py`, `get_positions.py`, `get_historical.py`, `stream_quotes.py`, `stream_trades.py`, `cancel_test_order.py`, `full_workflow.py`

---

## 5. Spring 2026 - University Coursework

**Path:** `D:\Code\Spring2026\` | **Files:** ~48
> **Also on F:** `F:\Spring2026\`

### 5.1 BMI_Intro_to_Leadership/ (10 files)
| File | Description |
|------|-------------|
| AssignmentOne/leadership_self_assessment.py | Personal leadership strengths/weaknesses assessment using Purdue LDP framework |
| AssignmentOne/generate_essays.py | Generates four MLA essays (reflective, expository, problem-solution, persuasive) on leadership assessment |
| CaseStudyOne/generate_essays.py | Four MLA essays on Southwest Hospital leadership case study |
| CaseStudyTwo/generate_essays.py | Four MLA essays on Southwest Hospital physician engagement |
| Week 2/upload_to_youtube.py | Uploads BMI 6305 week 2 lecture videos to YouTube (private) |
| Week 3/upload_to_youtube.py | Uploads BMI 6305 week 3 lecture videos to YouTube |
| Week 6/upload_to_youtube.py | Uploads BMI 6305 week 6 lecture videos to YouTube |
| upload_bmi_videos.py | Master uploader for all BMI 6305 lecture videos |
| verify_youtube_uploads.py | Verifies uploaded videos for existence, privacy, processing, playback |

### 5.2 NURS_7730/ (20+ files)
| File | Description |
|------|-------------|
| generate_essays.py | Four APA essays on NP payer mix and sustainable practice |
| generate_industry_docs.py | APA documents on industry relationships |
| generate_industry_essay.py | Reflective essay on professional healthcare industry relationships |
| generate_industry_summary_v2.py | Detailed v2 summary on industry relationships (strict APA) |
| Week_One/generate_essays.py | Four APA discussion posts on sustainable practice and payer mix |
| Week_Two/generate_essays.py | Four discussion posts on maximizing reimbursement |
| Week_Three/generate_essays.py | Four discussion posts on legal aspects of advanced clinical nursing |
| Week_Three/generate_quiz_ethical.py | Ethical issues in advanced practice quiz document |
| Week_Four/generate_essays.py | Four discussion posts on addressing ethical concerns in nursing |
| Week_Five/generate_essays.py | Four discussion posts on NP revenue management |
| Week_Five/verify_post5_numbers.py | Verification utility validating numeric claims in Discussion Post 5 |
| case5/generate_essays.py | Four discussion posts on NP revenue management (alternate) |
| Week_One_docker/generate_essays.py | Docker-compatible version of week 1 posts |
| Week_Two_docker/generate_essays.py | Docker-compatible version of week 2 posts |
| Week_Three_docker/generate_essays.py | Docker-compatible version of week 3 posts |
| Week_Three_final/generate_essays.py | Final version of week 3 legal aspects posts |
| Week_Three_final/generate_quiz_ethical.py | Final version of ethical issues quiz |
| Week_Four_docker/generate_essays.py | Docker-compatible version of week 4 posts |

### 5.3 MGT_6540_Ethics/ (12 files)
| File | Description |
|------|-------------|
| mla_helpers.py | Shared MLA formatting utility (document creation, paragraphs, Works Cited) |
| CaseStudyOne/generate_essays.py | Four MLA essays on accommodating religious beliefs in ICU |
| CaseStudyTwo/generate_essays.py | Four MLA essays on social media and negative health narratives |
| Week4/CaseStudy3/generate_essays.py | Four MLA essays on conflicting loyalties dilemma |
| Week4/CaseStudy4/generate_essays.py | Four MLA essays analyzing Theranos/Elizabeth Holmes |
| Week4/CaseStudy4/validate_citations.py | Validates MLA citations and Works Cited consistency |
| Week5/CaseStudy5/generate_essays.py | Four MLA essays on CJD surgical exposure disclosure |
| generate_final_essays.py | Final narrative essays on military mental health firearm loophole ethics |
| PresentationV2/generate_essays.py | Four essay variants on military mental health ethics |
| reflectionPaperV1/generate_reflection_doc.py | Reflection paper v1 on architecture of moral character |
| ReflectionsPaperV2/generate_reflection.py | Reflection paper v2 on personal values and ethical frameworks |

### 5.4 essay_engine/ (5 files)
| File | Description |
|------|-------------|
| __init__.py | OOP framework for formatted essay documents (MLA/APA, single/double spacing) |
| formatters.py | Document formatters for MLA and APA citation styles |
| generator.py | Essay generation orchestrator managing queue with formatting and I/O |
| models.py | Data models for essay config (author, course, formatting, citations) |
| runner.py | Docker runner wrapping build/run/copy/cleanup workflow |

### 5.5 scripts/ (1 file)
| File | Description |
|------|-------------|
| configure_gitignore.py | Machine-aware gitignore configuration layering machine-specific rules |

---

## 6. 1099 Form - Tax Automation

**Path:** `D:\Code\1099_Form\python\` | **Files:** ~28
> **Also on F:** `F:\1099_generation\python\`

### PDF Form Filling (6 files)
| File | Description |
|------|-------------|
| fill_irs_k1.py | Fills official IRS Schedule K-1 (Form 1065) for Dimaskus Capital Management |
| fill_irs_1099nec.py | Fills IRS 1099-NEC for Dimaskus LLC payer to Joshua Zayne recipient |
| fill_irs_w2.py | Fills IRS Form W-2 for Dimaskus Capital Management employment (Jan 2015-Aug 2025) |
| fill_irs_1065.py | Fills IRS Form 1065 for Dimaskus Capital Management with placeholder income |
| fill_k1_irs.py | Fills official IRS Schedule K-1 fillable PDF from irs.gov |
| fill_1099nec_irs.py | Fills official IRS 1099-NEC fillable PDF with flexible state support |

### Document Generation (11 files)
| File | Description |
|------|-------------|
| generate_k1.py | K-1 generation via ReportLab (deprecated - draws from scratch) |
| generate_1099.py | 1099-NEC form generation engine (deprecated) |
| generate_k1_dimaskus_llc.py | K-1 for Dimaskus LLC as LP with 18% profit share |
| generate_k1_joshua_zayne.py | K-1 for Joshua Zayne as individual LP with 3% profit share |
| generate_k1_2025.py | K-1 forms for tax year 2025 for both Dimaskus LLC and Joshua Zayne |
| generate_k1_dcm_to_joshua.py | K-1 for Joshua Zayne as 2% LP from DCM (2025 partial year) |
| generate_letters.py | Partnership agreement and offer letters |
| generate_lp_agreement_docx.py | LP Agreement between DCM and Dimaskus LLC (Word) |
| generate_offer_letter_docx.py | Offer letter from DCM to Joshua Zayne for portfolio manager role |
| generate_offer_letter_1099_docx.py | Offer letter as independent contractor with profit sharing |
| generate_offer_letter_redacted_docx.py | Redacted DCM offer letter (financial details blacked out) |

### Letters and Recommendations (3 files)
| File | Description |
|------|-------------|
| generate_recommendation_docx.py | Letter of recommendation for Joshua Zayne (Word) |
| generate_recommendation_v4_pdf.py | Version 4 PDF recommendation letter from High Desert Wagyu |
| generate_hdw_payment_letter_docx.py | Payment confirmation from High Desert Wagyu to Dimaskus LLC |

### Inspection and Debugging (5 files)
| File | Description |
|------|-------------|
| inspect_pdf_fields.py | Lists all fillable form field names in IRS PDF documents |
| inspect_1065_fields.py | Inspects Form 1065 fields with tooltips and mapping info |
| inspect_1065_checkboxes.py | Inspects checkbox widget appearance states in Form 1065 |
| debug_1065_fields.py | Fills each 1065 field with its name for visual debugging |
| debug_k1_fields.py | Fills every K-1 field with its name for visual debugging |

### Validation (3 files)
| File | Description |
|------|-------------|
| validate_forms.py | 50-point IRS form validator checking 1099-NEC and K-1 against specs |
| test_checkbox_1065.py | Tests different checkbox approaches on Form 1065 PDF |
| pdf_font_util.py | Sets font sizes on IRS fillable PDF fields to prevent overflow |

---

## 7. Finance Licenses - Exam Prep

**Path:** `D:\Code\FinanceLicenses\` | **Files:** ~25

### SIE/ (4 files): `__init__.py`, `study_guide.py`, `practice_exam.py`, `flashcards.py`
### Series7/ (9 files): `__init__.py`, `study_guide.py`, `practice_exam.py`, `flashcards.py`, `options_calc.py`, `suitability.py`, `margin_calc.py`, `municipal_bonds.py`, `tax_questions.py`
### Series24/ (4 files): `__init__.py`, `study_guide.py`, `practice_exam.py`, `supervisory_scenarios.py`
### Series63/ (3 files): `__init__.py`, `study_guide.py`, `practice_exam.py`
### Series68/ (4 files): `__init__.py`, `study_guide.py`, `practice_exam.py`, `combined_review.py`

---

## 8. WebScrapper

**Path:** `D:\Code\WebScrapper\` | **Files:** ~11

`__init__.py`, `src/instagram_scraper.py`, `src/web_crawler.py`, `src/html_parser.py`, `src/css_selector.py`, `src/data_exporter.py`, `src/rate_limiter.py`, `src/proxy_manager.py`, `src/utils.py`, `Docker/Dockerfile`, `Docker/docker-compose.yml`

---

## 9. Gmail Privacy Toolkit

**Path:** `D:\Code\gmail-privacy-toolkit\` | **Files:** ~9
> **Also on F:** `F:\gmailAPIManager\`

`__init__.py`, `auth.py`, `label_manager.py`, `privacy_scanner.py`, `redactor.py`, `encryptor.py`, `archive_manager.py`, `bulk_delete.py`, `utils.py`

---

## 10. CryptoMiner

**Path:** `D:\Code\CryptoMiner\` | **Files:** ~8

`__init__.py`, `miners/cpu_miner.py`, `miners/gpu_miner.py`, `pool_manager.py`, `coordinator.py`, `config/settings.py`, `monitor.py`, `utils.py`

---

## 11. Smaller Projects

| Path | Files | Description |
|------|-------|-------------|
| `D:\Code\IphonePhotoCleanse\` | 5 | `__init__.py`, `photo_organizer.py`, `duplicate_finder.py`, `heic_converter.py`, `cleanup.py` |
| `D:\Code\ohjoshrules\` | 3 | `__init__.py`, `device_detector.py`, `memory_sync.py` |
| `D:\Code\YoutubeVideoUpload\` | 4 | `youtube_uploader.py` - bulk YouTube uploader (resumable, crash-recovery); `onedrive_cleanup.py` - delete OneDrive source files after YouTube verification (`--dry-run`/`--verify`/`--delete`/`--status`); `delete_duplicates.py` - remove duplicate YouTube videos; `test_uploader.py` - uploader test harness |
| `D:\Code\CleanUP_C_Drive\` | 1 | `cleanup.py` - C: drive temp/cache cleanup |
| `D:\Code\Motorcycle_Test_Review\` | 2 | `quiz_generator.py`, `study_guide.py` |
| `D:\Code\raspie\` | 2 | `setup.py`, `service_manager.py` |
| `D:\Code\SignatureSnippet\` | 2 | `signature_generator.py`, `embed_signature.py` |

---

## 12. Cross-Drive Reference

### Where the Same Projects Live Across Drives

| Project | C: Drive | D: Drive | F: Drive |
|---------|----------|----------|----------|
| **Brokers Platform** | -- | `D:\Code\Brokers\` | `F:\Brokers\InteractiveBrokers\` |
| **InterActiveBrokers** | -- | `D:\Code\InterActiveBrokers_Project\` | `F:\InterActiveBrokers-Project\` |
| **IronBeam** | -- | `D:\Code\IronBeam\` | `F:\IronBeam_IBKR_likeCode\` |
| **Finance Course** | -- | `D:\Code\Finance\` | `F:\FinanceCode\`, `F:\Efficient_Frontier\`, `F:\CAPM_FAMAFRENCH\` |
| **1099 Tax Forms** | -- | `D:\Code\1099_Form\` | `F:\1099_generation\` |
| **Spring 2026** | -- | `D:\Code\Spring2026\` | `F:\Spring2026\` |
| **Finance Licenses** | -- | `D:\Code\FinanceLicenses\` | -- |
| **Alphainsider** | -- | -- | `F:\Alphainsider\` |
| **ohjoshrules** | `C:\Users\ohjos\ohjoshrules\` | `D:\Code\ohjoshrules\` | `F:\ohjoshrules\` |
| **Gmail Tools** | -- | `D:\Code\gmail-privacy-toolkit\` | `F:\gmailAPIManager\` |
| **Web Scraping** | -- | `D:\Code\WebScrapper\` | `F:\BISLWebScraper20260101\` |
| **YouTube Upload** | -- | `D:\Code\YoutubeVideoUpload\` | `F:\YoutubeVideoUpload\` |
| **Signature Tools** | `C:\Users\ohjos\SignatureSnippet\` | `D:\Code\SignatureSnippet\` | `F:\SignatureSnippet\` |
| **Avoider Game** | `C:\Users\ohjos\PycharmProjects\A7\` | -- | `F:\avoidergame\A7\` |
| **HealthCheck** | `C:\scripts\`, `C:\Users\ohjos\Documents\` | -- | -- |
| **Crypto Mining** | -- | `D:\Code\CryptoMiner\` | -- |
| **BISL Scraper** | -- | -- | `F:\BISLWebScraper20260101\` |
| **Voice/Talk to Claude** | -- | -- | `F:\VoiceToSpeech\`, `F:\TalkToSpeech\` |
| **Canvas Scraper** | -- | -- | `F:\CanvasVideoScrapper\` |
| **STATA** | -- | -- | `F:\STATA\` |
| **Motorcycle Test** | -- | `D:\Code\Motorcycle_Test_Review\` | -- |
| **Raspberry Pi** | -- | `D:\Code\raspie\` | -- |
| **iPhone Photos** | -- | `D:\Code\IphonePhotoCleanse\` | -- |
| **C: Drive Cleanup** | -- | `D:\Code\CleanUP_C_Drive\` | -- |

---

*End of D: Drive Python Code Master Index*
