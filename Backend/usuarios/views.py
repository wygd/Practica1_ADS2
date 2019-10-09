# usuarios/views.py
from rest_framework import generics

from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer