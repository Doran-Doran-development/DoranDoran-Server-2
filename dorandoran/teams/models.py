from django.db import models

# Create your models here.
class Team(models.Model) :
    team_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250,null=True)
    # reserver_id
