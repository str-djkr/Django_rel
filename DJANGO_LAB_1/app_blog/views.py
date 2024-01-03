# app_blog /views.py
from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    tags = post.tags.all()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'tags': tags})