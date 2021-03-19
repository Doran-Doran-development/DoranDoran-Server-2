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

        self.escapes_form = {
            "reason": "발목이 다쳤습니다",
            "start_at": "2021- 03-09:13",
            "end_at": "2021-03-09:",
        }

        def tearDown(self):
            User.objects.all().delete()
            StudentProfile.objects.all().delete()
            EscapeQueue.objects.all().delete()

        def test_apply_escapes_success(self):
            response = client.post(
                "/escapes/",
                self.escapes_form,
                content_type="application/json",
                HTTP_AUTHORIZATION="jwt " + self.token,
            )

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)