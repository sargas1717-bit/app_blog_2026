from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Aplicamos Herencia Simple: SignUpView adquiere todas las capacidades
# del motor de formularios genéricos de Django (CreateView).
class SignUpView(CreateView):
    # 1. Definimos qué formulario construirá la vista en memoria:
    # UserCreationForm genera automáticamente: username, password1 y password2 (confirmación)
    form_class = UserCreationForm

    # 2. Especificamos qué plantilla física renderizará el HTML:
    template_name = 'registration/signup.html'

    # 3. Redirección diferida:
    # Una vez que el usuario se registra con éxito en la base de datos SQLite,
    # lo enviamos a la pantalla de login para que ingrese con sus nuevas credenciales.
    # Usamos reverse_lazy porque la URL debe resolverse dinámicamente al momento del POST.
    success_url = reverse_lazy('login')
