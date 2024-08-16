from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts1'
    queryset = Post.objects.all().order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_details.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

