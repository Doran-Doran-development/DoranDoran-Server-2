from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.0", "localhost"]

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
