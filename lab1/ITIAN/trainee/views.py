from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.http import HttpResponse
def list_trainee(req):
    track = []
    track1 = {'name': 'ahmed', 'id': 1}
    track.append(track1)
    track2 = {'name': 'mostafa', 'id': 2}
    track.append(track2)
    track3 = {'name': 'belal', 'id': 3}
    track.append(track3)
    track4 = {'name': 'nada', 'id': 4}
    track.append(track4)
    context = {}
    context['tracks'] = track
    return render(req, 'list/list.html', context)
def update_trainee(req, id):
    return render(req, 'update/update.html', {'id': id})
def delete_trainee(req, id):
    return render(req, 'delete/delete.html', {'id': id})
def create_trainee(req, name):
    return render(req, 'create/create.html', {'name': name})




# Create your views here.
