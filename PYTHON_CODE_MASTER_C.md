# C: Drive - Python Code Master Index

> **Last updated:** 2026-04-22
> **Total Python files:** ~31 (user-written, excluding libraries/venvs)
>
> **See also:** [D: Drive Master](D:/PYTHON_CODE_MASTER.md) | [F: Drive Master](F:/PYTHON_CODE_MASTER.md)

---

## Table of Contents

1. [System Administration & Security](#1-system-administration--security)
2. [Signature Analysis & Image Processing](#2-signature-analysis--image-processing)
3. [Off-Grid Research](#3-off-grid-research)
4. [Cross-Device DevOps Tools](#4-cross-device-devops-tools)
5. [University Coursework (Archive)](#5-university-coursework-archive)
6. [Cross-Drive Reference](#cross-drive-reference)

---

## 1. System Administration & Security

### `C:\scripts\`

| File | Description |
|------|-------------|
| `HealthCheck_V24.py` | **Advanced** Windows security & system audit (v21.4+). Malware scanning via registry, process enumeration, root drive scanning, Defender integration, temp folder cleanup. Uses `ctypes` for admin checks and `winreg` for registry access. |

### `C:\Users\ohjos\Documents\`

| File | Description |
|------|-------------|
| `HealthCheck.py` | Simpler 5-step security audit: registry malware scan (HKCU/HKLM), process enumeration (flags Temp folder processes), C: root scan, Defender Quick Scan trigger, temp cleanup. |

### `C:\Users\ohjos\OneDrive\Documents\`

| File | Description |
|------|-------------|
| `HealthCheck.py` | OneDrive-synced copy of the Documents version. |

---

## 2. Signature Analysis & Image Processing

### `C:\Users\ohjos\` (user root)

| File | Description |
|------|-------------|
| `analyze_signature.py` | PIL + NumPy analysis of signature layout. Identifies ink boundaries, row/column density distributions, vertical split detection. |
| `analyze_signature2.py` | Extended analysis splitting ink into thirds (upper/middle/lower) and column density for first name, middle initial, last name. |
| `extract_signature.py` | Removes unwanted ink strokes from signature images via RGB channel analysis, brightness/chroma filtering. |
| `test_crops.py` | Extracts and saves test crop regions to verify component boundaries before rearranging. |
| `test_crops2.py` | More targeted signature crops with refined column/row boundaries for initial/last name splits. |
| `test_fonts.py` | Tests Windows cursive fonts (SCRIPTBL, FRSCRIPT, Segoe, Lucida, Palace) against signature for best match. |

### `C:\Users\ohjos\SignatureSnippet\`

| File | Description |
|------|-------------|
| `extract_signature.py` | Duplicate of the root folder signature extraction script. |

---

## 3. Off-Grid Research

### `C:\Users\ohjos\Desktop\offgrid_research\`

| File | Description |
|------|-------------|
| `research.py` | Off-grid power system research script (runs in Docker for isolation). Uses `duckduckgo_search` to scrape pricing/specs for solar panels, batteries, inverters. Outputs to JSON. |

---

## 4. Cross-Device DevOps Tools

### `C:\Users\ohjos\ohjoshrules\machine_ignore\`

| File | Description |
|------|-------------|
| `detect.py` | Machine/device detection (desktop/laptop/Raspberry Pi) via hostname matching against `device_registry.json`, with OS and drive signature fallback. |
| `apply.py` | Applies per-machine gitignore rules to git repos. Merges common + machine-specific + repo-specific rules into `.git/info/exclude`. |

### `C:\Users\ohjos\ohjoshrules\`

| File | Description |
|------|-------------|
| `sync_memory.py` | Cross-device Claude Code memory sync. Pulls/pushes memory between GitHub and local Claude memory. Supports `--pull`, `--push`, `--sync`, `--status`, `--dry-run`. |

---

## 5. University Coursework (Archive)

### `C:\Users\ohjos\2023-datascience-lectures\02-basic-python\`

| File | Description |
|------|-------------|
| `exercise.py` | Practice exercise: function scope with `add_numbers()`. |
| `first_steps.py` | Lecture material on basic Python concepts. |

### `C:\Users\ohjos\2023-datascience-lectures\14-web-scraping-and-apis\`

| File | Description |
|------|-------------|
| `credentials.py` | Empty API credential template (no secrets). |

### `C:\Users\ohjos\2024-datascience-lectures\02-basic-python\`

| File | Description |
|------|-------------|
| `exercise.py` | 2024 version of basic Python exercise. |
| `first_steps.py` | 2024 lecture material on basic Python concepts. |

### `C:\Users\ohjos\PycharmProjects\`

| Folder | File | Description |
|--------|------|-------------|
| `A4\` | `A4PartA.py` | Assignment: list printing, multiply function, conditionals. |
| `A4\` | `A4PartB.py` | Second part of Assignment A4. |
| `A4\` | `graphics.py` | Graphics library for assignment. |
| `A5\` | `PythonExamplesThree.py` | Assignment A5 examples. |
| `A6\` | `NovelAnalysis.py` | Text analysis: word frequency, stop words, chunking, pattern analysis. |
| `A7\` | `AvoiderGame.py` | Pygame game: sprite loading, collision detection, player interaction. |
| `URA\` | `URA_STOCK_PRICE.py` | Web scrapes real-time URA (uranium ETF) price from Yahoo Finance. |
| `Giraffe\` | `App.py` | Minimal/empty starter file. |
| `Practicaltest\` | `Practical.py` | Practical exam: dictionary problems, inventory system. |
| `Practicaltest\` | `testcode.py` | Additional test code. |
| `untitled\` | `App.py` | Generic project file. |
| `untitled\` | `Practice.py` | Generic project file. |
| `untitled\` | `Test 1.py` | Generic project file. |

---

## Cross-Drive Reference

Complete mapping of projects across C:, D:, and F: drives.

### Trading & Finance

| Project | C: Drive | D: Drive | F: Drive |
|---------|----------|----------|----------|
| **Brokers Platform** | -- | `D:\Code\Brokers\` | `F:\Brokers\InteractiveBrokers\` |
| **InterActiveBrokers** | -- | `D:\Code\InterActiveBrokers_Project\` | `F:\InterActiveBrokers-Project\` |
| **IronBeam** | -- | `D:\Code\IronBeam\` | `F:\IronBeam_IBKR_likeCode\` |
| **Finance Course** | -- | `D:\Code\Finance\` | `F:\FinanceCode\`, `F:\Efficient_Frontier\`, `F:\CAPM_FAMAFRENCH\` |
| **1099 Tax Forms** | -- | `D:\Code\1099_Form\` | `F:\1099_generation\` |
| **Finance Licenses** | -- | `D:\Code\FinanceLicenses\` | -- |
| **Alphainsider** | -- | -- | `F:\Alphainsider\` |
| **FinanceExamMCP** | -- | -- | `F:\FinanceExamMCP\` |
| **schwabdeb_copy** | -- | -- | `F:\schwabdeb_copy\` |

### University & Coursework

| Project | C: Drive | D: Drive | F: Drive |
|---------|----------|----------|----------|
| **Spring 2026** | -- | `D:\Code\Spring2026\` | `F:\Spring2026\` |

### Utilities & Tools

| Project | C: Drive | D: Drive | F: Drive |
|---------|----------|----------|----------|
| **ohjoshrules (device sync)** | `C:\Users\ohjos\ohjoshrules\` | `D:\Code\ohjoshrules\` | `F:\ohjoshrules\` |
| **Gmail Tools** | -- | `D:\Code\gmail-privacy-toolkit\` | `F:\gmailAPIManager\` |
| **Web Scraping** | -- | `D:\Code\WebScrapper\` | `F:\BISLWebScraper20260101\` |
| **YouTube Upload** | -- | `D:\Code\YoutubeVideoUpload\` | `F:\YoutubeVideoUpload\` |
| **Signature Tools** | `C:\Users\ohjos\SignatureSnippet\` | -- | `F:\SignatureSnippet\` |
| **Avoider Game** | `C:\Users\ohjos\PycharmProjects\A7\` | -- | `F:\avoidergame\A7\` |
| **HealthCheck** | `C:\scripts\`, `C:\Users\ohjos\Documents\` | -- | -- |
| **Crypto Mining** | -- | `D:\Code\CryptoMiner\` | -- |
| **BISL Scraper** | -- | -- | `F:\BISLWebScraper20260101\` |
| **Voice/Talk to Claude** | -- | -- | `F:\VoiceToSpeech\`, `F:\TalkToSpeech\` |
| **Canvas Scraper** | -- | -- | `F:\CanvasVideoScrapper\` |
| **STATA** | -- | -- | `F:\STATA\` |
| **Resumes** | -- | -- | `F:\resumes\` |
| **IphonePhotoCleanse** | -- | `D:\Code\IphonePhotoCleanse\` | -- |
| **CleanUP_C_Drive** | -- | `D:\Code\CleanUP_C_Drive\` | -- |
