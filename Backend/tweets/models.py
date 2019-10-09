from django.db import models
from usuarios.models import Usuario
from datetime import datetime
# Create your models here.

class Tweet(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	contenido = models.CharField(max_length=281)
	fecha = models.DateTimeField(default=datetime.now, blank=True)
