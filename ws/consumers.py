import json

from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer
from rest_framework.authtoken.models import Token


class OrderConsumer(WebsocketConsumer):
    @database_sync_to_async
    def verify_token(self, key):
        try:
            token = Token.objects.get(key=key)
            print("token==>", token)
            return token.user.is_active
        except Token.DoesNotExist:
            return False

    def connect(self):
        print("Welcome to websocket")
        self.user = None
        self.token = None
        headers = self.scope.get("headers")
        print("header==>", headers)
        if headers:
            for key, value in headers:
                if key.lower() == b"authorization":
                    self.token = value.decode("utf-8")
                    print("self.token==>", self.token)
                    break
        result = self.verify_token(self.token)
        print("result==>", result)
        if result:
            print("alo")
            self.accept()
            self.send(text_data=json.dumps({"message": "Connected"}))
        else:
            # If the token is missing or invalid, close the connection
            self.close()

    async def disconnect(self, close_code):
        print("Olala coca")
        await self.send(text_data=json.dumps({"message": "Dis-connected"}))
        await self.close()

    async def receive(self, text_data):
        print("text_data==>", text_data)
        await self.send(text_data=json.dumps({"message": "Hello world!"}))
