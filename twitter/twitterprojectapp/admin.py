from django.contrib import admin
from .models import User,Tweet
from django import forms


class UserAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        name=self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name is too short")
        return self.cleaned_data
            
class UserAdmin(admin.ModelAdmin):
    list_display=('name','email',)
    form=UserAdminForm
    
    
class TweetAdmin(admin.ModelAdmin):
    list_display=('username','tweet','date_created','date_edited','delete',)
    
admin.site.register(User,UserAdmin)
admin.site.register(Tweet,TweetAdmin)
