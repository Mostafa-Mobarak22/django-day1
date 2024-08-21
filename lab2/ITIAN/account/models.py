from django.db import models
from trainee.models import *
from track.models import *
# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class AccountTrainee(models.Model):
    traineeobject = models.ForeignKey('trainee.Trainee',on_delete=models.CASCADE)
    accountobject = models.ForeignKey('Account', on_delete=models.CASCADE)

class AccountTrack(models.Model):
    trackobject = models.ForeignKey('track.Track',on_delete=models.CASCADE)
    accountobject = models.ForeignKey('Account', on_delete=models.CASCADE)