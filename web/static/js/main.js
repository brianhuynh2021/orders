const wsUrl = "ws://" + window.location.host + "/ws/order/"
console.log("WS URL ======> ", wsUrl)
const ws = new WebSocket(wsUrl)

ws.onclose = function (e) {
  console.error("Chat socket closed unexpectedly")
}

ws.onopen = function (e) {
  console.log("====== WS Client opened successfully! ======")
}

ws.onmessage = function (e) {}
