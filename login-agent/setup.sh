#!/bin/bash
# Naye machine pe: ./setup.sh  (python3.11+ chahiye)
set -e
cd "$(dirname "$0")"
PY=$(command -v python3.12 || command -v python3.11) || { echo "python3.11+ install karo"; exit 1; }
$PY -m venv .venv
./.venv/bin/pip -q install --upgrade pip
./.venv/bin/pip -q install browser-use python-dotenv
cp -n .env.example .env || true
cp -n tasks.example.json tasks.json || true
echo "Done. Ab: .env bharo (API key + passwords), phir: ./.venv/bin/python run_batch.py signup"
