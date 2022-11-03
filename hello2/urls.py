from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index, name='index'),
  # nameという引数は、このurlにindexという名前を設定している。
  path('', views.message, name='message'),
  path('<int:page>', views.message, name='message'),
]