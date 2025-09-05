from django.urls import path 

from . import views

urlpatterns = [
    path('app/v1/', views.students, name='students'), 
    
]