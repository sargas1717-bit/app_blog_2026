from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# ================= 1. READ (Público) =================
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'read.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

# ================= 2. CREATE (Protegido + Autor Automático) =================
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content', 'author']  # Specify the fields you want to include in the form
# POLIMORFISMO Y SOBREESCRITURA (Concepto POO):
    # Interceptamos el formulario validado antes de guardarlo en SQLite
    def form_valid(self, form):
        # Asignamos al campo 'author' el usuario que tiene la sesión activa
        form.instance.author = self.request.user
        # super() delega a CreateView el guardado final en base de datos
        return super().form_valid(form)


# ================= 3. UPDATE (Protegido + Solo Autor) =================
# El orden en la herencia múltiple (MRO):
# 1. LoginRequiredMixin: ¿Está logueado?
# 2. UserPassesTestMixin: ¿Tiene permiso?
# 3. UpdateView: Construye el formulario.
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']  # Specify the fields you want to include in the form
# Método de autorización por objeto
    def test_func(self):
        # get_object() recupera el Post específico que viaja con el ID en la URL (<pk>)
        post = self.get_object()
        # Retorna True solo si el autor del post coincide con el usuario de la sesión
        return post.author == self.request.user


# ================= 4. DELETE (Protegido + Solo Autor) =================
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list after deletion
# Aplicamos la misma regla de negocio para la eliminación
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user