from django.shortcuts import render
from django.views import View


class Index(View):
    """Test"""

    def get(self, request):
        """'TEst view"""
        return render(request, "base.html", {})
