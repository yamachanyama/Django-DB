from .models import Message
from django import forms

class HelloForm(forms.Form):
  name = forms.CharField(label='name')
  mail = forms.CharField(label='mail')
  age = forms.IntegerField(label='age')

class MessageForm(forms.ModelForm):
  # models.pyよりMessageクラスを引用している
  # ModelFormについては、https://itc.tokyo/django/modelform/
  class Meta:
    model = Message
    fields = ['title','content','user']