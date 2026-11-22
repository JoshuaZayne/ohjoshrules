---
name: reference-desktop-hardware-inventory
description: "DimaskusPC hardware, IPs, full C/E/F drive accounting, the 577 GB of stale iPhone backups, and memory state; RAM dropped to ONE 16 GB stick at 3000 on 2026-11-22, drives measured 2026-11-21"
metadata:
  node_type: memory
  type: reference
  originSessionId: d02ded55-483e-408b-b7ff-1c90a9ff273f
  modified: 2026-11-22T12:04:48.224Z
---

Desktop "DimaskusPC" full inventory, read live from the machine on 2026-11-21 at 00:59 MST.

## Machine

1. Motherboard: ASUS ROG ZENITH EXTREME (X399)
2. CPU: AMD Ryzen Threadripper 1950X, 16 cores, 32 logical processors, 1 socket
3. GPU: AMD Radeon RX 7900 XTX, driver 32.0.32029.2010, status OK. The "NVIDIA Graphics Driver 528.02" row in Programs and Features is a stale leftover, not an installed card.
4. BIOS: 2601, released 2023-07-19. Already flashed. See [[project_desktop_driver_updates]].
5. OS: Microsoft Windows 10 Home, version 10.0.19045, build 19045 (the 22H2 branch). Not Windows 11.
6. Windows reports 0 NUMA nodes, so the memory interleave mode is UMA (Distributed), not NUMA.

## Network addresses

CORRECTION measured 2026-11-22 11:26 MST: the machine is on Wi-Fi, not Ethernet. `Wi-Fi` holds
192.168.0.152 on the TP-Link_FORTRESS network with gateway 192.168.0.1, Tailscale holds
100.125.102.88, and BOTH `Ethernet 3` and `Ethernet 2` are link local 169.254.x, meaning no
Ethernet link. The 192.168.24.30 figure below is from a different network and no longer resolves.
The laptop ZAYNESURFACE11 is 100.94.1.112 on the tailnet.

## Network addresses (as measured 2026-11-21, now stale)

Three adapters are up:

1. Ethernet 3: 192.168.24.30, gateway 192.168.24.1, DNS 192.168.24.1. This is the real LAN address.
2. Tailscale: 100.125.102.88
3. VirtualBox Host-Only Network: 192.168.56.1, virtual, no gateway

## Memory

### CURRENT STATE as of 2026-11-22 05:02 MST: only ONE stick is present

1. 15.88 GB usable, so 16 GB installed. A single 16 GB Corsair CMK32GX4M2B3000C15 in DIMM 1, bank "P0 CHANNEL D". One of eight slots filled, so the quad channel board is running SINGLE channel.
2. That one stick now runs at its rated 3000 MT/s, not the old 2133 JEDEC fallback, so a DOCP or XMP profile is active.
3. This is a change of 112 GB downward from the 128 GB measured at 02:24 the same morning, so SEVEN modules are undetected, not one. The machine rebooted twice early on 2026-11-22, at 01:45 and 04:58 MST, with no bugcheck and no WHEA error in the log, which fits a deliberate BIOS tuning session rather than a crash. Whether the other three sticks were pulled on purpose or failed to train at 3000 was NOT established.
4. Single threaded copy benchmark measured 6.34 to 7.41 GB/s of combined read plus write traffic. Theoretical peak for one DDR4-3000 channel is 24.0 GB/s, against 68.3 GB/s for the four channel 2133 configuration it replaced, so peak bandwidth is now about 35 percent of what it was.
5. Raw SMBIOS Type 17 parse on 2026-11-22 confirms the firmware itself marks seven of eight slots EMPTY, so no Windows side limit such as msconfig maxmem, truncatememory or a bad memory list is involved. The modules were rejected at POST, before Windows loaded. The one surviving module reports Ranks 2, dual rank. Reading the raw table is the ONLY way to tell "slot empty" from "module present but refused", because Win32_PhysicalMemory lists populated slots only.
5. Pagefile is now the fixed 16,384 MB set during the 2026-11-21 cleanup, using only 212 MB with a 217 MB peak. That cap was sized against 64 GB of RAM. With 16 GB physical the commit limit is 31.88 GB, which constrains heavy parallel builds.
6. `Get-MMAgent` returns "Access is denied" from an unelevated session, so compression and page combining settings cannot be read without elevation. The `Memory Compression` process was resident at 229 MB, so compression is active.

