---
name: reference-desktop-hardware-inventory
description: "DimaskusPC hardware, IPs, full C/E/F drive accounting, the 577 GB of stale iPhone backups, and memory speed state, measured 2026-11-21"
metadata:
  node_type: memory
  type: reference
  originSessionId: d02ded55-483e-408b-b7ff-1c90a9ff273f
  modified: 2026-11-21T08:34:40.253Z
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

Three adapters are up:

1. Ethernet 3: 192.168.24.30, gateway 192.168.24.1, DNS 192.168.24.1. This is the real LAN address.
2. Tailscale: 100.125.102.88
3. VirtualBox Host-Only Network: 192.168.56.1, virtual, no gateway

## Memory

1. 63.88 GB usable, so 64 GB installed. Four 16 GB Corsair CMK32GX4M2B3000C15 sticks in P0 channels A, B, C, D. Four of eight slots filled.
2. All four run at 2133 MHz at 1.200 V, which is the JEDEC fallback. The kit is rated 3000 MHz, so roughly 29 percent of rated bandwidth is unused. XMP is off.
3. The kit is a 2 by 16 GB part number used twice to fill four slots. A first generation Threadripper memory controller often will not hold 3000 MHz across four DIMMs; 2666 or 2933 is the realistic target. The board settling on 2133 with all four slots filled suggests it already tried and backed off.
4. DRAM frequency and timings are trained at POST. No Windows software can change them while Windows runs. AMD Ryzen Master is the only Windows side route and it applies on reboot; it is NOT installed as of this date.
5. Memory compression: on. Page combining: off. Application prelaunch: on. Standby cache 26.17 GB against 18.84 GB committed, so the machine is under no memory pressure at all.
6. Pagefile: C:\pagefile.sys allocated 73,728 MB with a lifetime peak usage of only 2,407 MB. Capping it near 16 GB would return roughly 57 GB to C: with no practical risk. Not yet done.

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
4. AMD Ryzen Master for a memory speed attempt above 2133 MHz

## Power plan, changed this session

Was `DllFixer Power Saver` (GUID 676bea0c-c3f3-4aa3-ba42-6114a16b6fc4), a leftover custom scheme from software no longer in the installed programs list. Its maximum processor state was 100 percent so it did not cap clocks, but its minimum processor state was 5 percent, which on Threadripper means aggressive core parking and slow ramp.

Switched on 2026-11-21 to `AMD Ryzen Balanced` (GUID 9897998c-92de-4669-853f-b7cd3ecb2790), which sets minimum processor state to 90 percent and maximum to 100 percent. The AMD Ryzen Balanced Driver is installed. Reversible with:

    powercfg /setactive 676bea0c-c3f3-4aa3-ba42-6114a16b6fc4

## Problem devices

Only two, both benign: PANGP Virtual Ethernet Adapter and the Cisco AnyConnect virtual miniport, each error code 22, meaning disabled. The AMD PSP Device error 43 recorded in [[project_desktop_driver_updates]] is RESOLVED, confirmed clear after BIOS 2601.

**Why:** the user asks for machine facts (IP, OS, drives, RAM) often enough that re-measuring every time wastes a session, and the memory speed and power plan findings explain real performance loss.

**How to apply:** treat the numbers as of 2026-11-21 00:59 MST and re-measure before quoting free space, which moves. The fixed facts (board, CPU, cluster sizes, DIMM part number, RAID boot layout) are stable. Related: [[project_c_drive_space_cleanup]], [[reference-rusttos-backups-and-data-jobs]], [[user_github_and_devices]].
