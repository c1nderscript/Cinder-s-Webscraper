#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Prepare required directories
mkdir -p data/logs output/scraped_data

# Create empty config files if missing
: > data/websites.json
: > data/schedules.db
if [ ! -f data/config.json ]; then
  : > data/config.json
fi
