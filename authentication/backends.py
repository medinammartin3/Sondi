from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()

"""
Override Django's default authentication backend to allow 
users to log-in using either their username or email address.
"""
class EmailBackend(ModelBackend):
    # Authenticate a user based on the given username
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Find a user from the database where either the username or email matches
            # the text provided on the `username` field, ignoring case (iexact).
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))

        # If no user matches the query
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user
            # (taken from Django source code)
            UserModel().set_password(password)
            return

        # If more than one user matches the query
        except UserModel.MultipleObjectsReturned:
            # Retrieve the first user from the filtered queryset
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        # Check the password and if the user is `active` 
        if user.check_password(password) and self.user_can_authenticate(user):
            return user # Successful authentication