from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status
from django.core import serializers

from .serializers import EscapeQueueSerializer
from .models import EscapeQueue
from users.models import User, StudentProfile

from datetime import datetime


class EscapeViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    def create(self, request, *args, **kwargs):

        obj = {
            "applicant_id": request.user.id,
            "reason": request.data["reason"],
            "start_at": request.data["start_at"],
            "end_at": request.data["end_at"],
        }

        serializer = EscapeQueueSerializer(data=obj)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):

        grade = request.GET.get("grade", None)
        classroom = request.GET.get("classroom", None)

        users = StudentProfile.objects.select_related("user").all()

        if grade != None:
            entrance_year = datetime.today().year + 1 - int(grade)
            users = users.filter(entrance_year=entrance_year)
        if classroom != None:
            users = users.filter(classroom=int(classroom))

        user_id = []

        for user in users:
            user_id.append(user.pk)

        escapes = EscapeQueue.objects.select_related("applicant_id").filter(
            applicant_id__in=user_id
        )

        result = []

        for escape in escapes:
            obj = {
                "id": escape.id,
                "name": escape.applicant_id.name,
                "reason": escape.reason,
                "start_at": escape.start_at,
                "end_at": escape.end_at,
                "status": escape.status,
            }
            result.append(obj)

        return Response(result, status=200)
