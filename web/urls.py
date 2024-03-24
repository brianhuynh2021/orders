from django.urls import path

from web.views import Index, Login

urlpatterns = [path("", Index.as_view()), path("login", Login.as_view())]
