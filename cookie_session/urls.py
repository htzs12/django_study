from django.contrib import admin
from django.urls import path

from . import views

app_name = 'cookie_session'

urlpatterns = [
    path('',views.index),
    path('list/',views.my_list),
    path('del/',views.del_cookie),
    path('session/',views.session_view),
]