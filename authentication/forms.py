from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as authForms

UserModel = get_user_model()

"""
Form to add email field to built-in Django UserCreation Form.
"""
class SignUpForm(authForms.UserCreationForm):
    email = forms.EmailField(label=("Email address"), required=True)
    # Set max length of a username to 15 characters
    UserModel._meta.get_field('username').validators[1].limit_value = 15

    def __init__(self, *args, **kwargs):
        super(authForms.UserCreationForm, self).__init__(*args, **kwargs)
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
class LoginForm(authForms.AuthenticationForm):
    username = forms.CharField(label='Email / Username')




# --- PASSWORD RESET ---

"""
Update label on the password reset form and add placeholder text to the field.
"""
class PasswordResetForm(authForms.PasswordResetForm):
    email = forms.EmailField(label="Email address")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholder text
        self.fields['email'].widget.attrs.update({'placeholder':'Enter your email address'})



"""
Remove help text on the password reset confirm form.
"""
class SetPasswordForm(authForms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for all fields
        for field in ['new_password1', 'new_password2']:
            self.fields[field].help_text = None




# --- PASSWORD CHANGE ---

"""
Remove help text on the password change form fields.
"""
class PasswordChangeForm(authForms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for all fields
        for field in ['old_password', 'new_password1', 'new_password2']:
            self.fields[field].help_text = None