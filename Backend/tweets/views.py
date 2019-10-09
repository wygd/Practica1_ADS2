# tweets/views.py
from rest_framework import generics

from tweets.models import Tweet
from tweets.serializers import TweetSerializer

class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all().order_by('-fecha')
    serializer_class = TweetSerializer

    def get_queryset(self):
        queryset = Tweet.objects.all()
        username = self.request.query_params.get('username')
        #try:
        #	usuario = Usuario.objects.get(username=username)
        #except Usuario.DoesNotExist:
        #	usuario = None
        if username:
            queryset = queryset.filter(usuario__username=username).order_by('-fecha')

        return queryset