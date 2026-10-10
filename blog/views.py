from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView

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

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']  # Specify the fields you want to include in the form

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list after deletion
