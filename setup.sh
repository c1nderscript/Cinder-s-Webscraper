#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Prepare required directories
mkdir -p data/logs output

# Create empty config files if missing
if [ ! -f data/websites.json ]; then
  touch data/websites.json
fi

if [ ! -f data/schedules.db ]; then
  touch data/schedules.db
fi

if [ ! -f data/config.json ]; then
  touch data/config.json
fi
