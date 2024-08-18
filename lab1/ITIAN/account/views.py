from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
def list_account(req):
    track = []
    track1={'name': 'python', 'id': 1}
    track.append(track1)
    track2 = {'name': 'java', 'id': 2}
    track.append(track2)
    track3 = {'name': 'os', 'id': 3}
    track.append(track3)
    track4 = {'name': 'mobile', 'id': 4}
    track.append(track4)
    context={}
    context['tracks'] = track
    return render(req,'list/list.html',context)
# Create your views here.
def update_account(req,id):
    return render(req,'update/update.html', {'id':id})
def delete_account(req,id):
    return render(req,'delete/delete.html', {'id':id})
def create_account(req,name):
    return render(req,'create/create.html', {'name':name})