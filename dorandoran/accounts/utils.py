import jwt

from datetime import datetime, timedelta
from calendar import timegm
from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def jwt_encode_handler(payload):
    key = settings.JWT_AUTH["JWT_SECRET_KEY"]
    algorithm = settings.JWT_AUTH["JWT_ALGORITHM"]

    return jwt.encode(dict(payload), key, algorithm).decode("utf-8")


def jwt_decode_handler(token):
    key = settings.JWT_AUTH["JWT_SECRET_KEY"]
    algorithm = settings.JWT_AUTH["JWT_ALGORITHM"]
    return jwt.decode(token, key, algorithm)


def jwt_payload_handler(user):
    expiration_time = datetime.utcnow() + settings.JWT_AUTH["JWT_EXPIRATION_DELTA"]
    payload = {
        "exp": timegm(expiration_time.utctimetuple()),
        "user_id": str(user.id),
        "email": user.email,
        "is_active": user.is_active,
        "name": user.name,
        "role": user.role,
    }

    if settings.JWT_AUTH["JWT_ALLOW_REFRESH"]:
        payload["iat"] = timegm(datetime.utcnow().utctimetuple())
    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    return {"user": user, "token": token}


def jwt_get_username_from_payload_handler(payload):
    return payload.get(UserModel.USERNAME_FIELD)
