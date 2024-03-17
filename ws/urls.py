# urls.py
from django.urls import path

from ws.views import Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
]
