from rest_framework import serializers
from rest_framework.exceptions import APIException
from users.serializers import UserSerializer
from django.contrib.auth import authenticate
from .utils import jwt_payload_handler, jwt_encode_handler, jwt_response_payload_handler


class ObtainTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(max_length=256, required=True, write_only=True)

    token = serializers.CharField(max_length=256, read_only=True)
    user = UserSerializer(read_only=True)

    def validate(self, attrs):
        credentials = {
            "email": attrs.get("email", None),
            "password": attrs.get("password", None),
        }
        user = authenticate(**credentials)
        if user is None:
            raise APIException(detail="Can't find user instance", code=400)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return jwt_response_payload_handler(user=UserSerializer(user).data, token=token)
