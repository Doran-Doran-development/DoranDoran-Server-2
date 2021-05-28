from django.test import Client
from model_mommy import mommy
from users.enums import UserRole
from accounts.utils import jwt_encode_handler, jwt_payload_handler
import abc


class BaseUserAPITest:
    def setUp(self):
        self.client = Client()
        self.fixture_student_user = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.fixture_profile = self.create_profile(self.fixture_student_user.id)

        payload = jwt_payload_handler(self.fixture_student_user)
        self.token = jwt_encode_handler(payload)

    @abc.abstractclassmethod
    def create_profile(self, user_id):
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
