from .models import User, TeacherProfile, StudentProfile, TeacherCertificationCode
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id", "is_active", "date_joined", "role")
        extra_kwargs = {"password": {"write_only": True}}


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    certification_code = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = TeacherProfile
        fields = "__all__"
        read_only_fields = ("id", "user")

    def create(self, validated_data):
        available_code = TeacherCertificationCode.objects.filter(
            certification_code=validated_data["certification_code"], is_active=1
        )
        if not available_code.exists():
            raise serializers.ValidationError(
                "certification code does not exist or already used"
            )

        available_code.update(is_active=0)
        del validated_data["certification_code"]

        user_instance = User.objects.create_teacher(**validated_data["user"])
        validated_data["user"] = user_instance
        teacher_instance = TeacherProfile.objects.create(**validated_data)
        return teacher_instance

    def validate(self, attrs):
        return attrs


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = StudentProfile
        fields = "__all__"
        read_only_fields = ("id", "user")

    def create(self, validated_data):
        user_instance = User.objects.create_student(**validated_data["user"])
        validated_data["user"] = user_instance
        student_instance = StudentProfile.objects.create(**validated_data)
        return student_instance

    def validate(self, attrs):
        return attrs
