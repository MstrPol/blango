from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog_core.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
