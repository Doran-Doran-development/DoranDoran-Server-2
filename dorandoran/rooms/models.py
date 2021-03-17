from django.db import models


class Room(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    room_id = models.AutoField(primary_key=True, db_column="room_id")
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, db_column="owner_id"
    )
    status = models.BooleanField(default=False)
    capacity = models.IntegerField()
    description = models.TextField(null=True)
    image = models.CharField(max_length=255, null=True)
    available_time = models.CharField(max_length=50, null=True)
