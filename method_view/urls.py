from django.contrib import admin
from django.urls import path

from . import views

app_name = 'method_view'

urlpatterns = [
    path('', views.index,name='index'),
    path('inde1/', views.index1,name='index1'),
    path('index2/', views.index2,name='index2'),
    path('index3/', views.ArticleListView.as_view(),name='index3'),
]