import json

# from asgiref.sync import async_to_sync
from pprint import pprint

# from channels.auth import login, logout, get_user
from channels.generic.websocket import WebsocketConsumer


class OrderConsumer(WebsocketConsumer):

    def connect(self):
        print("Welcome to websocket")
        if self.scope["user"].is_authenticated:
            print("Scope info ====> ")
            pprint(self.scope)
            print("Username ====> ", self.scope["user"].username)
            print("email ====> ", self.scope["user"].email)
            print("Logged in User =====> ")
            pprint(vars(self.scope["user"]._wrapped))
            print("Authenticate result ====> ", self.scope["user"].is_authenticated)

            self.accept()
            self.send(text_data=json.dumps({"message": "Connected"}))
        else:
            print("============User not logged it, so not able to use WS============")

    def disconnect(self, close_code):
        print("Olala coca")
        self.accept()
        self.send(text_data=json.dumps({"message": "Dis-connected"}))

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        print("text_data==>", text_data)
        self.send(text_data=json.dumps({"message": "Hello world!"}))
