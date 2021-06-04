from django.test import TestCase
from model_mommy import mommy
from accounts.utils import jwt_encode_handler, jwt_payload_handler
from users.enums import UserRole
from tests.reservations.base import BaseReservationAPITest


class ReservationAPITest(BaseReservationAPITest, TestCase):
    def prepare_fixture(self):
        self.fixture_user_student = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.fixture_user_student_2 = mommy.make(
            "users.User", role=UserRole.STUDENT.value, is_active=True
        )
        self.fixture_user_teacher = mommy.make(
            "users.User", role=UserRole.TEACHER.value, is_active=True
        )
        self.fixture_team = mommy.make(
            "teams.Team", applicant_id=self.fixture_user_student
        )
        self.fixture_team_member = mommy.make(
            "teams.TeamMember",
            team_id=self.fixture_team,
            member_id=self.fixture_user_student,
        )
        self.fixture_room = mommy.make("rooms.Room", owner_id=self.fixture_user_teacher)
        self.fixture_reservation = mommy.make(
            "reservations.ReservationQueue",
            room_id=self.fixture_room,
            team_id=self.fixture_team,
        )

        student_payload = jwt_payload_handler(self.fixture_user_teacher)
        teacher_payload = jwt_payload_handler(self.fixture_user_student)
        self.student_valid_token = jwt_encode_handler(student_payload)
        self.teacher_valid_token = jwt_encode_handler(teacher_payload)

    def test_create_reservation_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_valid_token}
        payload = {
            "time": [8, 9, 10, 11],
            "description": "2021주소창대회참여를 위해 홈베이스[1]실을 대여합니다",
            "team_id": self.fixture_team.id,
        }
        # when
        response = self.client.post(
            "/reservations/{}".format(self.fixture_room.id),
            **header,
            data=payload,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 201)

    def test_create_reservation_permission_fail(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.teacher_valid_token}
        payload = {
            "time": [8, 9, 10, 11],
            "description": "2021주소창대회참여를 위해 홈베이스[1]실을 대여합니다",
            "team_id": self.fixture_team.id,
        }
        # when
        response = self.client.post(
            "/reservations/{}".format(self.fixture_room.id),
            **header,
            data=payload,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 401)

    def test_retrieve_reservation_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_valid_token}
        # when
        response = self.client.get(
            "/reservations/my",
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 200)

    def test_list_reservation_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_valid_token}
        # when
        response = self.client.get(
            "/reservations?room_id={}".format(self.fixture_room.id),
            **header,
            content_type="application/json",
        )

    def test_accept_reservation_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.teacher_valid_token}
        # when
        response = self.client.patch(
            "/reservations/{}/accept".format(self.fixture_reservation.id),
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 204)

    def test_accept_reservation_permission_fail(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_valid_token}
        # when
        response = self.client.patch(
            "/reservations/{}/accept".format(self.fixture_reservation.id),
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 401)

    def test_deny_reservation_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.teacher_valid_token}
        # when
        response = self.client.patch(
            "/reservations/{}/deny".format(self.fixture_reservation.id),
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 204)

    def test_deny_reservation_permission_fail(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.student_valid_token}
        # when
        response = self.client.patch(
            "/reservations/{}/deny".format(self.fixture_reservation.id),
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 401)

    def test_cancel_reservation_success(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.teacher_valid_token}

        # when
        response = self.client.delete(
            "/reservations/{}".format(self.fixture_reservation.id),
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 202)

    def test_cancel_reservation_permission_fail(self):
        # given
        header = {"HTTP_AUTHORIZATION": "jwt " + self.fixture_user_student_2}

        # when
        response = self.client.delete(
            "/reservations/{}".format(self.fixture_reservation.id),
            **header,
            content_type="application/json",
        )
        # then
        self.assertEqual(response.status_code, 401)