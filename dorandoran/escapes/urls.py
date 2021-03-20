from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EscapeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"", EscapeViewSet, basename="escapes")

urlpatterns = [
    path("", include(router.urls)),
]