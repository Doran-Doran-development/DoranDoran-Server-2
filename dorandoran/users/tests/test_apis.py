from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_teacher_successful(self):
        # given
        payload = {
            "user": {"email": "teacher1@example.com", "password": "1234"},
            "grade": 1,
            "classroom": 1,
        }
        # when
        response = self.client.post("/users/", payload, format="json")
        # then
        self.assertEqual(response.status_code, 201)
