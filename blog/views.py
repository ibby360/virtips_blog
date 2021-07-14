from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from category.models import Category
from blog.models import Post, Author
from django.db.models import Q
from taggit.models import Tag

# Create your views here.

def post_list(request, tag_slug=None, category_slug=None): 
    categories = None
    posts = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        posts = Post.published.filter(category=categories)
        paginator = Paginator(posts, 9)
        page = request.GET.get('page')
        paged_posts = paginator.get_page(page)
        post_count = posts.count()
    else:
        posts = Post.published.all()
        paginator = Paginator(posts, 9)
        page = request.GET.get('page')
        paged_posts = paginator.get_page(page)
        post_count = posts.count()

    tags = Tag.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
  
    context = {
        'posts': paged_posts,
        'tags': tags,
        'tag': tag,
        'post_count': post_count
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, post, category_slug):
    post = get_object_or_404(Post, slug=post, status='published', category__slug=category_slug)
    try:
        previous_post = post.get_previous_by_publish()
        next_post = post.get_next_by_publish()
    except ObjectDoesNotExist:
        previous_post = None
        next_post = post.get_next_by_publish()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
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