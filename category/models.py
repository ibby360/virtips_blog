from django.db import models
from django.urls import reverse
import blog.models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_by_category', args=[self.slug])

    def category_post_count(self):
        return blog.models.Post.published.filter(category=self.id).count()

    def __str__(self):
        return self.category_name