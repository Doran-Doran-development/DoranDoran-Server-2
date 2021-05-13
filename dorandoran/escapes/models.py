from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

STATUS_CHOICES = getattr(settings, "STATUS_CHOICES")


class EscapeQueue(models.Model):

    id = models.AutoField(primary_key=True, db_column="id")
    applicant_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="applicant_id"
    )
    reason = models.CharField(_("reason"), max_length=100, null=False, default="reason")
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, null=False, default=3
    )
    start_at = models.DateTimeField(_("start time"))
    end_at = models.DateTimeField(_("end time"))

    class Meta:
        db_table = u"escape_queue"

    def __str__(self):
        return self.id, self.applicant_id
