from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'read.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content', 'author']  # Specify the fields you want to include in the form