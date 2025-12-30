#!/usr/bin/env bash
set -euo pipefail

# Usage (recommended):
#   echo -n "YOUR_API_KEY" | ./scripts/set-secret.sh
# This avoids leaving the secret in your shell history.

REPO="suryapetshops-art/mcp-rag-"

if [ -t 0 ]; then
  echo "Reading API key from stdin..."
else
  echo "No stdin detected. Usage: echo -n \"YOUR_API_KEY\" | $0" >&2
  exit 1
fi

# Read key from stdin without storing in a variable where possible
API_KEY=$(cat -)

echo -n "$API_KEY" | gh secret set API_KEY --repo "$REPO"

echo "Secret set for $REPO"
