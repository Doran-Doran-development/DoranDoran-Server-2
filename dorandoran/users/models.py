import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3

    ROLE_CHOICES = {
        (STUDENT, "student"),
        (TEACHER, "teacher"),
        (ADMIN, "admin"),
    }

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    first_name = None
    last_login = None
    last_name = None
    username = None
    is_staff = None
    is_superuser = None
    groups = None
    user_permissions = None

    user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_column="user_id"
    )

    name = models.CharField(_("real name"), max_length=150, default="unknown")

    email = models.EmailField(_("email address"), unique=True, max_length=128)

    role = models.ManyToManyField(Role)
