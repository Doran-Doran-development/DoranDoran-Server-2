import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from .enums import UserRole


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("must have user email")
        if not password:
            raise ValueError("must have user password")
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )  # name, role 정보
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = None
    last_login = None
    last_name = None
    username = None
    is_staff = None
    is_superuser = None
    groups = None
    user_permissions = None

    objects = UserManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column="id")
    name = models.CharField(_("real name"), max_length=150, default="unknown")
    email = models.EmailField(_("email address"), unique=True, max_length=128)
    role = models.PositiveSmallIntegerField(choices=UserRole.choices())

    USERNAME_FIELD = "id"
    EMAIL_FIELD = "email"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, db_column="user_id"
    )
    entrance_year = models.IntegerField()
    classroom = models.IntegerField(null=False, default=0)
    number = models.IntegerField(null=False, default=0)


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, db_column="user_id"
    )
    classroom = models.IntegerField(null=True)
    grade = models.IntegerField(null=True)
