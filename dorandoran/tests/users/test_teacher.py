from django.test import TestCase
from model_mommy import mommy
from users.enums import UserRole
from accounts.utils import jwt_encode_handler, jwt_payload_handler
from tests.users.base import BaseUserAPITest


class TeacherAPITest(BaseUserAPITest, TestCase):
    def prepare_fixture(self):
        self.fixture_user = mommy.make(
            "users.User", role=UserRole.TEACHER.value, is_active=True
        )
        self.fixture_profile = mommy.make(
            "users.TeacherProfile", user_id=self.fixture_user.id
        )
        self.fixture_certification_code = mommy.make("users.TeacherCertificationCode")
        payload = jwt_payload_handler(self.fixture_user)
        self.token = jwt_encode_handler(payload)

    def test_create_user_success(self):
        # given
        payload = {
            "user": {
                "email": "teacher1@example.com",
                "password": "1234",
                "name": "teacher1",
            },
            "entrance_year": 2021,
            "grade": 1,
            "classroom": 1,
            "number": 1,
            "certification_code": self.fixture_certification_code.certification_code,
        }
        # when
        response = self.client.post(
            path="/users/teacher",
            data=payload,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 201)

    def test_create_user_certification_code_fail(self):
        # given
        payload = {
            "user": {
                "email": "teacher1@example.com",
                "password": "1234",
                "name": "teacher1",
            },
            "entrance_year": 2021,
            "grade": 1,
            "classroom": 1,
            "number": 1,
            "certification_code": self.fixture_certification_code.certification_code
            + "NOISE",
        }
        # when
        response = self.client.post(
            path="/users/teacher",
            data=payload,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 400)

    def test_retrieve_user_success(self):
        # when
        response = self.client.get(
            path=f"/users/teacher/{self.fixture_profile.user_id}",
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 200)

    def test_list_user_successful(self):
        # when
        response = self.client.get(
            path="/users/teacher",
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 200)

    def test_delete_user_successful(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.token}
        # when
        response = self.client.delete(
            path=f"/users/teacher/{self.fixture_profile.user_id}",
            content_type="application/json",
            **header,
        )
        # then
        self.assertEqual(response.status_code, 204)

    def test_delete_user_permission_fail(self):
        # given
        # when
        response = self.client.delete(
            path=f"/users/teacher/{self.fixture_profile.user_id}",
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 401)
