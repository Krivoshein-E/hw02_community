from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# Create your views here.
def index(request):
    template = 'posts/index.html'

    title = 'Это главная страница проекта YaTube'
    text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
        'text': text}
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    text = 'Здесь будет информация о группах проекта YaTube'
    context = {
        'group': group,
        'posts': posts,
        'text': text}
    return render(request, template, context)
