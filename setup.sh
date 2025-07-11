#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Prepare required directories
mkdir -p data/logs output

# Create empty config files if missing
: > data/websites.json
if [ ! -f data/schedules.db ]; then
  python - <<'EOF'
from cinder_web_scraper.scheduling.schedule_manager import ScheduleManager
ScheduleManager("data/schedules.db").close()
EOF
fi
if [ ! -f data/config.json ]; then
  : > data/config.json
fi
