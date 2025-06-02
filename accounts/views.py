from django.http import JsonResponse
from django.views import View

class RegisterView(View):
    def get(self, request):
        return JsonResponse({"message": "Register endpoint active"})
