from lib2to3.fixes.fix_input import context

from django.urls import path,include
from .views import *

urlpatterns = [
   path('list/',list_trainee,name='list_trainee'),
   path('',trainee_trainee,name='trainee_trainee'),
   path('update/',update_trainee,name='update_trainee'),
   path('delete/',delete_trainee,name='delete_trainee'),
   path('create/',create_trainee,name='create_trainee'),

]