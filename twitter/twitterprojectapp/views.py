from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import response
from .serializers import TweetSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Tweet
from rest_framework import serializers

class TweetListAPIview(ListAPIView):
    queryset=Tweet.objects.all().filter(delete=False)
    serializer_class=TweetSerializers


