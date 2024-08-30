from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from django.contrib.auth.models import Group



"""
Display CustomUser model on the Django admin site.
"""
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields to display in the list view
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    # Fields to display in the detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
# Hide Groups section on Django admin site
admin.site.unregister(Group)