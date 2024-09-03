"""
Admin site configuration for displaying and managing polls.
"""

from django.contrib import admin

from .models import Choice, Question


"""
Inline for displaying all choices associated with a question.
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


"""
Display Question model on the Django admin site.
"""
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "owner", "code")
    fieldsets = [
        ("Question", {"fields": ["id", "owner", "code", "visibility", "question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["id", "owner", "code", "visibility", "question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["code", "owner", "question_text"]

admin.site.register(Question, QuestionAdmin)