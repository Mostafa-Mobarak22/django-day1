from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
def list_account(req):
    return render(req,'list/list.html')
# Create your views here.
def update_account(req):
    return render(req,'update/update.html')
def delete_account(req):
    return render(req,'delete/delete.html')
def create_account(req):
    return render(req,'create/create.html')
def account_account(req):
    return render(req, 'account.html')