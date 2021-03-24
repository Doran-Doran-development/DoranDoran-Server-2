from .views import ObtainTokenView
from django.urls import path


urlpatterns = [path("/login", ObtainTokenView.as_view())]
