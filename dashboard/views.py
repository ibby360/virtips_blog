from django.shortcuts import render, get_object_or_404
from blog.models import Post, Author
from django.contrib.auth.decorators import login_required

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