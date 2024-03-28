from datetime import timedelta

from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer


class LoginAPIView(APIView):
    authentication_classes = []  # No authentication classes needed for login
    permission_classes = [AllowAny]  # Allow access to unauthenticated users

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data.get("username_or_email")
            password = serializer.validated_data["password"]

            user = authenticate(request, username=username_or_email, password=password)
            if user is None:
                user = authenticate(request, email=username_or_email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token
                return Response(
                    {"access_token": str(access), "refresh_token": str(refresh)}
                )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