### THE REAL PRIOR STATE, measured 2026-11-22 02:24 MST: 128 GB in 8 DIMMs, MIXED KITS

This is the baseline that matters, not the 2026-11-21 one below. Four more modules
were added on 2026-11-21 afternoon, which is why the 2026-11-21 audit reads 64 GB.

1. 8 modules by 16 GB equals 128 GB, 127.88 GB usable, ALL EIGHT slots filled, 2 DIMMs per channel across channels A, B, C and D.
2. Every module ran at 2133 MT/s at 1.200 V, the JEDEC fallback. No DOCP or XMP profile was enabled.
3. **THE KITS ARE MIXED, and this is the permanent cause of training trouble on this machine.** Four `CMK32GX4M2E3200C16` modules, Corsair Vengeance LPX 3200 CL16 revision E, sit in DIMM 0 of every channel. Four `CMK32GX4M2B3000C15` modules, Vengeance LPX 3000 CL15 revision B, sit in DIMM 1 of every channel. Different revision letters mean different memory integrated circuits with different voltage and timing behavior. All eight must share ONE speed, voltage and timing set, so the ceiling is whichever module gives up first, and no single DOCP profile is correct for all eight.
4. 2 DIMMs per channel times 2 ranks per dual rank module equals FOUR RANKS PER CHANNEL, the heaviest electrical load a Zen 1 memory controller can be asked to drive. Realistic ceiling is 2666, not 3200.
5. Zero WHEA hardware errors in 90 days. Three unexpected shutdowns on 2026-11-13 22:56 and 2026-11-15 at 16:08 and 19:31, the last with bugcheck 0x1000007E (0xC0000005), which is a driver signature rather than a memory signature and lines up with the BIOS 2601 and driver work.

### What the tuning guide told the owner to do, and what happened instead

The guide at `C:\Users\ohjos\Machine\Memory_Training_Guide_ROG_Zenith_Extreme_2026-11-22_022908.md` set a realistic goal of 2666 MT/s and a stretch goal of 2933, and routed around DOCP on purpose. Its Phase 1 is MANUAL DDR4-2400 at CL 16-16-16-36 with Command Rate 2T, then Phase 2 manual 2666. Finding 2 of that guide warned in as many words that a one click DOCP profile may simply fail because no single profile suits all eight mixed modules.

A one click 3000 profile appears to have been applied anyway at the 04:58 MST boot. Seven of the eight modules then failed to train and the board booted on one. The guide predicted this exact failure.

