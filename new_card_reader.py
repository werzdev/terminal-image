import asyncio
import websockets
import logging
from mfrc522 import SimpleMFRC522

# Logging einrichten
logging.basicConfig(
    filename="/home/pi/pi-webkiosk/cardreader.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

reader = SimpleMFRC522()
connected_clients = set()

async def read_rfid():
    while True:
        try:
            logging.info("Warte auf Karte...")
            id, text = reader.read()
            card_data = f"ID: {id} | Text: {text.strip()}"
            logging.info(f"Gelesen: {card_data}")
            for ws in connected_clients:
                try:
                    await ws.send(card_data)
                except websockets.exceptions.ConnectionClosed:
                    logging.warning("Verbindung zu einem Client verloren.")
            await asyncio.sleep(0.5)
        except Exception as e:
            logging.error(f"Fehler beim Lesen der Karte: {e}")

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await read_rfid()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Cardreader-Service gestoppt.")
