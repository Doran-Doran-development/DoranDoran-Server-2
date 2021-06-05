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
        self.fixture_user = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.fixture_profile = mommy.make(
            "users.StudentProfile", user_id=self.fixture_user.id
        )
        payload = jwt_payload_handler(self.fixture_user)
        self.valid_token = jwt_encode_handler(payload)

        self.fixture_escape = mommy.make(
            "escapes.EscapeQueue", applicant_id=self.fixture_user
        )

    @abc.abstractmethod
    def test_create_escapes_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.valid_token}

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

        header = {"HTTP_AUTHORIZATION": "jwt " + self.valid_token}

        response = self.client.get(
            "/escapes/",
            **header,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)