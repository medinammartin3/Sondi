from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()

"""
Form to add email field to built-in Django UserCreation Form.
"""
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=("Email address"), required=True)
    # Set max length of a username to 15 characters
    UserModel._meta.get_field('username').validators[1].limit_value = 15

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # Remove help text for all fields
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2")

    

"""
Update the label on the login form to indicate 
that users can log in using either their email or username.
"""
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')