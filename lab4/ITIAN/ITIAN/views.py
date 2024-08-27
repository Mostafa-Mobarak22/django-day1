from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.http import HttpResponse
def home_itian(req):
    return render(req, 'itian.html')