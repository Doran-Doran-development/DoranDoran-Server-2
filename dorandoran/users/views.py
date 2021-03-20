from rest_framework import mixins, viewsets

from .models import User, TeacherProfile
from .serializers import UserSerializer, TeacherProfileSerializer


class TeacherProfileViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = TeacherProfile.objects.select_related("user").all()
    serializer_class = TeacherProfileSerializer
    lookup_field = "id"
