from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root welcome message
def welcome(request):
    return JsonResponse({
        "message": "Welcome to FandrLearn Backend API",
        "status": "running",
        "endpoints": {
            "health": "/api/health/",
            "accounts": "/api/accounts/",
            "courses": "/api/courses/",
            "admin": "/admin/"
        }
    })

# Health check endpoint
def health_check(request):
    return JsonResponse({
        "status": "ok",
        "message": "Backend is healthy"
    })

urlpatterns = [
    path('', welcome),  # Root URL
    path('admin/', admin.site.urls),  # Admin panel
    path('api/health/', health_check),  # Health check endpoint

    # API apps
    path('api/accounts/', include('accounts.urls')),  # Accounts app
    path('api/courses/', include('courses.urls')),    # Courses app
]

