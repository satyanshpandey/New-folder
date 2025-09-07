from django.urls import path 

from . import views



urlpatterns = [
    path('app/v1/', views.home, name='home'),
    path('app/v1/students/', views.home, name='students'),
]