from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250, null=True)
    applicant_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="applicant_id"
    )


class TeamMember(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    team_id = models.ForeignKey("Team", on_delete=models.CASCADE, db_column="team_id")
    member_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column="member_id"
    )

    class Meta:
        unique_together = (
            "team_id",
            "member_id",
        )
