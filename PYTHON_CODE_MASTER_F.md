# F: Drive - Python Code Master Index

> **Last updated:** 2026-04-20
> **Total Python files:** ~17,749 (many are backups/archives; ~4,000+ unique user-written)
>
> **See also:** [C: Drive Master](C:/Users/ohjos/PYTHON_CODE_MASTER.md) | [D: Drive Master](D:/PYTHON_CODE_MASTER.md)

---

## Table of Contents

**F:-Only Projects (Full Detail)**

1. [Alphainsider](#1-alphainsider)
2. [BISLWebScraper20260101](#2-bislwebscraper20260101)
3. [STATA Integration](#3-stata-integration)
4. [Voice/Speech Interfaces](#4-voicespeech-interfaces)
5. [gmailAPIManager](#5-gmailapimanager)
6. [schwabdeb_copy](#6-schwabdeb_copy)
7. [Lemma](#7-lemma)
8. [FinanceExamMCP](#8-financeexammcp)
9. [Canvas Video Scraper](#9-canvas-video-scraper)
10. [Montana Motorcycle Test Review](#10-montana-motorcycle-test-review)
11. [Resumes](#11-resumes)
12. [RaspberryPIE Claude Install Setup](#12-raspberrypie-claude-install-setup)
13. [YouTube Video Upload](#13-youtube-video-upload)
14. [Avoider Game](#14-avoider-game)
15. [ohjoshrules](#15-ohjoshrules)
16. [SignatureSnippet](#16-signaturesnippet)
17. [Ironbeam (Previous GitHub Repo)](#17-ironbeam-previous-github-repo)
18. [Josh's Stuff](#18-joshs-stuff)

**D: Drive Mirror Projects (Summary Only)**

19. [Brokers / InteractiveBrokers](#19-brokers--interactivebrokers-mirror)
20. [InterActiveBrokers-Project](#20-interactivebrokers-project-mirror)
21. [IronBeam IBKR-like Code](#21-ironbeam-ibkr-like-code-mirror)
22. [FinanceCode](#22-financecode-mirror)
23. [Efficient Frontier](#23-efficient-frontier-mirror)
24. [CAPM / Fama-French](#24-capm--fama-french-mirror)
25. [1099 Tax Form Generation](#25-1099-tax-form-generation-mirror)
26. [Spring 2026 Coursework](#26-spring-2026-coursework-mirror)
27. [Credit Spreading Tool](#27-credit-spreading-tool-mirror)
28. [FI Market Analysis](#28-fi-market-analysis-mirror)
29. [Industry Risk Framework](#29-industry-risk-framework-mirror)
30. [Sales Playbook](#30-sales-playbook-mirror)
31. [ROI Presentation Toolkit](#31-roi-presentation-toolkit-mirror)

**Other**

32. [Archive/Backup Directories](#32-archivebackup-directories)
33. [Cross-Drive Reference](#33-cross-drive-reference)

---

# F:-Only Projects (Full Detail)

---

## 1. Alphainsider

**Path:** `F:\Alphainsider\` | **Files:** ~63 | **F: drive only**

Trading strategy scraper and quantitative analysis framework. Scrapes AlphaInsider strategies, generates standalone Python files with readable trading logic and full quantitative metrics.

### `scraper/`

| File | Description |
|------|-------------|
| `main.py` | Main entry point orchestrating strategy scraping, analysis, and deep analysis with optional scheduling |
| `scraper.py` | Core scraping logic pulling strategies, performance, positions, orders from AlphaInsider API |
| `analyzer.py` | Processes scraped trading strategy data and generates standalone Python files with readable trading logic |
| `deep_analyzer.py` | Computes quantitative financial metrics (Sharpe, Sortino, PnL) and generates comprehensive reports |
| `api_client.py` | REST API wrapper for AlphaInsider with authentication, retries, and rate-limit handling |
| `config.py` | Environment configuration loader for API keys, base URLs, output directories |
| `indicator_rules.py` | Knowledge base of standard trading indicator rules with entry/exit conditions and confluence |
| `tradingview_parser.py` | Extracts TradingView URLs and Pine Script source from strategy descriptions |

### `strategies/` (54 files)

Each file is a scraped trading strategy with embedded quantitative metrics (Total Return, Sharpe Ratio, Sortino Ratio, Max Drawdown, PnL windows, trade activity).

| File | Strategy | Return | Sharpe |
|------|----------|--------|--------|
| `150ma_cross_buyandsell_strategy__d3nv3r__by_d3nv3r.py` | 150-period MA crossover | 38.64% | 0.987 |
| `2_moving_averages___trend_following_by_sosacur01.py` | 2 MA trend following | -9.62% | 0.050 |
| `bias_ratio_eth_3h__cttc5108_by_cttc5108.py` | Bias Ratio ETH 3H | 12.12% | 0.479 |
| `bitcoin_bear_season.py` | Bitcoin bear market seasonal | 58.98% | 2.261 |
| `bitcoin_futures_vs__spot_tri_frame___strategy__presenttrading__by_presenttrading.py` | BTC futures vs spot tri-frame | 33.34% | 1.116 |
| `btc_and_eth_long_strategy___version_1_by_philipina.py` | Long-only BTC+ETH | 545.42% | 0.923 |
| `btc_hashrate_ribbons_by_powerscooter.py` | BTC hashrate ribbons | -11.95% | -0.009 |
| `elliott_s_quadratic_momentum___strategy__presenttrading__by_presenttrading.py` | Elliott's quadratic momentum | -23.65% | -0.185 |
| `ema_backtester_by_somsbenikeenkat.py` | EMA backtester | 0.75% | 0.170 |
| `ema_candle_close_strategy_by_gentleman_goat.py` | EMA candle close | 13.14% | 0.458 |
| `ema_cross_strat___turtle_trading____strategy_by_mkonsap.py` | EMA cross / turtle trading | 119.56% | 0.448 |
| `evwma_vwap_cross_strategy__quantnomad__by_quantnomad.py` | EVWMA VWAP crossover | 97.99% | 1.284 |
| `fikira__fibma_fibema_strategy_by_fikira.py` | FibMA/FibEMA | 11.67% | 0.417 |
| `fine_tune_inputs__fourier_smoothed_hybrid_volume_spread_analysis_by_automatedtradingalgorithms.py` | Fourier smoothed hybrid VSA | -47.67% | -0.590 |
| `flexima_x_flexist___strategy__presenttrading__by_presenttrading.py` | FlexiMA x FlexiST | -12.76% | 0.005 |
| `harshtrades.py` | Harshtrades strategy | 19.09% | 0.522 |
| `hiubris_trend_strategy_2.py` | Hiubris trend v2 | -95.44% | -3.836 |
| `ichimoku_kinko_hyo__eth_3h_strategy_by_tobuno_by_tobuno.py` | Ichimoku ETH 3H | 716.41% | 0.862 |
| `keltner_channel__linkusdt__1h___strategy_by_kh_thetrader.py` | Keltner channel LINK/USDT 1H | 58.23% | 0.325 |
| `lunaowl__support_resistance_strategy_v4__eth__by_lunaowl.py` | Support/resistance ETH v4 | 256.25% | 0.847 |
| `ma_cross___strategy_by_hnipps.py` | MA cross | 126.45% | 0.514 |
| `moving_average_ema_sma_cross_strategy_by_criptonomics.py` | EMA/SMA cross | 58.97% | 0.345 |
| `multi_step_flexima___strategy__presenttrading__by_presenttrading.py` | Multi-step FlexiMA | 61.50% | 1.187 |
| `multi_tf_ai_supertrend_with_adx___strategy__presenttrading__by_presenttrading.py` | Multi-TF AI SuperTrend + ADX | -43.72% | -0.699 |
| `multi_time_frame_buy_the_dips__by_coinrule____strategy_by_coinrule.py` | Multi-TF buy-the-dips | -30.58% | 0.007 |
| `noro_s_ma_atr_strategy_by_noro.py` | Noro's MA+ATR | 289.21% | 0.653 |
| `noro_s_trendma_strategy_by_robo_trading.py` | Noro's TrendMA | 161.50% | 1.742 |
| `presenttrend_rmi_synergy___strategy__presenttrading__by_presenttrading.py` | PresentTrend RMI synergy | -44.05% | -0.610 |
| `profit_maximizer_strategy_by_softkill21.py` | Profit maximizer | 786.45% | 0.986 |
| `qqe_cross_v6_0_by_justunclel_long_short_by_sscogin_backtest___strategy_by_sscogin.py` | QQE Cross v6.0 long/short | 247.18% | 0.696 |
| `quantnomad___heikin_ashi_psar_strategy_by_quantnomad.py` | Heikin-Ashi PSAR | -71.08% | -0.183 |
| `quantnomad___significant_pivot_reversal_strategy_by_quantnomad.py` | Significant pivot reversal | -22.93% | -0.013 |
| `rate_of_change_strategy_by_genez_fi.py` | Rate of change | 30.15% | 0.704 |
| `ricky_parker_s_formula_by_rickyparker.py` | Ricky Parker's formula | 22.08% | 0.651 |
| `rmi_trend_sync___strategy__presenttrading__by_presenttrading.py` | RMI trend sync | 1.98% | 0.250 |
| `rsi_and_smoothed_rsi_bull_div_strategy__bigbitsio__by_bigbitsio.py` | RSI + smoothed RSI bull div | -80.60% | -1.178 |
| `script_algo___fibo_correction_strategy_by_script_algo.py` | Fibonacci correction | 1.13% | 0.455 |
| `simple_rsi_strategy_bitcoin___bitduke.py` | Simple RSI Bitcoin | 103.58% | 0.474 |
| `simple_rsi_strategy_buy_sell_at_a_certain_level___by_bitduke.py` | RSI buy/sell at level | 54.26% | 0.395 |
| `simple_rsi_strategy_buy_sell_at_a_certain_level_w__short_by_bitduke.py` | RSI buy/sell with short | -32.67% | 0.286 |
| `strategic_multi_step_supertrend___strategy__presenttrading__by_presenttrading.py` | Strategic multi-step SuperTrend | -38.23% | -0.449 |
| `strategy_tester_ema_sma_rsi_macd_by_fikira.py` | EMA/SMA/RSI/MACD tester | -25.67% | 0.194 |
| `supertrend_cloud_strategy_by_jhanson107.py` | SuperTrend cloud | 83.19% | 0.597 |
| `support_resistance_breakout_by_pmk07.py` | Support/resistance breakout | -13.48% | 0.193 |
| `sw_sve___stochastic_vol_emas__sergio_waldoke____strategy_by_galileogalilei1.py` | Stochastic + Vol + EMAs | -41.60% | -0.223 |
| `swing_trade___strategy_by_vinay182.py` | Swing trade | -5.48% | -0.347 |
| `tilson_t3_and_mavilimw_triple_combined_strategy_by_bartua.py` | Tilson T3 + MavilimW triple | -12.20% | 0.086 |
| `trend_deviation_strategy__ikkeomar__by_ikkeomar.py` | Trend deviation detection | 155.81% | 1.651 |
| `trend_switch_by_palitoj_endthen.py` | Trend switch | 68.98% | 0.926 |
| `tsi_w_supertrend_decision___strategy__presenttrading__by_presenttrading.py` | TSI + SuperTrend decision | -15.78% | -0.034 |
| `turtle_trader_strategy_by_gsanson66.py` | Turtle trader | -7.99% | 0.073 |
| `volatility_system_by_wilder__lucf____strategy_by_lucf.py` | Wilder volatility system | 84.82% | 0.376 |
| `wilder_s_moving_average_strategy_by_dongyun.py` | Wilder's moving average | 32.11% | 0.239 |
| `wmx_williams_fractals_strategy_v4_by_wmx_q_system_trading.py` | Williams fractals v4 | 865.96% | 1.096 |

**Top 5 by Return:** WMX Williams Fractals (865.96%), Profit Maximizer (786.45%), Ichimoku ETH 3H (716.41%), BTC+ETH Long (545.42%), Noro's MA+ATR (289.21%)

**Top 5 by Sharpe:** Bitcoin Bear Season (2.261), Noro's TrendMA (1.742), Trend Deviation (1.651), EVWMA VWAP Cross (1.284), Multi-Step FlexiMA (1.187)

### Other files

| File | Description |
|------|-------------|
| `strategies/_index.json` | Strategy index with file paths and generation metadata (50 strategies, generated 2026-02-12) |

---

## 2. BISLWebScraper20260101

**Path:** `F:\BISLWebScraper20260101\` | **Files:** ~11 | **F: drive only**

VA BISL Weekly Performance Report Generator. Scrapes three Power BI dashboards (TMS, Audit, Scheduling Accuracy) using Selenium/Chrome.

| File | Description |
|------|-------------|
| `main.py` | Main orchestrator running three VA BISL Power BI scrapers and generating weekly performance reports |
| `src/scrapers/base_scraper.py` | Base class providing common Selenium/Chrome functionality for Power BI reports |
| `src/scrapers/audit_scraper.py` | Scrapes VA BISL SAT Audit Dashboard for scheduling accuracy and compliance |
| `src/scrapers/scheduling_accuracy_scraper.py` | Extracts scheduling accuracy percentages by service group |
| `src/scrapers/tms_scraper.py` | Scrapes TMS completion percentages from Power BI Training Management System |
| `src/scrapers/__init__.py` | Scrapers package init |
| `src/utils/logger.py` | Centralized logging with timestamps and status prefixes |
| `src/utils/__init__.py` | Utils package init |
| `src/__init__.py` | Source package init |
| `InstStandAlone/EmailCode.py` | Single-file project generator creating entire scraping system as one embeddable script |
| `InstStandAlone/StepOneDocker.py` | Docker environment setup for secure isolated scraping |

---

## 3. STATA Integration

**Path:** `F:\STATA\` | **Files:** ~16 Python files | **F: drive only**

Python-STATA bridge library. Provides programmatic access to Stata from Python via the Stata Function Interface (SFI) and pystata utilities, including Jupyter/IPython magic commands.

### `ado/base/py/`

| File | Description |
|------|-------------|
| `sfi.py` | Stata Function Interface binding providing access to Stata's data, matrices, scalars, macros, characteristics, and value labels |
| `stoutput.py` | Stata output handling for interactive Python/Stata sessions |

### `utilities/pystata/`

| File | Description |
|------|-------------|
| `stata.py` | Core interface for executing Stata commands from Python with queue-based execution |
| `config.py` | System configuration for finding Stata installation paths and edition settings |
| `stexception.py` | Custom exception classes for IPython/pystata integration |
| `version.py` | Version metadata (0.1.1) |
| `__init__.py` | Pystata package init |

### `utilities/pystata/core/`

| File | Description |
|------|-------------|
| `numpy2mata.py` | NumPy array to Stata matrix (mata) conversion |
| `numpy2stata.py` | NumPy array to Stata variable conversion |
| `pandas2stata.py` | Pandas DataFrame to Stata variable conversion |
| `stout.py` | Stata output stream management |
| `__init__.py` | Core package init |

### `utilities/pystata/ipython/`

| File | Description |
|------|-------------|
| `stpymagic.py` | IPython magic commands (`%%stata`, `%%mata`, `%%python`) for running Stata in Jupyter notebooks |
| `grdisplay.py` | IPython display for Stata graphs as SVG/PNG/PDF in Jupyter cells |
| `ipy_utils.py` | IPython cache directory discovery and utility functions |
| `__init__.py` | IPython integration package init |

---

## 4. Voice/Speech Interfaces

**F: drive only**

### VoiceToSpeech

**Path:** `F:\VoiceToSpeech\`

| File | Description |
|------|-------------|
| `talk_to_claude.py` | Voice-powered finance exam assistant with push-to-talk and 7-method consensus verification. Uses Google Speech Recognition for input and TTS for Claude's responses |

### TalkToSpeech

**Path:** `F:\TalkToSpeech\`

| File | Description |
|------|-------------|
| `talk_to_claude.py` | Voice-to-speech interface using Google Speech Recognition and TTS for exam solving. Alternate implementation with logging and batch mode |

---

## 5. gmailAPIManager

**Path:** `F:\gmailAPIManager\` | **Files:** ~9 | **F: drive only**

Gmail privacy audit toolkit with MCP server integration for Claude Code.

| File | Description |
|------|-------------|
| `auth.py` | OAuth2 authentication for Gmail API with credential management and token refresh |
| `cli.py` | CLI for Gmail privacy auditing with audit, headers, trackers, and metadata stripping commands |
| `config.py` | Configuration including credentials paths and tracking domain lists |
| `mcp_server.py` | MCP server exposing Gmail privacy audit tools to Claude Code |
| `utils/account.py` | Gmail account audit for forwarding, auto-forwarding, and filter settings |
| `utils/headers.py` | Email header analysis for privacy-relevant sender info extraction |
| `utils/metadata.py` | File metadata stripping utilities |
| `utils/tracking.py` | Tracking pixel and link tracker detection via pattern matching |
| `utils/__init__.py` | Utils package init |

---

## 6. schwabdeb_copy

**Path:** `F:\schwabdeb_copy\` | **Files:** ~27 | **F: drive only**

Schwab API client library (schwabdev) with comprehensive examples, documentation compiler, and test suite.

### `schwabdev/`

| File | Description |
|------|-------------|
| `client.py` | Main Schwab API client for sync/async HTTP requests with authentication |
| `stream.py` | WebSocket streaming client for real-time market data |
| `tokens.py` | OAuth token management with encryption and automatic refresh |
| `enums.py` | TimeFormat enumeration |
| `translate.py` | Stream field ID to human-readable name mappings |
| `__init__.py` | Package init |

### `docs/`

| File | Description |
|------|-------------|
| `compile-docs.py` | Markdown-to-HTML converter with syntax highlighting for API documentation |

### `docs/examples/`

| File | Description |
|------|-------------|
| `api_demo.py` | Basic Schwab API call demo with authentication flow |
| `async_api_calls.py` | Concurrent async API calls for multiple tickers |
| `stream_demo.py` | Basic streaming market data example |
| `playground.py` | Interactive REPL for Schwab API testing |

### `docs/examples/extra/`

| File | Description |
|------|-------------|
| `api_gui_demo.py` | Tkinter GUI for Schwab API interaction |
| `async_api_demo_parsed.py` | Async demo with parsed JSON responses |
| `async_playground.py` | Async interactive REPL for Schwab API |
| `async_stream_demo.py` | Async streaming market data example |
| `capture_callback.py` | OAuth callback capture server for token acquisition |
| `charting.py` | Real-time matplotlib charting of streaming data |
| `concurrent_stream_calls.py` | Multiple concurrent WebSocket stream connections |
| `encrypted_db_setup.py` | Encrypted SQLite for secure token storage |
| `processing_streaming_data.py` | Stream data processing pipeline |
| `template.py` | Schwab API starter template |
| `translating_stream.py` | Stream field number-to-name translation demo |

### `tests/`

| File | Description |
|------|-------------|
| `conftest.py` | Pytest fixtures for Schwab API tests |
| `test_client.py` | Tests for ClientBase HTTP methods |
| `test_stream.py` | Tests for StreamBase WebSocket functionality |
| `test_tokens.py` | Tests for Tokens OAuth flow |
| `__init__.py` | Tests package init |

---

## 7. Lemma

**Path:** `F:\Lemma\` | **Files:** 6 Python files | **F: drive only**

Finance course materials (Obsidian vault) and coursework generators.

### `Finance/Efficient_Frontier/Efficient_Frontier 2/`

| File | Description |
|------|-------------|
| `data_loader.py` | Portfolio optimization data loader for stock return data |
| `main.py` | Main portfolio optimization runner with Modern Portfolio Theory (Markowitz) |
| `plotting.py` | Efficient frontier visualization with MVP, tangent portfolio, and two-fund separation |
| `portfolio_optimizer.py` | MPT optimizer computing minimum variance and tangent portfolios |

### `Spring2026/BMI/`

| File | Description |
|------|-------------|
| `generate_leadership_essays.py` | APA-formatted essay generator for leadership assessment assignments |
| `leadership_self_assessment.py` | Purdue Global leadership self-assessment tool with scoring |

---

## 8. FinanceExamMCP

**Path:** `F:\FinanceExamMCP\` | **Files:** 2 | **F: drive only**

MCP (Model Context Protocol) server for finance exam support in Claude Desktop.

| File | Description |
|------|-------------|
| `server.py` | Finance exam MCP server with Excel reading and 7-method consensus solving |
| `setup.py` | Setup script installing dependencies and registering MCP server with Claude Desktop |

---

## 9. Canvas Video Scraper

**Path:** `F:\CanvasVideoScrapper\` | **Files:** 1 | **F: drive only**

| File | Description |
|------|-------------|
| `canvas_transcript.py` | Canvas/Instructure video transcript scraper extracting Kaltura captions to markdown notes |

---

## 10. Montana Motorcycle Test Review

**Path:** `F:\Montana_Motorcycle_Test_Review\` | **Files:** 1 | **F: drive only**

| File | Description |
|------|-------------|
| `generate_flashcards.py` | Montana motorcycle test flashcard generator producing PDF, PPTX, HTML, and CSV formats |

---

## 11. Resumes

**Path:** `F:\resumes\_src\` | **Files:** 5 | **F: drive only**

Resume generation pipeline with Docker support. Generates targeted resumes for BlackRock, Morgan Stanley, SGI, State Street, URS, and Vanguard.

| File | Description |
|------|-------------|
| `main.py` | Main resume generation runner with 2-page dense layout |
| `resume_generator.py` | Core resume generator using python-docx with Arial font |
| `resume_generator 2.py` | v1.4+ with tight margins and gray separators |
| `resume_generator 3.py` | v1.4.3 with Key Projects formatting |
| `20260201_v1.py` | Resume generator version 1.0 |

---

## 12. RaspberryPIE Claude Install Setup

**Path:** `F:\RaspberryPIE_Claude_Install_setup\` | **Files:** 2 | **F: drive only**

| File | Description |
|------|-------------|
| `run.py` | Raspberry Pi Claude Code installer - runs the full setup sequence |
| `setup_raspberry_pi.py` | Automated Pi setup (Docker, Node.js, Claude CLI) with dependency checking |

---

## 13. YouTube Video Upload

**Path:** `F:\YoutubeVideoUpload\` | **Files:** 1 | **F: drive only**

| File | Description |
|------|-------------|
| `youtube_uploader.py` | Bulk YouTube uploader with resumable uploads, crash detection, and auto-retry |

---

## 14. Avoider Game

**Path:** `F:\avoidergame\A7\` | **Files:** 1 | **F: drive only**

| File | Description |
|------|-------------|
| `AvoiderGame.py` | Pygame-based avoidance game |

---

## 15. ohjoshrules

**Path:** `F:\ohjoshrules\` | **Files:** 1 Python file | **Present on all drives**

| File | Description |
|------|-------------|
| `sync_memory.py` | Cross-device Claude Code memory sync (desktop, laptop, Raspberry Pi) |

---

## 16. SignatureSnippet

**Path:** `F:\SignatureSnippet\` | **Files:** 2 | **F: drive only**

| File | Description |
|------|-------------|
| `extract_signature.py` | Extracts handwritten signature from scanned images |
| `generate_blue_signature.py` | Generates blue-ink styled signature image from extracted signature |

---

## 17. Ironbeam (Previous GitHub Repo)

**Path:** `F:\Ironbeam_github_previous_repo\` | **Files:** ~20 | **F: drive only**

Earlier iteration of the IronBeam futures trading client as a structured Python package.

### `src/ironbeam/`

| File | Description |
|------|-------------|
| `base.py` | Base client class with HTTP session management |
| `exceptions.py` | Custom exception classes for API errors |
| `literals.py` | Type literal definitions |
| `__init__.py` | Package init |

### `src/ironbeam/auth/`

| File | Description |
|------|-------------|
| `base.py` | Authentication handler for IronBeam API |
| `__init__.py` | Auth package init |

### `src/ironbeam/info/`

| File | Description |
|------|-------------|
| `base.py` | Account and instrument info retrieval |
| `models.py` | Data models for account/instrument info |
| `__init__.py` | Info package init |

### `src/ironbeam/market/`

| File | Description |
|------|-------------|
| `base.py` | Market data retrieval (quotes, history) |
| `models.py` | Data models for market data |
| `__init__.py` | Market package init |

### `examples/`

| File | Description |
|------|-------------|
| `authentication.py` | Authentication example |
| `info.py` | Account info retrieval example |
| `market.py` | Market data retrieval example |

### `tests/`

| File | Description |
|------|-------------|
| `conftest.py` | Pytest fixtures |
| `test_auth.py` | Authentication tests |
| `test_base.py` | Base client tests |
| `test_info.py` | Info endpoint tests |
| `test_market.py` | Market endpoint tests |

---

## 18. Josh's Stuff

**Path:** `F:\Josh's Stuff\` | **Primarily personal documents; few Python files**

| File | Description |
|------|-------------|
| `Coding Folder/TD_Ameritrade_quotes.py` | Fetches stock quotes from TD Ameritrade API |
| `Coding Folder/openai/openai_1.py` | OpenAI API usage example (v1) |
| `Coding Folder/openai/openai_2.py` | OpenAI API usage example (v2) |
| `Josh's stuff sub folder/Environments/hw one numerical analysis/hw_one_num_an.py` | Numerical analysis homework |
| `Josh's stuff sub folder/Environments/Numerical analysis/Numerical_analysis_I.py` | Numerical analysis coursework |
| `Josh's stuff sub folder/Environments/stock_test.py` | Stock testing script |
| `Josh's stuff sub folder/Environments/TD_Ameritrade_quotes/TD_Ameritrade_quotes.py` | TD Ameritrade quotes (older copy) |
| `Josh's stuff sub folder/Environments/URA stock price/URA_stock_price.py` | URA ETF price tracker |

---

# D: Drive Mirror Projects (Summary Only)

> These projects are mirrors of D: drive originals. Files are identical.
> **See `D:\PYTHON_CODE_MASTER.md` for complete file-by-file detail.**

---

## 19. Brokers / InteractiveBrokers (Mirror)

**Path:** `F:\Brokers\InteractiveBrokers\` | **Files:** ~1,635
**Primary:** `D:\Code\Brokers\`

Comprehensive multi-broker trading platform integration with Interactive Brokers. Includes core trading engine, accounting/P&L, contract management, multi-asset data fetching (stocks, bonds, forex, futures, indices), order management, portfolio/risk management, 10+ strategies (MA Crossover, ATR Breakout, Keltner, Trend Following, Credit Spread, Forex, IV, Event-Driven, Commodity), visualization, and maintenance scripts.

**Subfolders:** `src/core/`, `src/accounting/`, `src/contracts/`, `src/data/`, `src/getTimeFrameData/`, `src/orders/`, `src/portfolioMGT/`, `src/strategies/`, `src/utils/`, `src/visualization/`, `scripts/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 20. InterActiveBrokers-Project (Mirror)

**Path:** `F:\InterActiveBrokers-Project\` | **Files:** ~710
**Primary:** `D:\Code\InterActiveBrokers_Project\`

IBKR data downloader with code quality agents (AST cleanup, docstring generation, type hints, test review, performance audit), data pipeline, and comprehensive test suite.

**Subfolders:** `agents/`, `src/`, `tests/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 21. IronBeam IBKR-like Code (Mirror)

**Path:** `F:\IronBeam_IBKR_likeCode\` | **Files:** ~239
**Primary:** `D:\Code\IronBeam\`

Futures/commodities trading platform with real-time WebSocket streaming, InfluxDB storage, and demo/live execution modes.

**Subfolders:** `src/`, `tests/`, `scripts/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 22. FinanceCode (Mirror)

**Path:** `F:\FinanceCode\` | **Files:** ~298
**Primary:** `D:\Code\Finance\`

Top-level runner for all Finance course projects including CAPM, Efficient Frontier, Bond Analysis, credit spreading, FI market analysis, industry risk, sales playbook, and ROI toolkit.

**Key files:** `run_all.py`, `scan.py`, `device_paths.py`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 23. Efficient Frontier (Mirror)

**Path:** `F:\Efficient_Frontier\` | **Files:** ~38
**Primary:** `D:\Code\Finance\Efficient_Frontier\`

Portfolio optimization and Markowitz efficient frontier analysis with CLI and interactive modes.

**Key files:** `run_cli.py`, `run_interactive.py`, `create_formula_workbook.py`, `process_input_data.py`, `setup.py`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 24. CAPM / Fama-French (Mirror)

**Path:** `F:\CAPM_FAMAFRENCH\` | **Files:** ~38
**Primary:** `D:\Code\Finance\CAPM_French\`

Capital Asset Pricing Model with Fama-French 3-Factor regression analysis, batch CLI, and interactive interface.

**Key files:** `run_cli.py`, `run_interactive.py`, `setup.py`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 25. 1099 Tax Form Generation (Mirror)

**Path:** `F:\1099_generation\` | **Files:** ~27
**Primary:** `D:\Code\1099_Form\`

IRS form automation: fills official PDFs (1099-NEC, K-1, W-2, 1065), generates Word documents (LP agreements, offer letters, recommendations), and includes validation and debugging tools.

**Subfolders:** `python/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 26. Spring 2026 Coursework (Mirror)

**Path:** `F:\Spring2026\` | **Files:** ~19
**Primary:** `D:\Code\Spring2026\`

Spring 2026 semester coursework including essay engine (MLA, APA, discussion formats) and BMI Intro to Leadership assignment generators.

**Subfolders:** `essay_engine/`, `BMI_Intro_to_Leadership/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 27. Credit Spreading Tool (Mirror)

**Path:** `F:\credit-spreading-tool\` | **Files:** ~11
**Primary:** `D:\Code\Finance\credit-spreading-tool\`

DSCR calculator, leverage ratios, UCA cashflow analysis with Excel export.

**Subfolders:** `src/analysis/`, `src/data/`, `src/export/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 28. FI Market Analysis (Mirror)

**Path:** `F:\fi-market-analysis\` | **Files:** ~14
**Primary:** `D:\Code\Finance\fi-market-analysis\`

Competitive analysis, scoring, market segmentation, account prioritization, and chart visualization for financial institution markets.

**Subfolders:** `src/analysis/`, `src/data/`, `src/targeting/`, `src/visualization/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 29. Industry Risk Framework (Mirror)

**Path:** `F:\industry-risk-framework\` | **Files:** ~11
**Primary:** `D:\Code\Finance\industry-risk-framework\`

Industry benchmarking, classification, metrics calculation with Excel export.

**Subfolders:** `src/analysis/`, `src/data/`, `src/export/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 30. Sales Playbook (Mirror)

**Path:** `F:\sales-playbook\` | **Files:** ~12
**Primary:** `D:\Code\Finance\sales-playbook\`

Enterprise SaaS sales methodology: discovery questions, qualification, objection handling, ROI calculations.

**Subfolders:** `src/discovery/`, `src/objections/`, `src/roi/`, `src/export/`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

## 31. ROI Presentation Toolkit (Mirror)

**Path:** `F:\roi-presentation-toolkit\` | **Files:** ~15
**Primary:** `D:\Code\Finance\roi-presentation-toolkit\`

Dynamic ROI presentation project generator.

**Key file:** `generate_project.py`

> See `D:\PYTHON_CODE_MASTER.md` for complete file-level detail.

---

# Other

---

## 32. Archive/Backup Directories

These directories contain large numbers of Python files but are archives, backups, or package installations. No file-level detail provided.

| Path | Files | Description |
|------|-------|-------------|
| `F:\NVME BACKUP\` | ~6,727 | Old system backup. Contains duplicates of many projects above |
| `F:\Main computer programs\` | ~5,486 | Anaconda/Miniconda installs and system package directories |
| `F:\iCloudDrive\` | ~1,191 | Synced iCloud mixed content (documents, photos, misc) |

---

## 33. Cross-Drive Reference

### Where the Same Projects Live Across Drives

| Project | C: Drive | D: Drive | F: Drive |
|---------|----------|----------|----------|
| **Brokers Platform** | -- | `D:\Code\Brokers\` | `F:\Brokers\InteractiveBrokers\` |
| **InterActiveBrokers** | -- | `D:\Code\InterActiveBrokers_Project\` | `F:\InterActiveBrokers-Project\` |
| **IronBeam** | -- | `D:\Code\IronBeam\` | `F:\IronBeam_IBKR_likeCode\` |
| **IronBeam (prev repo)** | -- | -- | `F:\Ironbeam_github_previous_repo\` |
| **Finance Course** | -- | `D:\Code\Finance\` | `F:\FinanceCode\` |
| **Efficient Frontier** | -- | `D:\Code\Finance\Efficient_Frontier\` | `F:\Efficient_Frontier\` |
| **CAPM / Fama-French** | -- | `D:\Code\Finance\CAPM_French\` | `F:\CAPM_FAMAFRENCH\` |
| **Credit Spreading Tool** | -- | `D:\Code\Finance\credit-spreading-tool\` | `F:\credit-spreading-tool\` |
| **FI Market Analysis** | -- | `D:\Code\Finance\fi-market-analysis\` | `F:\fi-market-analysis\` |
| **Industry Risk Framework** | -- | `D:\Code\Finance\industry-risk-framework\` | `F:\industry-risk-framework\` |
| **Sales Playbook** | -- | `D:\Code\Finance\sales-playbook\` | `F:\sales-playbook\` |
| **ROI Presentation** | -- | `D:\Code\Finance\roi-presentation-toolkit\` | `F:\roi-presentation-toolkit\` |
| **1099 Tax Forms** | -- | `D:\Code\1099_Form\` | `F:\1099_generation\` |
| **Spring 2026** | -- | `D:\Code\Spring2026\` | `F:\Spring2026\` |
| **Alphainsider** | -- | -- | `F:\Alphainsider\` |
| **BISL Scraper** | -- | -- | `F:\BISLWebScraper20260101\` |
| **STATA** | -- | -- | `F:\STATA\` |
| **Voice/Talk to Claude** | -- | -- | `F:\VoiceToSpeech\`, `F:\TalkToSpeech\` |
| **FinanceExamMCP** | -- | -- | `F:\FinanceExamMCP\` |
| **Canvas Scraper** | -- | -- | `F:\CanvasVideoScrapper\` |
| **Schwab Dev (copy)** | -- | -- | `F:\schwabdeb_copy\` |
| **Lemma** | -- | -- | `F:\Lemma\` |
| **Resumes** | -- | -- | `F:\resumes\` |
| **Motorcycle Test** | -- | -- | `F:\Montana_Motorcycle_Test_Review\` |
| **ohjoshrules** | `C:\Users\ohjos\ohjoshrules\` | `D:\Code\ohjoshrules\` | `F:\ohjoshrules\` |
| **Gmail Tools** | -- | `D:\Code\gmail-privacy-toolkit\` | `F:\gmailAPIManager\` |
| **Web Scraping** | -- | `D:\Code\WebScrapper\` | `F:\BISLWebScraper20260101\` |
| **YouTube Upload** | -- | `D:\Code\YoutubeVideoUpload\` | `F:\YoutubeVideoUpload\` |
| **Raspberry Pi Setup** | -- | -- | `F:\RaspberryPIE_Claude_Install_setup\` |
| **Signature Tools** | `C:\Users\ohjos\SignatureSnippet\` | -- | `F:\SignatureSnippet\` |
| **Avoider Game** | `C:\Users\ohjos\PycharmProjects\A7\` | -- | `F:\avoidergame\A7\` |
| **HealthCheck** | `C:\scripts\`, `C:\Users\ohjos\Documents\` | -- | -- |
| **Crypto Mining** | -- | `D:\Code\CryptoMiner\` | -- |
| **Finance Licenses** | -- | `D:\Code\FinanceLicenses\` | -- |

### Drive Summary

| Drive | Total .py Files | Unique User-Written | Primary Role |
|-------|----------------|---------------------|--------------|
| **C:** | ~700 | ~50 | System scripts, health checks, small projects |
| **D:** | ~3,400 | ~2,800 | Primary development (all active trading/finance projects) |
| **F:** | ~17,749 | ~4,000+ | Mirrors + F:-only projects + archives |
