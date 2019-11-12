from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email',)


class TweetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tweet
        fields = ('username','tweet','date_created','date_edited','delete',)