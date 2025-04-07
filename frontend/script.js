const statusEl = document.getElementById("status");
const lastScanEl = document.getElementById("last-scan");
const logEl = document.getElementById("log");

const ws = new WebSocket("ws://localhost:8765");

ws.onopen = () => {
  statusEl.textContent = "✅ WebSocket verbunden";
  statusEl.style.color = "green";
};

ws.onmessage = (event) => {
  const data = event.data;
  const time = new Date().toLocaleTimeString();
  lastScanEl.textContent = `${data} (${time})`;

  const li = document.createElement("li");
  li.textContent = `${time} – ${data}`;
  logEl.prepend(li);
};

ws.onerror = () => {
  statusEl.textContent = "❌ WebSocket-Fehler";
  statusEl.style.color = "red";
};

ws.onclose = () => {
  statusEl.textContent = "⚠️ Verbindung geschlossen";
  statusEl.style.color = "orange";
};
