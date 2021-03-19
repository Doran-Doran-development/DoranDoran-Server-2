from .models import User, TeacherProfile, StudentProfile
from rest_framework import serializers
from .enums import UserRole


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id", "is_active", "date_joined", "role")
        extra_kwargs = {"password": {"write_only": True}}


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = TeacherProfile
        fields = "__all__"
        read_only_fields = ("id", "user")

    def create(self, validated_data):
        # TODO 선생님 인증 코드 확인 절차 추가
        user_instance = User.objects.create_teacher(**validated_data["user"])
        validated_data["user"] = user_instance
        teacher_instance = TeacherProfile.objects.create(**validated_data)
        return teacher_instance

    def validate(self, attrs):
        return attrs
