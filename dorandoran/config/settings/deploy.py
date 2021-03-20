import os
import dj_database_url
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["0.0.0.0"]
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
