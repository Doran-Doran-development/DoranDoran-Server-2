from rest_framework import serializers
from .models import EscapeQueue


class EscapeQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscapeQueue
        fields = "__all__"
