from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index, name='index'),
  # nameは、templates/hello2/message.htmlの文中の<form action="{% url 'message' %}" method="post">におけるmessageで引用されている。
  path('', views.message, name='message'),
  path('<int:page>', views.message, name='message'),
]