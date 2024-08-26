import sys
from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
def show_account(req,id):
    accounts = Account.objects.get(pk=id)
    context={}
    context['accounts']=accounts
    return render(req,'show/show_account.html',context)
def list_account(req):
    accounts = Account.objects.all()
    context={}
    context['accounts']=accounts
    return render(req,'list/list.html',context)
def update_account(req,id):
    context = {}
    accountobject = Account.objects.get(pk=id)
    context['account_obj']= accountobject
    if(req.method=='POST'):
        if(len(req.POST['accountname'])>0 and len(req.POST['accountname'])<=50 and len(req.POST['accountdescription'])>0):
            Account.objects.filter(pk=id).update(name=req.POST['accountname'],description=req.POST['accountdescription'])
            return redirect('list_account')
        else:
            context['error']="invalid account"
    return render(req,'update/update.html',context)
def delete_account(req,id):
    context={}
    try:
        Account.objects.filter(pk=id).delete()
        return redirect('list_account')
    except:
        context['error'] = sys.exc_info()[1]
    return render(req,'delete/delete.html',context)
def create_account(req):
    context = {}
    if(req.method=='POST'):
        if(len(req.POST['accountname'])>0 and len(req.POST['accountname'])<=50 and len(req.POST['accountdescription'])>0):
            accountobject = Account()
            accountobject.name = req.POST['accountname']
            accountobject.description =req.POST['accountdescription']
            accountobject.save()
            return redirect('list_account')
        else:
            context['error']="invalid account"
    return render(req,'create/create.html',context)
def account_account(req):
    return render(req, 'account.html')