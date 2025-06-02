from django.urls import path
from django.http import JsonResponse
from .views import RegisterView  # or any other views you have

def accounts_home(request):
    return JsonResponse({
        "message": "Accounts API active",
        "available_endpoints": ["/register/"]
    })

urlpatterns = [
    path('', accounts_home),  # This will fix the 404 at /api/accounts/
    path('register/', RegisterView.as_view(), name='register'),
]
