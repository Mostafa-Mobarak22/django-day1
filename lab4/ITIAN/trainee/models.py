from audioop import reverse
from django.shortcuts import render,redirect
from django.db import models
from django.urls import reverse
from track.models import *
# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='trainee/images', blank=True, null=True)
    trackobject = models.ForeignKey('track.Track',on_delete=models.CASCADE)
    @staticmethod
    def get_url():
       return reverse('list_trainee')

    @classmethod
    def delete(cls,id):
        cls.objects.filter(pk=id).delete()
        return redirect(cls.get_url())


    @classmethod
    def create(cls,name,image,trackid):
        traineeobject = Trainee()
        traineeobject.name = name
        traineeobject.trackobject = Track.objects.get(pk=trackid)
        traineeobject.img = image
        traineeobject.save()
        return redirect(cls.get_url())

    # def create(cls,name,image,trackid):
    #     traineeobject = Trainee()
    #     traineeobject.name = name
    #     traineeobject.trackobject = Track.objects.get(pk=trackid)
    #     traineeobject.img = image
    #     traineeobject.save()
    #     cls.get_url()
    def getimage(self):
        return f'/media/{self.img}'