from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('me/', views.dashboard, name='dashboard'),
    path('me/article/create/', views.create_post, name='article-create'),
    path('me/published-articles/', views.published_articles, name='published-articles'),
    path('me/drafted-articles/', views.drafted_articles, name='drafted-articles'),
    path('me/<slug:slug>/', views.post_details, name='post_details'),
    path('me/edit/<slug:slug>/', views.edit_blog_post, name='edit-post'),
]
