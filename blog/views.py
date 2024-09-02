from blog.models import Post
from django.shortcuts import render


def post_list_view(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})
