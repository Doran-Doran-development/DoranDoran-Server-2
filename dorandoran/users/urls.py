from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeacherProfileViewSet, StudentProfileViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"teacher", TeacherProfileViewSet)
router.register(r"student", StudentProfileViewSet)

urlpatterns = [
    path("/", include(router.urls)),
]
