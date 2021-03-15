from django.db import models

# Create your models here.
class Team(models.Model) :
    team_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250,null=True)
    reserver_id = models.ForeignKey("users.StudentProfile", on_delete=models.CASCADE)

class TeamMember(models.Model) :
    team_id = models.ForeignKey("Team",on_delete=models.CASCADE)
    member_id = models.FOreignKey("users.StutdentProfile",on_delete=models.CASCADE)
    class Meta:
        unique_together = ('team_id','member_id',)