from django.shortcuts import render, get_object_or_404
from blog.models import Post


def home(request):
    featured = Post.published.filter(featured=True)[:2]
    posts = Post.published.order_by('-publish').exclude(featured=True)[:9]
    context = {
        'featured': featured,
        'posts': posts
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def error_404(request, exception):
    return render(request, 'page404.html', {})


def error_500(request):
    return render(request, 'page500.html', {})
