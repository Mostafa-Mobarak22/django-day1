from django.db import models
from track.models import *
# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    trackobject = models.ForeignKey('track.Track',on_delete=models.CASCADE)
