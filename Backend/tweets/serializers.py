# users/serializers.py
from rest_framework import serializers
from tweets.models import Tweet
from datetime import datetime
from usuarios.models import Usuario

class TweetSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(max_length=70)
    class Meta:
        model = Tweet
        #extra_kwargs = {'pk': {'read_only': True}}
        fields = ('usuario','contenido','fecha')
        ordering = '-fecha'

    def create(self, validated_data):
        """Create and return a new user."""
        username = validated_data['usuario']
        contenido = validated_data['contenido']
        print(username)
        print(contenido)
        print(validated_data)
        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            usuario = Usuario(username=username,nombre='Jonh Doe',correo='email@gmail.com')
            usuario.save()
            

        tweet = Tweet(
            usuario = usuario,
            contenido = contenido,
        )
        tweet.fecha = datetime.now()
        tweet.save()
        #numero_cuenta = datetime.now().strftime('%Y%m%d%H%M%S')
        #cuenta.numero = numero_cuenta + str(cuenta.id)
        #cuenta.save()
        return tweet