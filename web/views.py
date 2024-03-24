from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):
        """Test view"""
        return render(request, "base.html", {})


class Login(View):
    def get(self, request):
        username = "admin"
        password = "admin"
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login Success"})
        else:
            # Return an 'invalid login' error message.
            return JsonResponse({"message": "Login failed"})
