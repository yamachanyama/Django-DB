from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .forms import HelloForm, MessageForm
from django.core.paginator import Paginator

# Create your views here.
"""def index(request):
    data = Friend.objects.all()
    params = {
      'title': 'Hello',
      'message': 'all friends.',
      'data': data,
      }
    return render(request, 'hello2/index.html', params)
"""

def message(request, page=1):
    #message.htmlのformにてpostされた時に下記if文が実行される模様。
    if (request.method == 'POST'):
      obj = Message()
      form = MessageForm(request.POST, instance=obj)
      form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
      'title': 'Message',
      'form': MessageForm(),
      'data': paginator.get_page(page),
      }
    return render(request, 'hello2/message.html', params)