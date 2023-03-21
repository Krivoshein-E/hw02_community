from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User
import datetime

LAST_TEN_POSTS: int = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
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
    posts = Post.objects.filter(group=group).all()
    paginator = Paginator(posts, LAST_TEN_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)
