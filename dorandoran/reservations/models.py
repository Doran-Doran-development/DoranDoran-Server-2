from django.db import models


class ReservationQueue(models.Model):
    ACCEPTED = 1
    DENIED = 2
    WAITING = 3
    EXPIRED = 4

    STATUS_CHOICES = {
        (ACCEPTED, "accepted"),
        (DENIED, "denied"),
        (WAITING, "waiting"),
        (EXPIRED, "expired"),
    }  # TODO : base.py 에서 처리하도록 하자

    team_id = models.ForeignKey(
        "teams.Team", on_delete=models.CASCADE, db_column="post_id"
    )
    room_id = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, db_column="post_id"
    )
    time = models.IntegerField()
    date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    description = models.CharField(max_length=256)
