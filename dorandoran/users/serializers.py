from .models import User, TeacherProfile, StudentProfile, TeacherCertificationCode
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id", "is_active", "date_joined", "role")
        extra_kwargs = {
            "password": {"write_only": True, "help_text": "유저의 비밀번호 ex) 0128gksqls!"},
            "id": {
                "help_text": "유저의 ID (UUID) ex) 144e0ca5-e506-4c6e-b2c5-ff2cb1c4b888"
            },
            "name": {"help_text": "유저의 이름 ex) 정한빈"},
            "email": {"help_text": "유저의 이메일 ex) hanbin8269@gmail.com"},
            "role": {
                "help_text": "유저의 권한 정보 ex) 1 (1, 'student'),(2, 'teacher'),(3, 'admin')"
            },
            "is_active": {"help_text": "활성화 된 유저인지 확인 (이메일 인증 여부) ex) 1"},
            "last_login": {
                "help_text": "유저가 최근에 로그인 한 시간 ex) 2021-06-18T02:01:59.856000Z"
            },
        }


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    certification_code = serializers.CharField(
        required=True, write_only=True, help_text="미리 발급했던 선생님 인증 코드 ex) etwitwiewt"
    )

    class Meta:
        model = TeacherProfile
        fields = "__all__"
        read_only_fields = ("id", "user")
        extra_kwargs = {
            "classroom": {"help_text": "선생님이 담당하는 반 정보 ex) 2"},
            "grade": {"help_text": "선생님이 담당하는 학년 번호 ex) 1"},
        }

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
        extra_kwargs = {
            "entrance_year": {"help_text": "유저의 입학년도 ex) 2019"},
            "classroom": {"help_text": "유저의 반 ex) 2"},
            "number": {"help_text": "유저의 번호 ex) 16"},
        }

    def create(self, validated_data):
        user_instance = User.objects.create_student(**validated_data["user"])
        validated_data["user"] = user_instance
        student_instance = StudentProfile.objects.create(**validated_data)
        return student_instance

    def validate(self, attrs):
        return attrs
