from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
import json
import requests

class Index(View):

	def get(self,request,*args, **kwargs):	
		url = 'http://backend:8000/api/v1/tweets'
		headers = {'Content-Type': 'application/json',}

		try:
			response = requests.get(url,headers=headers)
			if response.status_code == 200:
				#print('si funciono el consumo')
				#print(response.content.decode('utf-8'))
				#return json.loads(response.content.decode('utf-8'))
				tweets = json.loads(response.content.decode('utf-8'))
				return render(request,'index.html',context={'mensaje':'Si funcionono','tweets':tweets})
			else:
				return render(request,'index.html',context={'mensaje':'Hubo un error, no se pudo consumir correctamente'})
		except requests.exceptions.RequestException as e:
			print(e)
			return render(request,'index.html',context={'mensaje':'Hubo un error'+str(e)})
	def post(self,request):
		usuario = request.POST['usuario']
		mensaje = request.POST['mensaje']
		if usuario != '' and mensaje != '':
			post = json.dumps({'usuario':usuario,'contenido':mensaje})
			#json_post = json.dump(post)
			url = 'http://backend:8000/api/v1/tweets'
			headers = {'Content-Type': 'application/json',}
			try:
				response = requests.post(url,data=post,headers=headers)
				if response.status_code == 200:
					return redirect('/inicio')
				else:
					return redirect('/inicio')
			except requests.exceptions.RequestException as e:
				print(e)
				return redirect('/inicio')

class Perfil(View):
	def get(self,request,username):
		print(username)
		url = 'http://backend:8000/api/v1/tweets?username={0}'.format(username)
		headers = {'Content-Type': 'application/json',}
		try:
			response = requests.get(url,headers=headers)
			if response.status_code == 200:
				#print('si funciono el consumo')
				#print(response.content.decode('utf-8'))
				#return json.loads(response.content.decode('utf-8'))
				tweets = json.loads(response.content.decode('utf-8'))
				return render(request,'perfil.html',context={'mensaje':'Si funcionono','tweets':tweets})
			else:
				return render(request,'index.html',context={'mensaje':'Hubo un error, no se pudo consumir correctamente'})
		except requests.exceptions.RequestException as e:
			return render(request,'index.html',context={'mensaje':'Hubo un error'+str(e)})
	


class Buscar(View):
	def post(self,request):
		usuario= request.POST['usuario']
		print(usuario)
		url = '/perfil/{}'.format(usuario)
		return redirect(url)