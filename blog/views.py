from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from category.models import Category
from blog.models import Post, Author
from django.db.models import Q, Count
from blog.forms import CommentForm
from taggit.models import Tag

# Create your views here.

def post_list(request, tag_slug=None, category_slug=None): 
    categories = None
    posts = None
    tag = None
    object_list = Post.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag]).distinct()
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
    
  
    context = {
        'posts': paged_posts,
        'tags': tags,
        'tag': tag,
        'post_count': post_count,
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, post, category_slug):
    post = get_object_or_404(Post, slug=post, status='published', category__slug=category_slug)
    session_key = f"viewed_article {post}"
    if not request.session.get(session_key, False):
        post.views += 1
        post.save()
        request.session[session_key] = True
    try:
        previous_post = post.get_previous_by_publish()
    except ObjectDoesNotExist:
        previous_post = None
    try:
        next_post = post.get_next_by_publish()
    except ObjectDoesNotExist:
        next_post = None

    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'new_comment': new_comment,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post.html', context)

def author(request, username):
    author_obj = get_object_or_404(Author, user__username=username)
    posts = Post.published.filter(author=author_obj).order_by('-publish')
    post_count = posts.count()
    context = {
        'author': author_obj,
        'posts': posts,
        'post_count': post_count
    }
    return render(request, 'blog/author.html', context)


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            posts = Post.published.order_by('-publish').filter(Q(title__icontains=q) | Q(body__icontains=q))
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)