from django.urls import path
from .views import ListAPIView,TweetListAPIview


urlpatterns=[
    path('tweet',TweetListAPIview.as_view(),name='tweet-list'),
]