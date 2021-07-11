from django.core import paginator
from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    featured = Post.published.filter(featured=True)[:2]
    posts = Post.published.order_by('-publish').exclude(featured=True)
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    context = {
        'featured': featured,
        'posts': paged_posts
    }
    return render(request, 'index.html', context)