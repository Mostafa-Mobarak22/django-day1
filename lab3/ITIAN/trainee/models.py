from django.db import models
from track.models import *
# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='trainee/images', blank=True, null=True)
    trackobject = models.ForeignKey('track.Track',on_delete=models.CASCADE)

    def getimage(self):
        return f'/media/{self.img}'