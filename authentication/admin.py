from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from polls.models import Question
from django.contrib.auth.models import Group



"""
Inline for displaying all questions created by the user.
"""
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ('question_text',)
    readonly_fields = ('question_text',)
    can_delete = False
    show_change_link = True # Add the link to each question


"""
Display CustomUser model on the Django admin site.
"""
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    readonly_fields = ("id",)
    # Fields to display in the list view
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')
    ordering = ['id']
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('id', 'username', 'email')
    # Fields to display in the detail view
    fieldsets = (
        (None, {'fields': ('id', 'username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [QuestionInline]


admin.site.register(CustomUser, CustomUserAdmin)
# Hide Groups section on Django admin site
admin.site.unregister(Group)