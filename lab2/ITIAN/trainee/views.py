from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.http import HttpResponse
def list_trainee(req):
    return render(req, 'listtrainee/list.html')
def update_trainee(req):
    return render(req, 'updatetrainee/update.html')
def delete_trainee(req):
    return render(req, 'deletetrainee/delete.html')
def create_trainee(req):
    return render(req, 'createtrainee/create.html')
def trainee_trainee(req):
    return render(req, 'trainee.html')




# Create your views here.
