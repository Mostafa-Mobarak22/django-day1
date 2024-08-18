from lib2to3.fixes.fix_input import context

from django.urls import path,include
from .views import *

urlpatterns = [
   path('list/',list_trainee,name='list_trainee'),
   path('update/<int:id>',update_trainee,name='update_trainee'),
   path('delete/<int:id>',delete_trainee,name='delete_trainee'),
   path('create/<str:name>',create_trainee,name='create_trainee'),

]