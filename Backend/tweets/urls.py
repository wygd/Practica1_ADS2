from django.urls import path,include
from tweets.views import TweetListCreateView
urlpatterns = [
    path('', TweetListCreateView.as_view()),
]
