from blog.models import Post
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from .forms import NewPostForm


def post_list_view(request):
    # posts_list = Post.objects.all()
    posts_list = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = NewPostForm()
    return render(request, 'blog/post_create.html', context={'form': form})
