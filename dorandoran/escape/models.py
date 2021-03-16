from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Escape(models.Model):
    STATUS_CHOICES = {
        (1, "accepted"),
        (2, "denied"),
        (3, "waiting"),
        (4, "expired"),
    }
    id = models.AutoField(primary_key=True, db_column="id")
    applyer_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="applyer_id"
    )
    reason = models.CharField(_("reason"), max_length=100, null=False, default="reason")
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, null=False, default=3
    )
    start_at = models.DateTimeField(_("start time"))
    end_at = models.DateTimeField(_("end time"))

    class Meta:
        db_table = u"Escape"

    def __str__(self):
        return self.id, self.applyer_id
