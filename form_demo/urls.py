from django.contrib import admin
from django.urls import path

from . import views

app_name = 'form_demo'

urlpatterns = [
    path('register', views.RegisterView.as_view(),name='index'),
    path('file', views.FileView.as_view(),name='files'),
]