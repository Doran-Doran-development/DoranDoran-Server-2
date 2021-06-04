from django.test import TestCase
from model_mommy import mommy
from dorandoran.accounts.utils import jwt_encode_handler, jwt_payload_handler
from users.enums import UserRole
from tests.reservations.base import BaseReservationAPITest


class ReservationAPITest(BaseReservationAPITest, TestCase):
    def prepare_fixture(self):
        self.fixture_user = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.fixture_teacher = mommy.make(
            "users.User", role=UserRole.TEACHER.value, is_active=True
        )
        self.fixture_team = mommy.make("teams.Team", applicant_id=self.fixture_user)
        self.fixture_team_member = mommy.make(
            "teams.TeamMember",
            team_id=self.fixture_team,
            member_id=self.fixture_user,
        )
        self.fixture_room = mommy.make("rooms.Room", owner_id=self.fixture_teacher)
        self.fixture_reservation = mommy.make(
            "reservations.ReservationQueue",
            room_id=self.fixture_room,
            team_id=self.fixture_team,
        )
        payload = jwt_payload_handler(self.fixture_user)
        self.valid_token = jwt_encode_handler(payload)
