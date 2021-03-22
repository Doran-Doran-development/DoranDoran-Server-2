"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_url_patterns = [
    path("users", include("users.urls")),
    path("reservations", include("reservations.urls")),
    path("rooms", include("rooms.urls")),
    path("teams", include("teams.urls")),
    path("escapes", include("escapes.urls")),
]


schema_view = get_schema_view(
    openapi.Info(
        title="DoranDoran2 API",
        default_version="v2",
        description="GSM 학생 이동관리 웹 서비스 DoranDoran의 API 문서입니다.",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(name="woungsub1234@gmail.com"),
        license=openapi.License(name="DoranDoran"),
    ),
    patterns=schema_url_patterns,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path(
            "swagger<str:format>",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
urlpatterns += schema_url_patterns
