from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .serializers import EscapeQueueSerializer
from .models import EscapeQueue


class EscapeViewSet(viewsets.ViewSet):
    def create(self, request):

        obj = {
            "applicant_id": request.user.id
            "reason": request.data["reason"],
            "start_at": request.data["start_at"],
            "end_at": request.data["end_at"],
        }
        serializer = EscapeQueueSerializer(data=obj)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)