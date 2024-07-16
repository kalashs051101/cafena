from django.contrib import admin
from django.urls import path,include
from app1.views import *
urlpatterns = [
    path('',app1,name='app1'),
    path('llogin/',llogin,name='llogin'),
    path('registration_page/',registration_page,name='registration_page'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete_data/<int:id>',delete_data,name='delete_data'),
    path('update_data<int:id>/',update_data,name='update_data'),
    path('upload_data<int:id>/',upload_data,name='upload_data'),
    # path('start_login/',start_login,name='start_login'),
    #path('newone',newone,name='newone'),
    path('logoutt',logoutt,name='logoutt'),
    path('Blogg',Blogg,name='Blogg'),

    #path('forget/<str:name>/',forgot_p,name='forget'),
    #path('abc',abcs,name='abcs'),
     
]