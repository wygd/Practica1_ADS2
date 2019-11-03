# users/serializers.py
from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username','nombre','correo','password' )