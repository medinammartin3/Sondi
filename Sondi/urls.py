"""
Root URL configuration for Sondi, routing to app-specific URL configurations.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("home.urls")),
    path("polls/", include("polls.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]