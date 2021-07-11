from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, Author
from django.db.models import Q

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
        
    context = {
        'posts': paged_posts
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            posts = Post.published.order_by('-publish').filter(Q(title__icontains=q) | Q(body__icontains=q))
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)