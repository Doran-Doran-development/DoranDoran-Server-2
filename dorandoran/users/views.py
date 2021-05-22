from rest_framework import mixins, viewsets
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes
from core.email_verification import account_activation_token
from .models import TeacherProfile, StudentProfile
from .serializers import (
    TeacherProfileSerializer,
    StudentProfileSerializer,
)


class BaseProfileViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    lookup_field = "user_id"

    def perform_create(self, serializer):
        user_instance = serializer.save()
        current_site = get_current_site(self.request)

        html_message = render_to_string(
            "email/email-verification.html",
            {
                "user": user_instance.user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user_instance.user.pk)),
                "token": account_activation_token.make_token(user_instance.user),
            },
        )

        send_mail(
            subject="도란도란 계정 이메일 인증 요청",
            message=strip_tags(html_message),
            html_message=html_message,
            from_email=None,
            recipient_list=[user_instance.user.email],
            fail_silently=False,
        )


class TeacherProfileViewSet(BaseProfileViewSet):
    queryset = TeacherProfile.objects.select_related("user").all()
    serializer_class = TeacherProfileSerializer


class StudentProfileViewSet(BaseProfileViewSet):
    queryset = StudentProfile.objects.select_related("user").all()
    serializer_class = StudentProfileSerializer
