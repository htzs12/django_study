from django.contrib import admin
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('', views.proxy_view,name='index'),
    path('', views.one_view,name='index'),
]