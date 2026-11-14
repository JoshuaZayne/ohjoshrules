---
name: project_desktop_driver_updates
description: "Desktop driver update 2026-11-13: what was downloaded, what is pending (install run, BIOS 2601 flash), and the RAID boot drive caution"
metadata:
  node_type: memory
  type: project
  originSessionId: cccc1980-e14d-4fe8-81f6-b5bb02397b42
  modified: 2026-11-14T05:34:21.913Z
---

Desktop hardware: ASUS ROG Zenith Extreme (X399), Threadripper 1950X, Radeon RX 7900 XTX, Windows 10 Home 19045.
Windows BOOTS FROM "AMD-RAID Array 1" (3724 GB); "AMD-RAID Array 2" (953 GB) is data.

State as of 2026-11-13 22:28 MST (nothing installed yet; first attempt's UAC prompt timed out unseen):
1. Folder: C:\Users\ohjos\Downloads\Driver_Updates_2026-11-13_221254
2. Full record with SHA256, URLs, decisions: DRIVER_UPDATE_RECORD_2026-11-13_222820.txt in that folder
3. User runs Install_Driver_Updates.bat (self elevating) which: restore point, Marvell AQtion 10G 3.1.3.0, Qualcomm 11ad 2.0.85.0, Apple USB driver via Windows Update, Realtek audio 6.0.1.9359 (ASUS AsusSetup.exe, interactive), AMD Adrenalin 26.11.1 Optional (last; its Restart button is the single restart). Logs to install_log_<timestamp>.txt.
4. BIOS: installed 1402 (2018); latest 2601 (ASUS 2023-08-30) downloaded, NOT flashed. Must be done by hand via EZ Flash 3. Flash resets SATA Mode / NVMe RAID mode; must be set back to RAID or Windows will not boot.
5. Left alone on purpose: AMD RAID driver 9.2.0.105 (newer than ASUS 9.2.0.87, and boot drive is RAID); chipset 8.09.28.1124; Bluetooth 10.0.0.448; Wi-Fi 12.0.0.722; Intel I211.
6. Open question: VirtualBox 6.1.34 to 7.x (app upgrade, may affect VMs), user not asked yet.
7. AMD PSP Device (second die) shows error 43; recheck after BIOS 2601.

ASUS's support API that lists this board's BIOS/drivers (the asus.com product.asmx one returns FAIL):
https://rog.asus.com/support/webapi/product/GetPDBIOS?website=us&model=ROG-ZENITH-EXTREME&systemCode=rog
(GetPDDrivers with &osid=45 for Windows 10 64-bit drivers)

**Why:** user asked for all driver updates; RAID boot makes RAID driver and BIOS steps risky.
**How to apply:** next session, read the install_log_*.txt in the folder to see what actually installed, then follow up on BIOS flash and VirtualBox. See [[feedback_uac_prompt_from_session]].
