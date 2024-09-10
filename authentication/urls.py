"""
URL configuration for the Authentication app.
Most of the URLs are already provided by Django built-in URLs.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup/confirmation", views.SignUpConfirmationView.as_view(), name="signup_confirmation"),
    # Password reset
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # Password change
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
]