from django.contrib import admin
from django.urls import path

from . import views

app_name = 'cookie_session'

urlpatterns = [
    path('',views.index),
]