from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from django.test import Client
from model_mommy import mommy
from users.enums import UserRole
from accounts.utils import jwt_encode_handler, jwt_payload_handler
import abc


class BaseUserAPITest:
    def setUp(self):
        self.client = Client()
        self.prepare_fixture()

    @abc.abstractclassmethod
    def prepare_fixture(self):
        pass

    @abc.abstractclassmethod
    def test_create_user_success(self):
        pass

    @abc.abstractclassmethod
    def test_retrieve_user_success(self):
        pass

    @abc.abstractclassmethod
    def test_list_user_success(self):
        pass

    @abc.abstractclassmethod
    def test_delete_user_success(self):
        pass


class StudentAPITest(BaseUserAPITest, TestCase):
    def prepare_fixture(self):
        self.fixture_user = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.fixture_profile = mommy.make("users.StudentProfile", user_id=self.fixture_user.id)
        payload = jwt_payload_handler(self.fixture_user)
        self.valid_token = jwt_encode_handler(payload)


    def test_create_user_success(self):
        # given
        payload = {
            "user": {
                "email": "student1@example.com",
                "password": "1234",
                "name": "student1",
            },
            "entrance_year": 2021,
            "grade": 1,
            "classroom": 1,
            "number": 1,
        }
        # when
        response = self.client.post(
            "/users/student",
            data=payload,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 201)

    def test_retrieve_user_success(self):
        # when
        response = self.client.get(
            f"/users/student/{self.fixture_profile.user_id}",
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 200)

    def test_list_user_successful(self):
        # when
        response = self.client.get(
            "/users/student",
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 200)

    def test_delete_user_successful(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.valid_token}
        # when
        response = self.client.delete(
            f"/users/student/{self.fixture_profile.user_id}",
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 204)

    def test_delete_user_permission_fail(self):
        # given
        # when
        response = self.client.delete(
            f"/users/student/{self.fixture_profile.user_id}",
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 401)

