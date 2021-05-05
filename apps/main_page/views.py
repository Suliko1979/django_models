from django.shortcuts import render
from apps.posts.models import post


def index(request):
    posts = post.objects.all()
    return render(request=request, template_name='pages/index.html', context={'posts': posts})
