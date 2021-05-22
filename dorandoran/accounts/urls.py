from .views import ObtainTokenView, ActivateAccountView
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("/login", ObtainTokenView.as_view()),
    path(
        "/activate/<slug:uid64>/<slug:token>",
        ActivateAccountView.as_view(),
        name="activate",
    ),
]
