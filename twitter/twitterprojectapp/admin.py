from django.contrib import admin
from .models import User,Tweet
from django import forms
import re


class UserAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        name=self.cleaned_data.get('name')
        email=self.cleaned_data.get('email')
        regex = r'^(((\w+)(\.\w+)?)|((\w+)(\-\w+)?))\@(\w+)(\.\w+)(\.\w+)*'
        matches = re.match(regex, email)
        if matches is None:
            raise forms.ValidationError("Enter correct email")
        if len(name) < 3:
            raise forms.ValidationError("Name is too short.")
        return self.cleaned_data
    

class TweetAdminForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(TweetAdminForm,self).__init__(*args,**kwargs)
    
    def clean(self):
        tweet=self.cleaned_data.get('tweet')
        if len(tweet) == 0:
            raise forms.ValidationError("Your tweet should have atleast 1 character.")
        if len(tweet) > 140:
            raise forms.ValidationError("Your tweet should not exceed 140 characters.")
        return self.cleaned_data
        
            
class UserAdmin(admin.ModelAdmin):
    list_display=('name','email',)
    form=UserAdminForm
    
    
class TweetAdmin(admin.ModelAdmin):
    list_display=('username','tweet','date_created','date_edited','delete',)
    form=TweetAdminForm
    
admin.site.register(User,UserAdmin)
admin.site.register(Tweet,TweetAdmin)
