"""
Views for the Authentication system. 
Most of the views are already provided by Django built-in views.
"""

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, LoginForm, PasswordResetForm, SetPasswordForm


"""
View for new user sign-up.
"""
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



"""
View for user log-in.
"""
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"



"""
View for password reset email form.
"""
class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    template_name = "registration/password_reset_form.html"



"""
View for password reset confirm form.
"""
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = "registration/password_reset_confirm.html"