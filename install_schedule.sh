#!/usr/bin/env bash
# Registers a cron entry that runs sync_memory.py --sync on a schedule.
#
# Usage:
#   ./install_schedule.sh                 # default: every hour at :05
#   ./install_schedule.sh "*/15 * * * *"  # custom cron expression
#
# Run this ONCE per Linux / Raspberry Pi device. It uses the current folder,
# so make sure you run it from a permanent clone location.

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WRAPPER="$SCRIPT_DIR/sync_memory.sh"
LOG_FILE="$SCRIPT_DIR/sync_memory.log"
MARKER="# ClaudeMemorySync"

if [ ! -x "$WRAPPER" ]; then
    chmod +x "$WRAPPER" || true
fi

SCHEDULE="${1:-5 * * * *}"
CRON_LINE="$SCHEDULE $WRAPPER --sync >> $LOG_FILE 2>&1 $MARKER"

# Remove any existing entry with our marker, then append the new one.
TMP="$(mktemp)"
crontab -l 2>/dev/null | grep -v "$MARKER" > "$TMP" || true
echo "$CRON_LINE" >> "$TMP"
crontab "$TMP"
rm -f "$TMP"

echo "Cron entry installed:"
echo "  $CRON_LINE"
echo
echo "To view:    crontab -l"
echo "To remove:  ./uninstall_schedule.sh"
echo "Log file:   $LOG_FILE"
