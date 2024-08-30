"""
Views for the Authentication system. 
Most of the views are already provided by Django built-in views.
"""

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, LoginForm


"""
View for new user sign-up.
"""
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"



"""
View for user log-in.
"""
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "authentication/login.html"
