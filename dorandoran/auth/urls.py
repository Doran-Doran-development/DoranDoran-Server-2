from .views import ObtainTokenView, ActivateAccountView
from django.urls import path


urlpatterns = [
    path("/login", ObtainTokenView.as_view()),
    path("/activate", ActivateAccountView.as_view()),
]
