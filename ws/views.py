from django.http import JsonResponse
from django.views import View


class Index(View):
    """Test"""

    def get(self, request):
        """Test view"""
        data = {"Hello Brian Huynh": "yes I am"}
        return JsonResponse(data)
