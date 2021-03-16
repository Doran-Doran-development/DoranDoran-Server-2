from django.db import models

# Create your models here.
class rooms(models.Model):
    room_id = models.AutoField(primary_key=True, db_column="room_id")
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    capacity = models.IntegerField()
    description = models.TextField(null=True)
    image = models.CharField(max_length=255, null=True)
    available_time = models.CharField(max_length=50, null=True)
