from accounts.models import Account
from django.db import models
from django.conf import settings
from django.urls import reverse 
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from category.models import Category 

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars', default='img/author/default-profile.png')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default='')
    tags = TaggableManager()
    author = models.ForeignKey(Author, related_name='blog_post', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='post')
    overview = models.TextField()
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    objects  = models.Manager() # Default Manager
    published = PublishedManager() # Custom Manager

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.category.slug, self.slug])
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'