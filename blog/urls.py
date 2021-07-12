from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('search/', views.search, name='search'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]
