#!/bin/bash

# --------------------
# KONFIGURATION
# --------------------

# Lokaler Modus ODER extern?
USE_LOCAL=true

# Wenn USE_LOCAL=true:
LOCAL_PORT=8080
LOCAL_PATH="/home/pi/pi-webkiosk/frontend"

# Wenn USE_LOCAL=false:
REMOTE_URL="https://deine-website.de/kiosk"

# --------------------
# Starte je nach Modus
# --------------------

if [ "$USE_LOCAL" = true ]; then
  cd "$LOCAL_PATH"
  python3 -m http.server "$LOCAL_PORT" &
  sleep 2
  chromium-browser --kiosk http://localhost:$LOCAL_PORT
else
  chromium-browser --kiosk "$REMOTE_URL"
fi
