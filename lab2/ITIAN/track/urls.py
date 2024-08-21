from lib2to3.fixes.fix_input import context

from django.urls import path,include
from .views import *

urlpatterns = [
   path('list/',list_track,name='list_track'),
   path('',track_track,name='track_track'),
   path('update/',update_track,name='update_track'),
   path('delete/',delete_track,name='delete_track'),
   path('create/',create_track,name='create_track'),

]