from django.urls import path,include
from usuarios.views import UsuarioListView
urlpatterns = [
    path('', UsuarioListView.as_view()),
]
