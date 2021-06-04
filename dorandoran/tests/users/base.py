from django.test import Client
import abc


class BaseUserAPITest:
    def setUp(self):
        self.client = Client()
        self.prepare_fixture()

    @abc.abstractmethod
    def prepare_fixture(self):
        pass

    @abc.abstractmethod
    def test_create_user_success(self):
        pass

    @abc.abstractmethod
    def test_retrieve_user_success(self):
        pass

    @abc.abstractmethod
    def test_list_user_success(self):
        pass

    @abc.abstractmethod
    def test_delete_user_success(self):
        pass
