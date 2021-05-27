import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "users.User"

ROLE_CHOICES = (
    (1, "student"),
    (2, "teacher"),
    (3, "admin"),
)

STATUS_CHOICES = (
    (1, "accepted"),
    (2, "denied"),
    (3, "waiting"),
    (4, "expired"),
)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "drf_yasg",
    "rest_framework",
    "corsheaders",
    "escapes",
    "users",
    "rooms",
    "teams",
    "reservations",
    "accounts",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

AUTHENTICATION_BACKENDS = ["accounts.backends.UserBackend"]


REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "core.utils.custom_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

JWT_AUTH = {
    "JWT_ENCODE_HANDLER": "accounts.utils.jwt_encode_handler",
    "JWT_DECODE_HANDLER": "accounts.utils.jwt_decode_handler",
    "JWT_PAYLOAD_HANDLER": "accounts.utils.jwt_payload_handler",
    "JWT_PAYLOAD_GET_USERNAME_HANDLER": "accounts.utils.jwt_get_username_from_payload_handler",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "accounts.utils.jwt_response_payload_handler",
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": os.getenv("JWT_ALGORITHM"),
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": timedelta(days=30),
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
    "JWT_ALLOW_REFRESH": False,
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=30),
    "JWT_AUTH_HEADER_PREFIX": "jwt",
    "JWT_AUTH_COOKIE": None,
}

ROOT_URLCONF = "config.urls"

TEMPLATE_DIRS = [os.path.join(os.path.dirname(BASE_DIR), "templates")]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(os.path.dirname(BASE_DIR), "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, ".static")
