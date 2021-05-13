"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import sys
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + "/dorandoran")
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
load_dotenv()
application = get_asgi_application()
