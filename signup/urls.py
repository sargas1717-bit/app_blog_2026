from django.urls import path
from .views import SignUpView

urlpatterns = [
    # as_view() transforma la clase en una función procesable por el despachador de URLs
    path('signup/', SignUpView.as_view(), name='signup'),
]