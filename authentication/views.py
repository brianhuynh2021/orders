from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginAPIView(APIView):
    authentication_classes = []  # No authentication classes needed for login
    permission_classes = [AllowAny]  # Allow access to unauthenticated users

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data.get("username_or_email")
            password = serializer.validated_data["password"]

            user = authenticate(username=username_or_email, password=password)
            if user is None:
                # Attempt to authenticate by email not support will customize it later
                user = authenticate(email=username_or_email, password=password)
            if user:
                login(request, user)
                # Check if token exists and is not expired
                token, created = Token.objects.get_or_create(user=user)
                if not created and token.created + timedelta(days=1) <= timezone.now():
                    # If token exists but is expired, refresh it
                    token.delete()
                    token = Token.objects.create(user=user)
                elif created:
                    # If token was just created, set its expiration time
                    token.created = timezone.now()
                    token.save()

                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
