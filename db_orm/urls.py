from django.contrib import admin
from django.urls import path

from . import views

app_name = 'db_orm'

urlpatterns = [
    # path('exact/', views.exact,name='index'),
    # path('contains/', views.contains,name='index'),
    # path('model/', views.model,name='model'),
    # path('model1/', views.model1,name='model1'),
    # path('model2/', views.model2,name='model2'),
    # path('model3/', views.model3,name='model3'),
    # path('model4/', views.model4,name='model4'),
    # path('model5/', views.model5,name='model5'),
    # path('model6/', views.model6,name='model6'),
    # path('model7/', views.model7,name='model7'),
    # path('model8/', views.model8,name='model8'),
    # path('model9/', views.model9,name='model9'),
    # path('model10/', views.model10,name='model10'),
    path('model11/', views.model11,name='model11'),
]