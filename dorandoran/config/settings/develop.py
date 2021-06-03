import os
import dj_database_url
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DJANGO_DB_NAME"),
        "USER": os.getenv("DJANGO_DB_USERNAME"),
        "PASSWORD": os.getenv("DJANGO_DB_PASSWORD"),
        "HOST": os.getenv("DJANGO_DB_HOST"),
        "PORT": os.getenv("DJANGO_DB_PORT"),
    }
}
