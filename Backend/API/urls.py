from django.urls import path,include

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('tweets/', include('tweets.urls')),
]
