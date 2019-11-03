# usuarios/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

class UsuarioListView(generics.ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

class UsuarioLoginView(generics.GenericAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
	lookup_field = ('username','password')
	def get_queryset(self):
		queryset = Usuario.objects.all()
		username = self.request.query_params.get('username')
		password = self.request.query_params.get('password')
		#try:
		#	usuario = Usuario.objects.get(username=username)
		#except Usuario.DoesNotExist:
		#	usuario = None
		if username and password:
			queryset = queryset.filter(username=username,password=password)
		return queryset

class UsuarioLogin(APIView):

	def get(self,request,username,password):
		#username = self.request.query_params.get('username')
		#password = self.request.query_params.get('password')
		usuario = Usuario.objects.get(username=username,password=password)
		usuario_json = UsuarioSerializer(usuario)
		return Response(usuario_json.data)