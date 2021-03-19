from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeacherProfileViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"teacher", TeacherProfileViewSet)

urlpatterns = [
    path("/", include(router.urls)),
]
