from category.models import Category
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Post, Author
from django.contrib.auth.decorators import login_required
from dashboard.forms import ArticleCreateForm, CategoryForm
from django.contrib import messages
from django.utils import timezone
from django.views.generic import View


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    author_obj = get_object_or_404(Author, user_id=request.user.id)
    article_list = Post.published.filter(author=author_obj)

    total_published_articles = len(article_list)
    total_articles_comments = sum(
        article.comments.count() for article in article_list)
    total_articles_views = sum(article.views for article in article_list)

    recent_published_articles = article_list.order_by("-publish")[:9]

    context = {
        'total_published_articles': total_published_articles,
        'total_articles_comments': total_articles_comments,
        'total_articles_views': total_articles_views,
        'recent_published_articles': recent_published_articles,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'dashboard/blog/post_details.html', context)


@login_required(login_url='login')
def create_post(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    form = ArticleCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = get_object_or_404(Author, user_id=request.user.id)
        obj.author = author
        obj.save()
        form.save_m2m()
        form = ArticleCreateForm()

    context = {
        'form': form
    }
    return render(request, "dashboard/blog/write_article.html", context)


@login_required(login_url='login')
def published_articles(request):
    author_obj = get_object_or_404(Author, user_id=request.user.id)
    article_list = Post.published.filter(author=author_obj)
    context = {
        'posts': article_list
    }
    return render(request, 'dashboard/blog/published_articles.html', context)


@login_required(login_url='login')
def drafted_articles(request):
    author_obj = get_object_or_404(Author, user_id=request.user.id)
    article_list = Post.objects.filter(author=author_obj, status='draft')
    context = {
        'posts': article_list
    }
    return render(request, 'dashboard/blog/drafted_articles.html', context)


@login_required(login_url='login')
def edit_blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = ArticleCreateForm(request.POST or None,
                             request.FILES or None, instance=post)
    author = get_object_or_404(Author, user_id=request.user.id)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.publish = timezone.now()
            form.updated = timezone.now()
            form.save()
            return redirect(reverse('dashboard:post_details', kwargs={'slug': form.instance.slug}))
    context = {
        'form': form
    }
    return render(request, 'dashboard/blog/update_article.html', context)


@login_required(login_url='login')
def create_category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category submitted successfully.')
            return redirect('dashboard:add-category')
    else:
        form = CategoryForm()

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'dashboard/blog/category.html', context)


@login_required(login_url='login')
def author_settings(request):
	return render(request, 'dashboard/profile/settings.html')


@login_required(login_url='login')
def author_profiile(request):
	return render(request, 'dashboard/profile/profile.html')
