from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog_core.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.filter(is_publish=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
