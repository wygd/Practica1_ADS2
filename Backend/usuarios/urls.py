from django.urls import path,include
from usuarios.views import UsuarioListView,UsuarioLoginView,UsuarioLogin
urlpatterns = [
    path('', UsuarioListView.as_view()),
    path('login/<str:username>/<str:password>', UsuarioLogin.as_view()),
]
