from django.db import models
from dorandoran.users.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Status(models.Model):
    ACCEPTED = 1
    DENIED = 2
    WAITING = 3
    LATED = 4

    STATUS_CHOICES = {
        (ACCEPTED, "accepted"),
        (DENIED, "denied"),
        (WAITING, "waiting"),
        (LATED, "lated"),
    }

    id = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Escape(models.Model):
    id = models.AutoField(primary_key=True)
    applyer_id = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="applyer_id"
    )
    reason = models.CharField(_("reason"), max_length=100, null=False, default="reason")
    status = models.ManyToManyField(Status)
    start_at = models.DateTimeField(_("start time"))
    end_at = models.DateTimeField(_("end time"))

    class Meta:
        db_table = u"Escape"

    def __str__(self):
        return self.id, self.applyer_id
