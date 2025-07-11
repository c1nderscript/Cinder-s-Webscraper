#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Prepare required directories
mkdir -p data/logs output/scraped_data

# Create empty config files if missing without truncating existing files
if [ ! -f "data/websites.json" ]; then
    touch "data/websites.json"
fi

if [ ! -f "data/schedules.db" ]; then
    touch "data/schedules.db"
fi
