from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    context = {
        'post': post
    }
    return render(request, '', context)
