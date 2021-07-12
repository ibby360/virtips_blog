from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, Author
from django.db.models import Q
from taggit.models import Tag

# Create your views here.

def post_list(request, tag_slug=None):
    tags = Tag.objects.all()
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    try:
        paged_posts = paginator.page(page)
    except PageNotAnInteger:
        paged_posts = paginator.page(1)
    except EmptyPage:
        paged_posts = paginator.page(paginator.num_pages)
        
    context = {
        'posts': paged_posts,
        'tags': tags,
        'tag': tag,
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