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
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('list', views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<int:post_pk>/', views.comment_create, name='comment_create'),
    path('reply/<int:comment_pk>/', views.reply_create, name='reply_create'),
#    path('<int:num>', views.index, name='index'),
#    path('edit/<int:num>', views.edit, name='edit'),
#    path('find', views.find, name='find'),
#    path('message/', views.message, name='message'),
#    path('message/<int:page>', views.message, name='message'),
]
