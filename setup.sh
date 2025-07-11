#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Prepare required directories
mkdir -p data/logs output

# Create empty config files if missing
: > data/websites.json
: > data/schedules.db
