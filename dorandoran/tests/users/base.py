from django.test import Client
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
