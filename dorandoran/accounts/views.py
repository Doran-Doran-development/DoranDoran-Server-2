from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ObtainTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model

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
    def get(self, request, uid64, token):
        pass
