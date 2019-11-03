from django.db import models

# Create your models here.


class Usuario(models.Model):
	username = models.CharField(max_length=70)
	nombre = models.CharField(max_length=100)
	correo = models.EmailField()
	password = models.CharField(max_length=40,default="1234")

	def __str__(self):
		return self.username;