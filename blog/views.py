from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from .models import *

def post_list(request):
    all_posts = Post.published.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 3)
    posts = paginator.get_page(page_num)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status = Post.Status.PUBLISHED,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             slug = slug)
    return render(request, 'blog/post/detail.html', {'post':post})