Supporting files from that session, all under `C:\Users\ohjos\Machine\`: the memory training guide above, `SecureBoot_Enable_Guide_ROG_Zenith_Extreme_2026-11-22_020126.md`, `BIOS_Card_ROG_Zenith_Extreme_2026-11-22_023948.md`, `Get-MachineTuningState.ps1` with `Run_MachineTuningState.bat`, and three baseline snapshots in `Machine\Snapshots\` from 02:45 to 02:46 that record the full 8 module state as JSON.

### Prior state, measured 2026-11-21, kept for comparison

1. 63.88 GB usable, so 64 GB installed. Four 16 GB Corsair CMK32GX4M2B3000C15 sticks in P0 channels A, B, C, D. Four of eight slots filled. OUTDATED: four more modules were added later that same day, reaching 128 GB by 2026-11-22 02:24.
2. All four ran at 2133 MHz at 1.200 V, which is the JEDEC fallback. The kit is rated 3000 MHz, so roughly 29 percent of rated bandwidth was unused. XMP was off.
3. The kit is a 2 by 16 GB part number used twice to fill four slots. A first generation Threadripper memory controller often will not hold 3000 MHz across four DIMMs; 2666 or 2933 is the realistic target. The board settling on 2133 with all four slots filled suggests it already tried and backed off.
4. DRAM frequency and timings are trained at POST. No Windows software can change them while Windows runs. AMD Ryzen Master is the only Windows side route and it applies on reboot; it was NOT installed as of that date.
5. Memory compression: on. Page combining: off. Application prelaunch: on. Standby cache 26.17 GB against 18.84 GB committed, so the machine was under no memory pressure at all.

### What WMI cannot tell you about this memory

The `ConfiguredVoltage`, `MinVoltage` and `MaxVoltage` fields all read 1200 mV, which is the SMBIOS nominal DDR4 figure and NOT the live DIMM voltage; the 3000 C15 profile for this kit calls for 1.35 V. WMI exposes no CAS latency or subtiming at all. Use HWiNFO64, CPU-Z or the BIOS for real timings and voltage.

## Drives

Logical volumes:

1. C: "Windows 10 Raid", NTFS, 4 KB clusters, 3,723.0 GB total, 1,199.3 GB free
2. D: "MRI 1", FAT32, 16 KB clusters, 28.9 GB total, 25.1 GB free. Removable Kanguru FlashBlu USB stick.
3. E: "GS#16", exFAT, 512 KB clusters, 1,863.0 GB total, 0.00 GB free. See [[project-e-drive-backup-slack]].
4. F: "1TB RAID", NTFS, 4 KB clusters, 952.7 GB total, 166.4 GB free

Physical disks:

1. PHYSICALDRIVE1: AMD-RAID Array 1, 3,724.0 GB, 3 partitions. The boot array behind C:.
2. PHYSICALDRIVE2: AMD-RAID Array 2, 952.7 GB, 1 partition, which is F:.
3. PHYSICALDRIVE3: Samsung PSSD T7 external SSD, 1,863.0 GB, which is E:.
4. PHYSICALDRIVE0: Kanguru FlashBlu USB stick, 28.9 GB, which is D:.

F: top level content, largest first: Media_Archive_2019 313.72 GB, GitHub Repos 220.32 GB, iCloudDrive 92.88 GB, PhotoLibrary 63.22 GB, OllamaModels 59.81 GB, SCHOOOL_RAID0_ 34.06 GB, Josh's Stuff 14.41 GB, PhoneImportStaging 3.78 GB, STATA 1.47 GB. Every other folder on F: is under 1 GB.

C: root, largest first: Ohjoshrules 254.13 GB, pagefile.sys 72.00 GB, Program Files 71.62 GB, Windows 46.42 GB, hiberfil.sys 25.55 GB, Program Files (x86) 22.16 GB, System Volume Information 17.33 GB, Jts 8.82 GB, RustTOS_backup_mirror 7.07 GB, Autodesk 4.68 GB. A stray 2.78 GB file literally named PHYSICALDRIVE4 sits at the C: root, unexplained. Root items total about 539.4 GB, leaving about 1,984 GB in C:\Users.

C:\Users\ohjos real contents: AppData 1,081.11 GB, OneDrive 224.05 GB, Music 206.51 GB, Videos 179.63 GB, RustTOS_target_C 160.17 GB, Documents 43.68 GB, Pictures 24.70 GB, anaconda3 20.33 GB, iCloudPhotos 17.96 GB. Inside AppData: Roaming\Apple Computer 607.78 GB, Local\wsl 151.54 GB, Local\Microsoft 60.85 GB, Local\Docker 56.31 GB, Local\Temp 54.18 GB, Local\Comfy-Desktop 33.75 GB.

## Two traps when measuring C:\Users on this machine

Any naive recursive scan of C:\Users\ohjos reports 4,128.57 GB, larger than the whole drive. Both causes must be corrected for:

1. Legacy compatibility junctions double count. `Application Data` points to AppData\Roaming (626.96 GB), `Local Settings` to AppData\Local (453.59 GB), `My Documents` to Documents (43.68 GB), and `AppData\Local\Application Data` is self referential back to AppData\Local (453.59 GB). Use robocopy /XJ or skip ReparsePoint attributes. Also `C:\Users\All Users` is a junction to C:\ProgramData, not extra space. One junction is genuinely useful: `indicators` under the profile points to F:\GitHub Repos\indicators.
2. Cloud placeholders report full size while occupying nothing. `iCloudPhotos` is 1,019.86 GB logical but only 17.96 GB on disk, with 91,574 placeholder files out of 107,083. `OneDrive` is 230.15 GB logical and 224.05 GB on disk, so it is nearly all real. Detect placeholders by testing the file attributes OFFLINE 0x1000, RECALL_ON_OPEN 0x40000, RECALL_ON_DATA_ACCESS 0x400000 and SPARSE 0x200.

Corrected: 4,128.57 less 1,124.23 of junction duplicates less 1,008.00 of placeholders gives 1,996.34 GB, against 1,984.3 GB implied by the volume. The 0.7 percent gap is 4 KB cluster rounding. The C: accounting is closed.

## Cleanup carried out 2026-11-21, and what C: looks like now

Four changes were made on 2026-11-21 between 00:58 and 01:32 MST. C: free went from 1,199.30 GB to 1,847.33 GB, from 32 percent of the drive to 50 percent, reaching about 1,903 GB (51 percent) after the next reboot.

1. Power plan switched, see above.
2. `AppData\Local\Temp` cleared: 54.18 GB to 3.34 GB, reclaiming 50.84 GB. 68,471 items removed, 12 locked by running processes.
3. Pagefile capped at a fixed 16,384 MB, down from 73,728 MB against a 2,407 MB lifetime peak. Automatic management is now OFF. Takes effect on reboot, worth about 56 GB. Restore with `Get-CimInstance Win32_ComputerSystem | Set-CimInstance -Property @{ AutomaticManagedPagefile = $true }`.
4. Hibernation disabled with `powercfg /hibernate off`; `C:\hiberfil.sys` removed, 25.55 GB back immediately. NOTE: this also disabled Fast Startup, so cold boots are slower. Sleep (S3) still works. Restore with `powercfg /hibernate on`.

### iPhone backups DELETED, permanently

The user explicitly confirmed on 2026-11-21 after being shown that no second copy existed. All five September 2022 backups in `AppData\Roaming\Apple Computer\MobileSync\Backup` were removed, 576.70 GB: iPhone 11 Pro 248.05 GB, Josh's iPhone 14 Pro 151.82 GB, "Tooner" iPhone 7 Plus on iOS 13.3 99.13 GB, "Olive's Black Mirror" iPhone 13 Pro Max 77.70 GB, and an empty folder. KEPT: `00008130-000959482021401C`, 10.14 GB, dated 2023-10-25, device unidentified. `Apple Computer` went from 607.78 GB to 31.09 GB.

The identity record for every deleted backup (device name, model, iOS, serial, IMEI, backup date) is preserved at `C:\Users\ohjos\Notes\iPhone_Backup_Manifest_2026-11-21_012000.md`. The contents themselves are unrecoverable: the Geek Squad backup on E: has a `User Data` folder with NO `AppData` directory, so it never held MobileSync.

Full audit report: `C:\Users\ohjos\Notes\System_Audit_DimaskusPC_2026-11-21_011017.md`.

### Still available, not done

1. `RustTOS_target_C` 160.17 GB of regenerable Rust build output
2. E: reformat at 32 KB clusters, about 350 GB, needs 1.46 TB of staging space
3. The two suspected corrupt 44 GB images on E:, 88 GB, not yet validated by reading their headers
4. Reseat the three missing DIMMs and find the highest speed that trains with all four populated. The 2026-11-22 state proves the kit itself reaches 3000 with one stick, so the ceiling is the memory controller under load, not the modules.

## Power plan, changed this session

Was `DllFixer Power Saver` (GUID 676bea0c-c3f3-4aa3-ba42-6114a16b6fc4), a leftover custom scheme from software no longer in the installed programs list. Its maximum processor state was 100 percent so it did not cap clocks, but its minimum processor state was 5 percent, which on Threadripper means aggressive core parking and slow ramp.

Switched on 2026-11-21 to `AMD Ryzen Balanced` (GUID 9897998c-92de-4669-853f-b7cd3ecb2790), which sets minimum processor state to 90 percent and maximum to 100 percent. The AMD Ryzen Balanced Driver is installed. Reversible with:

    powercfg /setactive 676bea0c-c3f3-4aa3-ba42-6114a16b6fc4

## Problem devices

Only two, both benign: PANGP Virtual Ethernet Adapter and the Cisco AnyConnect virtual miniport, each error code 22, meaning disabled. The AMD PSP Device error 43 recorded in [[project_desktop_driver_updates]] is RESOLVED, confirmed clear after BIOS 2601.

**Why:** the user asks for machine facts (IP, OS, drives, RAM) often enough that re-measuring every time wastes a session, and the memory speed and power plan findings explain real performance loss.

**How to apply:** treat the numbers as of 2026-11-21 00:59 MST and re-measure before quoting free space, which moves. The fixed facts (board, CPU, cluster sizes, DIMM part number, RAID boot layout) are stable. Related: [[project_c_drive_space_cleanup]], [[reference-rusttos-backups-and-data-jobs]], [[user_github_and_devices]].
