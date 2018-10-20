from django.contrib import admin
from django.urls import path

from . import views

app_name = 'method_view'

urlpatterns = [
    path('', views.index,name='index'),
    path('inde1/', views.index1,name='index1'),
]