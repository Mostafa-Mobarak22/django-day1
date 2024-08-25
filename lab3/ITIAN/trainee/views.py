from lib2to3.fixes.fix_input import context
from django.shortcuts import render,redirect
import sys
from django.http import HttpResponse
from .models import *
from track.models import *
def show_trainee(req,id):
    trainees = Trainee.objects.get(pk=id)
    context={}
    context['trainees']=trainees
    return render(req,'show/show_trainee.html',context)
def list_trainee(req):
    trainees = Trainee.objects.all()
    context = {}
    context['trainees'] = trainees
    return render(req, 'listtrainee/list.html',context)
def update_trainee(req,id):
    context={}
    trainee_obj=Trainee.objects.get(pk=id)
    context['traineeobj']=trainee_obj
    context['trackobjs']=Track.objects.all()
    if(req.method=='POST'):
        if(len(req.POST['traineename'])>0 and len(req.POST['traineename'])<=50):
            Trainee.objects.filter(pk=id).update(name=req.POST['traineename'],trackobject=Track.objects.get(pk=req.POST['trackobj']))
            return redirect('list_trainee')
        else:
            context['error']="invalid trainee"
    return render(req, 'updatetrainee/update.html',context)
def delete_trainee(req,id):
    context={}
    try:
        Trainee.objects.filter(pk=id).delete()
        context['deleted'] = "trainee is deleted"
        return redirect('list_trainee')
    except:
        context['error'] = sys.exc_info()[1]
    return render(req, 'deletetrainee/delete.html',context)
def create_trainee(req):
    context = {}
    context['trackobjs']=Track.objects.all()
    if(req.method=='POST'):
        if(len(req.POST['traineename'])>0 and len(req.POST['traineename'])<=50):
            traineeobject = Trainee()
            traineeobject.name = req.POST['traineename']
            traineeobject.trackobject = Track.objects.get(pk=req.POST['trackobj'])
            traineeobject.save()
            return redirect('list_trainee')
        else:
            context['error']="invalid trainee"
    return render(req, 'createtrainee/create.html',context)
def trainee_trainee(req):
    return render(req, 'trainee.html')




# Create your views here.
