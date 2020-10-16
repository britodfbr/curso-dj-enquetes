# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
