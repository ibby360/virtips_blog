from django.contrib import admin
from blog.models import Post, Author, Comment

# Register your models here.
admin.site.register(Author)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'date_created', 'active')
    list_filter = ('active', 'date_created', 'updated')
    search_fields = ('name', 'email', 'body')
    actions = ['disapprove_comments']

    def disapprove_comments(self, request, queryset):
        queryset.update(active=False)