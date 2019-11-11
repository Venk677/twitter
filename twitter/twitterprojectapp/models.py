from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=15,unique=True)
    
    def __str__(self):
        return self.name
    

    
    
class Tweet(models.Model):
    username=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    tweet=models.CharField(max_length=140)
    date_created=models.DateField(auto_now=False)
    date_edited=models.DateField(auto_now_add=False)
    delete=models.BooleanField(default=False)
    
    def __str__(self):
        return self.tweet
    

