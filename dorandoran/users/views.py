from rest_framework import mixins, viewsets

from .models import User
from .serializers import UserSerializer, TeacherProfileSerializer


class TeacherProfileViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = TeacherProfileSerializer
    lookup_field = "id"
