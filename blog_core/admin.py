from django.contrib import admin
from blog_core.models import Post


class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'rating')
    search_fields = ('title', 'author', 'content', 'rating')


admin.site.register(Post, PostAdmin)
