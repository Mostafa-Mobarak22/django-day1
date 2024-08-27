from lib2to3.fixes.fix_input import context

from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('list/',list_trainee,name='list_trainee'),
   path('',trainee_trainee,name='trainee_trainee'),
   path('update/<int:id>',update_trainee,name='update_trainee'),
   path('delete/<int:id>',delete_trainee,name='delete_trainee'),
   path('create/',create_trainee,name='create_trainee'),
   path('createform/',create_trainee_form,name='create_trainee_form'),
   path('show/<int:id>',show_trainee,name='show_trainee'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)