#!/bin/bash

set -e

SOURCE_LOGS="$HOME/Documents/sahzade-ai-local-chat-mini (v2)/logs/chat_logs.jsonl"
TARGET_LOGS="data/input/chat_logs.jsonl"

echo "Copying V2 chat logs..."

if [ ! -f "$SOURCE_LOGS" ]; then
  echo "Source log file not found:"
  echo "$SOURCE_LOGS"
  exit 1
fi

cp "$SOURCE_LOGS" "$TARGET_LOGS"

echo "Logs copied successfully."
echo "Saved to: $TARGET_LOGS"