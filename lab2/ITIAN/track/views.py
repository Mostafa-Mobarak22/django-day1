from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
def list_track(req):
    return render(req, 'listtrack/list.html')
# Create your views here.
def update_track(req):
    return render(req, 'updatetrack/update.html')
def delete_track(req):
    return render(req, 'deletetrack/delete.html')
def create_track(req):
    return render(req, 'createtrack/create.html')
def track_track(req):
    return render(req, 'track.html')




# Create your views here.
