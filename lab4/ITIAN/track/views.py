from contextlib import redirect_stdout
from lib2to3.fixes.fix_input import context
from urllib.request import HTTPRedirectHandler
import sys
from django.http import HttpResponse
from .models import *
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect

def show_track(req,id):
    tracks = Track.objects.get(pk=id)
    context={}
    context['tracks']=tracks
    return render(req,'show/show_track.html',context)
def list_track(req):
    tracks = Track.objects.all()
    context = {}
    context['tracks'] = tracks
    return render(req, 'listtrack/list.html',context)
def update_track(req,id):
    context={}
    track_obj = Track.objects.get(pk=id)
    context['trackobj'] = track_obj
    if(req.method=='POST'):
        if(len(req.POST['trackname'])>0 and len(req.POST['trackname'])<=50):
            Track.objects.filter(pk=id).update(name=req.POST['trackname'])
            return redirect('list_track')
        else:
            context['error']="invalid account"
    return render(req, 'updatetrack/update.html',context)
def delete_track(req,id):
    context={}
    try:
        Track.objects.filter(pk=id).delete()
        return redirect('list_track')
    except:
        context['error'] = sys.exc_info()[1]
    return render(req, 'deletetrack/delete.html',context)
def create_track(req):
    context = {}
    if(req.method=='POST'):
        if(len(req.POST['trackname'])>0 and len(req.POST['trackname'])<=50):
            trackobject = Track()
            trackobject.name = req.POST['trackname']
            trackobject.save()
            return redirect('list_track')
        else:
            context['error']="invalid track name"
    return render(req, 'createtrack/create.html',context)

def track_track(req):
    return render(req, 'track.html')




# Create your views here.
