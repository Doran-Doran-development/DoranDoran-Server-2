import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = None
    last_login = None
    last_name = None
    username = None
    is_staff = None
    is_superuser = None
    groups = None
    user_permissions = None

    STUDENT = 1
    TEACHER = 2
    ADMIN = 3

    ROLE_CHOICES = {
        (STUDENT, "student"),
        (TEACHER, "teacher"),
        (ADMIN, "admin"),
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column="id")
    name = models.CharField(_("real name"), max_length=150, default="unknown")
    email = models.EmailField(_("email address"), unique=True, max_length=128)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)


class StudentProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column="user_id")
    entrance_year = models.IntegerField()
    classroom = models.IntegerField(null=False, default=0)
    number = models.IntegerField(null=False, default=0)


class TeacherProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column="user_id")
    classroom = models.IntegerField(null=True)
    grade = models.IntegerField(null=True)
