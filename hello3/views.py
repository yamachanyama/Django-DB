from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Message
from .forms import MessageForm
from .forms import FindForm

from django.db.models import Q

from django.db.models import Count,Sum,Avg,Min,Max

from django.core.paginator import Paginator

def index(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Top',
        'data': paginator.get_page(page),
    }
    return render(request, 'hello3/index.html', params)

def list(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'List',
        'data': paginator.get_page(page),
    }
    return render(request, 'hello3/list.html', params)

def edit(request, num):
    obj = Message.objects.get(id=num)
    if (request.method == 'POST'):
        message = MessageForm(request.POST, instance=obj)
        message.save()
        return redirect(to='index')
    params = {
        'title': 'Edit',
        'id': num,
        'form': MessageForm(instance=obj),
        }
    return render(request, 'hello3/edit.html', params)

def create(request):
    params = {
        'title': 'Create',
        'form': MessageForm(),
        }
    if (request.method == 'POST'):
        obj = Message()
        message = MessageForm(request.POST, instance=obj)
        message.save()
        return redirect(to='index')
    return render(request, 'hello3/create.html', params)