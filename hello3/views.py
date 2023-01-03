from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django import forms

from .models import Message, Comment
from .forms import MessageForm, FindForm

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

def edit(request, num):
    obj = Message.objects.get(id=num)
    if (request.method == 'POST'):
        message = MessageForm(request.POST, instance=obj)
        message.save()
        return redirect(to='index')
    form = MessageForm(request.GET) #プレビューに推移するときにformでサーバ側に渡しているデータ(POSTはしていない)をゲットしてMessageForm Classに渡す
    if form.is_valid(): #POSTで渡していない時（プレビュー時）はここが実行される。（MessageForm Classの機能としてvalidされている）
        # context に form だけ渡す
        context = {'form': form }
        return render(
            request,
            "hello3/preview.html",
            context=context
        )
    params = { #1回目はここが実行される。
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


# コメント、返信フォーム
CommentForm = forms.modelform_factory(Comment, fields=('text', ))


class PostList(generic.ListView):
    """記事一覧"""
    template_name = 'hello3/post_list.html'
    model = Message


class PostDetail(generic.DetailView):
    """記事詳細"""
    template_name = 'hello3/post_detail.html'
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # どのコメントにも紐づかないコメント=記事自体へのコメント を取得する
        context['comment_list'] = self.object.comment_set.filter(parent__isnull=True)
        return context


def comment_create(request, post_pk):
    """記事へのコメント作成"""
    post = get_object_or_404(Message, pk=post_pk)
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(to='post_detail', pk=post.pk)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'hello3/comment_form.html', context)


def reply_create(request, comment_pk):
    """コメントへの返信"""
    comment = get_object_or_404(Comment, pk=comment_pk)
    post = comment.post
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.parent = comment
        reply.post = post
        reply.save()
        return redirect(to='post_detail', pk=post.pk)

    context = {
        'form': form,
        'post': post,
        'comment': comment,
    }
    return render(request, 'hello3/comment_form.html', context)