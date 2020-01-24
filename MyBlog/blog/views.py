from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# We using render function ro recieve HttpResponse and
# render this template with our variables (n here)


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)            # _iexact is means Case insensitive
    return render(request, 'blog/post_detail.html', context={'post': post})

