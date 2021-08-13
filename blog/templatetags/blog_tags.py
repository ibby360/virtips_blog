from django import template
from django.db.models import Count, Sum, F
from django.shortcuts import get_object_or_404
from blog.models import Post, Author

register = template.Library()


@register.simple_tag
def get_most_viewed_posts(count=4):
    return Post.published.filter(views__gt=10)[:count]


@register.simple_tag
def get_latest_posts():
    return Post.published.order_by('-publish')[:4]
