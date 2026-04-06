#!/usr/bin/env bash
# Removes the ClaudeMemorySync cron entry.
set -e

MARKER="# ClaudeMemorySync"
TMP="$(mktemp)"
crontab -l 2>/dev/null | grep -v "$MARKER" > "$TMP" || true
crontab "$TMP"
rm -f "$TMP"
echo "ClaudeMemorySync cron entry removed (if it existed)."
