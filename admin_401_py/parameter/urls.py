from django.urls import path

from . import views

urlpatterns = [
    path('createParameter', views.createParameter, name='createParameter'),
    path('getParameters', views.getParameters, name='getParameters'),
]