from django.shortcuts import redirect
from django.urls import reverse

class BlockAdminForNonAdminsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            user = request.user
            if not user.is_authenticated:
                # Not logged in, send to admin login page
                return redirect(reverse('admin:login'))
            # Check if user is admin based on your custom role or default flags
            if not (user.is_superuser or (hasattr(user, 'role') and user.role == 'admin')):
                # Block non-admin, non-superuser users
                return redirect('/')
        return self.get_response(request)
