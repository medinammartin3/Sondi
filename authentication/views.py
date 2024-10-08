"""
Views for the Authentication system. 
Most of the views are already provided by Django built-in views.
"""

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, LoginForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm


"""
View for new user sign-up.
"""
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("signup_confirmation")
    template_name = "registration/signup.html"



"""
View for new user sign-up.
"""
class SignUpConfirmationView(generic.TemplateView):
    template_name = "registration/signup_confirmation.html"



"""
View for user log-in.
"""
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"



# --- PASSWORD RESET ---

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



# --- PASSWORD CHANGE ---

"""
View for password change form.
"""
class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/password_change_form.html"