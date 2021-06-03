from django.test import Client
import abc


class BaseEscapeAPITest:
    def setUp(self):
        self.client = Client()
        self.prepare_fixture()

    @abc.abstractclassmethod
    def prepare_fixture(self):
        pass

    @abc.abstractclassmethod
    def test_create_escape_success(self):
        pass

    @abc.abstractclassmethod
    def test_list_escape_success(self):
        pass

    @abc.abstractclassmethod
    def test_accept_escape_success(self):
        pass

    @abc.abstractclassmethod
    def test_deny_escape_success(self):
        pass

    @abc.abstractclassmethod
    def test_delete_escape_success(self):
        pass
