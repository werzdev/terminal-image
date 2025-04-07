## SPI aktivieren und Bibliotheken installieren
sudo raspi-config          # -> Interface Options -> SPI -> Enable
pip install mfrc522 websockets

## kiosk.sh ausführbar machen
chmod +x /home/pi/pi-webkiosk/run_kiosk.sh

## Services aktivieren und starten
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

sudo systemctl enable rfid-websocket.service
sudo systemctl enable kiosk.service

sudo systemctl start rfid-websocket.service
sudo systemctl start kiosk.service

## Logs auslesen via systemd
journalctl -u rfid-websocket.service -f

