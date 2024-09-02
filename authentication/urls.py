"""
URL configuration for the Authentication app.
Most of the URLs are already provided by Django built-in URLs.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
]