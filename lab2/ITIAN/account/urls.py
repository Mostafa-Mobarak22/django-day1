from lib2to3.fixes.fix_input import context

from django.urls import path,include
from .views import *

urlpatterns = [
   path('list/',list_account,name='list_account'),
   path('',account_account,name='account_account'),
   path('update/',update_account,name='update_account'),
   path('delete/',delete_account,name='delete_account'),
   path('create/',create_account,name='create_account'),

]