---
name: project_cod_tpm_attestation
description: "Call of Duty MW4 attestation failure on DimaskusPC: cause is AMD fTPM 3.8.0.3, which ASUS will never fix on X399; escalation drafts written 2026-11-22"
metadata:
  node_type: memory
  type: project
  originSessionId: 2c1990e4-e864-4579-83fc-49b324613ace
  modified: 2026-11-22T12:31:10.700Z
---

Call of Duty keeps sending the owner to Activision's Trusted Platform Module and Secure Boot page demanding a BIOS update, even though BIOS 2601 is already flashed. Diagnosed on the machine 2026-11-22 at 05:11:07 MST.

## The cause, confirmed

The only failing requirement is the AMD firmware Trusted Platform Module version. `tpmtool getdeviceinformation` reports Manufacturer AMD, Manufacturer Version **3.8.0.3**. Activision's article says verbatim that AMD boards with Manufacturer Version `3.*.0.*` "are not compatible" and "require a firmware update to meet compliance". 3.8.0.3 matches: 3 in the first field, 0 in the third.

Everything else already passes: Secure Boot enabled (`UEFISecureBootEnabled = 1`), UEFI mode, GPT boot disk, TPM 2.0 present and device status OK, `Ready For Attestation: True`, `Is Capable For Attestation: True`, Windows 10 Home 22H2 build 19045.6466 which clears Activision's floor of Windows 10 22H2. `PCR7 Binding State` reads 2, meaning unbound, which no published source maps numerically; it is plausibly the AMD RAID boot path adding extra measurements to PCR7.

## Why it cannot be fixed with a BIOS

BIOS 2601 (2023-07-19) is the last release ASUS will ever publish for the ROG Zenith Extreme. X399 and first generation Threadripper are past end of firmware support. AMD article PA-420 says AMD gave board makers corrected firmware TPM images in 2022; ASUS never published one for X399. So Activision's prescribed remedy does not exist for this machine. Do NOT keep hunting for a newer BIOS: there is none. See [[project_desktop_driver_updates]] and [[reference-desktop-hardware-inventory]].

## Game install locations

The affected title is the Steam one, `cod26` which is Modern Warfare 4, at `C:\Ohjoshrules\steamapps\common\Call of Duty HQ`. The Secure Attestation Wizard ships with it: `CODSecureAttestationWizard.exe` in that folder, needs Run as administrator. Old Battle.net installs sit at `F:\Call of Duty\Call of Duty Modern Warfare` and the Cold War beta.

## Wizard result, run 2026-11-22 at 05:18:09 MST

`CODSecureAttestationWizard.exe` needs NO administrator rights; its manifest is `asInvoker`, so there is no UAC trap. It is a GUI app with no command line switches, but its interface is standard WPF, so `System.Windows.Automation` reads every label out of it without needing optical character recognition.

Its Scan Complete screen PASSES "TPM 2.0" and PASSES "Secure Boot", and fails only "BIOS Firmware Update Required", with "Attestation Requisite not met" and a banner saying "Failed Attestation Status will be applied, match quality will be reduced". That is the perfect evidence for the tickets: Activision's own tool clears both configurable items and fails only the one with no available fix. Screenshot kept at `C:\Users\ohjos\Notes\CoD_Attestation_Wizard_Result_2026-11-22_051809.png`.

## The real mechanism, from the diagnostic bundle 2026-11-22 05:21:50 MST

The wizard's Help tab has a "Create diagnostic file" button. It writes with NO save dialog, straight to `C:\Users\ohjos\Documents\SecureAttestationDiagnostic.zip`, 77.9 KB, holding `certreq_output.txt` and `diagnostic_info.json`. Timestamped copy at `C:\Users\ohjos\Notes\CoD_Attestation_Diagnostic_2026-11-22_052150.zip`. Scanned clean: no user name, email, machine name, paths or board serial, so it is safe to attach anywhere.

The bundle shows the defect is deeper than a version string:

1. The firmware TPM holds NO Endorsement Key certificate at all. `rsaEkExists` and `eccEkExists` are both false and all nine certificate indexes (0x01C00002, 0x01C00012, 0x01C0001C, 0x01C0001E, 0x01C0000A, 0x01C00014, 0x01C00016, 0x01C00018, 0x01C0001A) report present false. Only the manufacturer can provision that, at firmware level.
2. The Endorsement Key present was signed by an AMD ENGINEERING authority: issuer `CN=PRG-ZP, O=Advanced Micro Devices, S=CA, L=Sunnyvale, C=US, OU=Engineering`, key identity `AMD-KeyId-578c545f796951421221a4a578acdb5f682f89c8`, firmware 196616.3 which is 0x30008 meaning 3.8.
3. So Microsoft's Attestation Identity Key service returns HTTP 404, "The authority ... does not exist", failing at EnrollStage 140 with 0x80190194 HTTP_E_STATUS_NOT_FOUND.

Wizard internal checks: every REQUIRED check passes (TPM2_PRESENT, CAN_TURN_ON_SECURE_BOOT, SHOULD_TURN_ON_SECURE_BOOT). The sole failure is `AMDFW_NEEDS_UPDATE`, graded EXPECTED, which is why the status is "temporarily compliant" rather than a hard block. Side note not implicated in any check: IOMMU reports available false and enabled false.

## The voluntary TPM report form EXCLUDES this machine

Do not submit support.activision.com/tpm-report. Its warning box says do not report AMD devices with Manufacturer Version `3.*.0.*`, which is exactly 3.8.0.3. Had it been open, the answers were: manufacturer ASUS, version number 3.8.0.3 (that field means the TPM Manufacturer Version, NOT BIOS 2601).

## Escalation state

All DRAFTED, none sent as of 2026-11-22 05:29:27 MST. Final ready to paste tickets, each standalone:

1. `C:\Users\ohjos\Notes\Ticket_Activision_2026-11-22_052927.txt` for support.activision.com/options. Tone is firm and deflection proof, opening by pre-empting the canned "enable Secure Boot" reply. Attach both the screenshot and the ZIP.
2. `C:\Users\ohjos\Notes\Ticket_ASUS_2026-11-22_052927.txt` for asus.com/support. Tone is collegial, since ASUS is the only party who can fix it and the board really is out of support. Gives them an easy second option (name the correct discrete TPM module and say whether the header is LPC or SPI) so they can help even if no BIOS is coming. Attach the ZIP.

Background and full evidence live in `C:\Users\ohjos\Notes\CoD_TPM_Attestation_Escalation_2026-11-22_051107.txt`, whose Parts 4 and 5 are the superseded earlier drafts. Key trap: the Activision TPM report form at support.activision.com/tpm-report says verbatim it "will not create a support ticket, and you will not receive a response", so the real ticket route is support.activision.com/options.

The one open hardware question, asked in both drafts: whether a discrete TPM 2.0 module on the board's 14-1 pin TPM header would present a compliant non AMD Manufacturer Version and pass attestation. The Zenith Extreme manual documents a 14-1 pin TPM connector, but ASUS TPM-M R2.0 listings name the later Zenith II Extreme Alpha, and LPC against SPI was not resolved. UNVERIFIED, so nothing should be bought on spec.

**Why:** the owner was being told to update an already current BIOS, so the real blocker needed naming, and the escalation path is counterintuitive because the obvious form is a dead end.

**How to apply:** if this comes up again, re-read the fTPM version first with `tpmtool getdeviceinformation`; if it still starts with 3 and has 0 in the third field, nothing software side will fix it. Related: [[feedback_no_auto_reply]], [[feedback_verifiable_claims]].
