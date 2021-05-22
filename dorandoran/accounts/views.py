from rest_framework import generics, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.encoding import force_text
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from .serializers import ObtainTokenSerializer
from users.serializers import UserSerializer
from core.email_verification import account_activation_token


UserModel = get_user_model()


class ObtainTokenView(generics.GenericAPIView):
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        response_data = serializer.validated_data
        response = Response(response_data)
        return response


class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
        except ValueError:
            raise exceptions.APIException(detail="Invalid uidb64", code=400)

        user = UserModel.objects.get(id=uid)

        if not user:
            raise exceptions.APIException(detail="User does not exist", code=404)

        if not account_activation_token.check_token(user, token):
            raise exceptions.APIException(
                detail="Invalid account activation token", code=400
            )

        user.is_active = True
        user.save()
        response = Response(UserSerializer(user).data)
        return response
