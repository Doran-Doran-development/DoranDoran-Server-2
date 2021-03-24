import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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

    def create_student(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", UserRole.STUDENT.value)
        return self.create_user(email=email, password=password, **extra_fields)

    def create_teacher(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", UserRole.TEACHER.value)
        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser):
    objects = UserManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column="id")
    name = models.CharField(_("real name"), max_length=150, default="unknown")
    email = models.EmailField(_("email address"), unique=True, max_length=128)
    role = models.PositiveSmallIntegerField(choices=UserRole.choices())
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        db_column="user_id",
        primary_key=True,
    )
    entrance_year = models.IntegerField()
    classroom = models.IntegerField(null=False, default=0)
    number = models.IntegerField(null=False, default=0)


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        db_column="user_id",
        primary_key=True,
    )
    classroom = models.IntegerField(null=True)
    grade = models.IntegerField(null=True)


class TeacherCertificationCode(models.Model):
    certification_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
