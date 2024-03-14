from django.shortcuts import render
from django.views import View


class Index(View):
    """Test"""

    def get(self, request):
        """Test view"""
        return render(request, "base.html", {})
