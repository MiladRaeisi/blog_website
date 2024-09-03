from blog.models import Post
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def post_list_view(request):
    # posts_list = Post.objects.all()
    posts_list = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

