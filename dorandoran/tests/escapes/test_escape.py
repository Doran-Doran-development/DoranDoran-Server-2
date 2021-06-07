from django.http import response
from django.test import Client
import abc

from django.test import TestCase
from model_mommy import mommy
from users.enums import UserRole
from accounts.utils import jwt_encode_handler, jwt_payload_handler


class EscapeAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.prepare_fixture()

    @abc.abstractmethod
    def prepare_fixture(self):

        # student
        self.student_user = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.student_profile = mommy.make(
            "users.StudentProfile", user_id=self.student_user.id
        )
        payload = jwt_payload_handler(self.student_user)
        self.student_token = jwt_encode_handler(payload)

        # teacher
        self.teacher_user = mommy.make(
            "users.User", role=UserRole.TEACHER.value, is_active=True
        )
        self.teacher_profile = mommy.make(
            "users.TeacherProfile", user_id=self.teacher_user.id
        )
        self.fixture_certification_code = mommy.make("users.TeacherCertificationCode")
        payload = jwt_payload_handler(self.teacher_user)
        self.teacher_token = jwt_encode_handler(payload)

        # escape
        self.fixture_escape = mommy.make(
            "escapes.EscapeQueue", applicant_id=self.student_user
        )

    @abc.abstractmethod
    def test_create_escapes_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_token}

        payload = {
            "reason": "Example reason",
            "start_at": "2020-01-01 12:00:00",
            "end_at": "2020-01-01 13:00:00",
        }
        # when
        response = self.client.post(
            "/escapes",
            **header,
            data=payload,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 201)

    @abc.abstractmethod
    def test_list_escapes_success(self):

        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_token}

        response = self.client.get(
            "/escapes/",
            **header,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    @abc.abstractmethod
    def test_accept_escapes_success(self):

        header = {"HTTP_AUTHORIZATION": "jwt " + self.teacher_token}

        response = self.client.patch(
            "/escapes/{self.fixture_escape.id}/accept",
            **header,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    @abc.abstractmethod
    def test_deny_escapes_success(self):

        header = {"HTTP_AUTHORIZATION": "jwt " + self.teacher_token}

        response = self.client.patch(
            "/escapes/{self.fixture_escape.id}/deny",
            **header,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
