from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from rest_framework import exceptions

UserModel = get_user_model()


class UserBackend(BaseBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            raise exceptions.ValidationError("No matching user found for email")
        
        if not user.check_password(password):
            raise exceptions.ValidationError("Incorrect password")
        
        if not self.user_can_authenticate(user):
            raise exceptions.ValidationError("This user is not active. Please verify your e-mail.")
        
        return user

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, "is_active", None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
