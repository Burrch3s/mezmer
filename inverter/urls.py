#!/usr/bin/python3

from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
