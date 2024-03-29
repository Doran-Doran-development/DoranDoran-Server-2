import os
import dj_database_url
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
