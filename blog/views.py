from django.shortcuts import render, get_list_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_detail(request, year, month, day, post):
    post = get_list_or_404(Post,
                           status=Post.Status.PUBLISHED,
                           slug=post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

def post_list(request):
    post_list = Post.published.all()
    # Разбивка с 3 постами на страницу
    paginator = Paginator(post_list, 3)
    page_namber = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_namber)
    except PageNotAnInteger:
        # Если не page_number не целое, выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазона, выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})
