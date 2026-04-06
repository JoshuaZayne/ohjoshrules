#!/usr/bin/env bash
# Linux / Raspberry Pi wrapper for sync_memory.py
# Usage: ./sync_memory.sh            (pull from github into local Claude memory)
#        ./sync_memory.sh --push     (push local memory up to repo)
#        ./sync_memory.sh --sync     (full round-trip: pull, push local, commit+push)
#        ./sync_memory.sh --status   (show device detection)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 "$SCRIPT_DIR/sync_memory.py" "$@"
