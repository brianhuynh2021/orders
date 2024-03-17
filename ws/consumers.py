import json

from channels.generic.websocket import WebsocketConsumer


class OrderConsumer(WebsocketConsumer):
    def connect(self):
        print("Welcome to websocket")
        self.accept()
        self.send(text_data=json.dumps({"message": "Connected"}))

    def disconnect(self, close_code):
        print("Olala coca")
        self.accept()
        self.send(text_data=json.dumps({"message": "Dis-connected"}))

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        print("text_data==>", text_data)
        self.send(text_data=json.dumps({"message": "Hello world!"}))
