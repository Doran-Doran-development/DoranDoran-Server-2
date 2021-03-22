from django.db import models
from django.conf import settings

STATUS_CHOICES = getattr(settings, "STATUS_CHOICES")


class ReservationQueue(models.Model):

    id = models.AutoField(primary_key=True, db_column="id")
    team_id = models.ForeignKey(
        "teams.Team", on_delete=models.CASCADE, db_column="team_id"
    )
    room_id = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, db_column="room_id"
    )
    time = models.IntegerField()
    date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, null=False, default=3
    )
    description = models.CharField(max_length=256)
