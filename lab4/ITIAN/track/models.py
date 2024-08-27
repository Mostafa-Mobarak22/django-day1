from distutils.command.upload import upload
from django.db import models
# Create your models here.
class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    @classmethod
    def get_all(cls):
        return [(track.id,track.name) for track in cls.objects.all()]
