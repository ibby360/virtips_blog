from django import template
from django.db.models import Count, Sum, F
from django.shortcuts import get_object_or_404
from blog.models import Post, Author

register = template.Library()


@register.simple_tag
def get_most_viewed_postss(count=4):
    return Post.published.filter(views__gt=8)[:count]

# 
# def get_most_commented_posts(count=4):
# 
    # return Post.published.annotate(
        # total_comments=Count('comments')
    # ).filter(publish__range=[timezone.now() - timezone.timedelta(seconds=3), timezone.now()]).order_by('-total_comments')[:count]


@register.simple_tag
def get_latest_posts():
    return Post.published.order_by('-publish')[:4]

@register.simple_tag
def get_most_viewed_posts(count=4):
    return Post.published.annotate(
total_views=Count('views')
).order_by('-total_views')[:count]

