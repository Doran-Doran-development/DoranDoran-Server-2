from django.test import Client
from abc import abstractmethod


class BaseReservationAPITest:
    def setUp(self):
        self.client = Client()
        self.prepare_fixture()

    @abstractmethod
    def prepare_fixture(self):
        pass

    @abstractmethod
    def test_create_reservation_success(self):
        pass

    @abstractmethod
    def test_retrieve_my_reservation_success(self):
        pass

    @abstractmethod
    def test_list_reservation_success(self):
        pass

    @abstractmethod
    def test_accept_reservation_success(self):
        pass

    @abstractmethod
    def test_deny_reservation_success(self):
        pass

    @abstractmethod
    def test_cancel_reservation_success(self):
        pass
