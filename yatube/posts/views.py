from django.shortcuts import render, get_object_or_404

from .models import Post, Group, User

import datetime


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts
    }
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)

    author = User.objects.get(username="leo")
    keyword = "утро"
    posts = Post.objects.filter(
        pub_date__range=(start_date, end_date),
        text__contains=keyword, author=author
    )

    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
