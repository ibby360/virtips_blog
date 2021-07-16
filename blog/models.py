from django.db import models
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='static/img/author/default-profile.png')
    description = models.TextField()

    def get_author_url(self):
        return reverse('author', args=[self.id])

    def __str__(self):
        return self.author.username

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
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False)

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
    