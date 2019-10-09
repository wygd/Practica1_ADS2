from django.contrib import admin
from django.urls import path
from ui.views import Index,Perfil,Buscar
urlpatterns = [
	path('inicio',Index.as_view()),
    path('perfil/<str:username>/',Perfil.as_view()),
    path('buscar/',Buscar.as_view()),
]
