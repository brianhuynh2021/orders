import json

from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken


class OrderConsumer(WebsocketConsumer):
    def verify_token(self, token):
        try:
            decoded_token = AccessToken(token)
            user_id = decoded_token.payload.get("user_id")
            if user_id is not None:
                User = get_user_model()
                user = User.objects.get(id=user_id)
                if user.is_active:
                    return True
        except Exception as e:
            print("Error verifying token:", str(e))
        return False

    def connect(self):
        self.user = None
        self.token = None
        headers = self.scope.get("headers")
        if headers:
            for key, value in headers:
                if key.lower() == b"authorization":
                    self.token = value.decode("utf-8")
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
        await self.send(text_data=json.dumps({"message": "Disconnected"}))
        await self.close()

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({"message": "Hello world!"}))
