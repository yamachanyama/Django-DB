# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:59:43 2018

@author: tuyano
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index/<int:page>', views.index, name='index'),
    path('list', views.list, name='list'),
    path('list/<int:page>', views.list, name='list'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
#    path('<int:num>', views.index, name='index'),
#    path('edit/<int:num>', views.edit, name='edit'),
#    path('find', views.find, name='find'),
#    path('message/', views.message, name='message'),
#    path('message/<int:page>', views.message, name='message'),
]
