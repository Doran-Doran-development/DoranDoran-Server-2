from rest_framework import generics
from .serializers import ObtainTokenSerializer
from rest_framework.response import Response


class ObtainTokenView(generics.GenericAPIView):
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=400)

        response_data = serializer.validated_data
        response = Response(response_data)
        return response
