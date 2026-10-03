from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'read.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
