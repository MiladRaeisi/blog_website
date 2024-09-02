from blog.models import Post
from django.shortcuts import render


def post_list_view(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

