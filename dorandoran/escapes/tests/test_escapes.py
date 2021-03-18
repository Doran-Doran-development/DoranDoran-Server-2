from django.test import TestCase, Client
from rest_framework import status
from escapes.models import EscapeQueue
from users.models import User, StudentProfile, TeacherProfile
from django.contrib.auth.hashers import make_password

import uuid
import json

client = Client()


class ApplyEscape(TestCase):
    def setUp(self):

        student_id = uuid.uuid4

        user = {
            "id": student_id,
            "email": "student1@example.com",
            "name": "학생",
            "password": make_password("test1234"),
            "role": 1,
        }

        User.objects.create(**student)

        student = {
            "user_id": student_id,
            "entrance_year": 2019,
            "classroom": 1,
            "number": 1,
        }

        StudentProfile.objects.create(**student)

        user_login = {"email": "student1@example.com", "password": "test1234"}

        response = client.post(
            "auth/login", user_login, content_type="application/json"
        )

        self.token = response.json()["token"]