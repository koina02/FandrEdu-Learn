from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Show in the admin user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_active', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    readonly_fields = ('last_login', 'date_joined')

    # Display role in user detail view
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Info', {'fields': ('role',)}),
    )

    # Add role during user creation (if superuser)
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Role Assignment', {
            'classes': ('wide',),
            'fields': ('role',),
        }),
    )

    # Lock role editing for non-superusers
    def get_readonly_fields(self, request, obj=None):
        fields = list(super().get_readonly_fields(request, obj))
        if not request.user.is_superuser:
            fields.append('role')
        return fields

