from lib2to3.fixes.fix_input import context
from django.shortcuts import render,redirect
import sys
from .forms import *
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
            Trainee.objects.filter(pk=id).update(name=req.POST['traineename'],trackobject=Track.objects.get(pk=req.POST['trackobj']),img=req.POST['image'])
            return redirect('list_trainee')
        else:
            context['error']="invalid trainee"
    return render(req, 'updatetrainee/update.html',context)
def delete_trainee(req,id):
    context={}
    try:
        Trainee.delete(id)
        return redirect('list_trainee')
    except:
        context['error'] = sys.exc_info()[1]
    return render(req, 'deletetrainee/delete.html')
def create_trainee(req):
    context = {}
    context['trackobjs']=Track.objects.all()
    if(req.method=='POST'):
        if(len(req.POST['traineename'])>0 and len(req.POST['traineename'])<=50):
            Trainee.create(req.POST['traineename'],req.FILES['image'],req.POST['trackobj'])
            return redirect('list_trainee')
        else:
            context['error']="invalid trainee"
    return render(req, 'createtrainee/create.html',context)
def trainee_trainee(req):
    return render(req, 'trainee.html')

def create_trainee_form(req):
    context={}
    form = NewTrainee()
    context['form']=form
    if(req.method=='POST'):
        forms = NewTrainee(req.POST,req.FILES)
        if(forms.is_valid()):
            Trainee.create(forms.cleaned_data['name'],
                      forms.cleaned_data['img'],forms.cleaned_data['trackobject'])
            return redirect('list_trainee')
        else:
            context['error']=forms.errors
    return render(req, 'createtrainee/createform.html',context)


# Create your views here.
