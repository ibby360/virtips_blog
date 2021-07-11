from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, Author

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
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
