from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Article

from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', "email")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__( *args, **kwargs)

        self.fields['username'].widget.attrs.update({
            "placeholder":"username"
        })

        self.fields['password1'].widget.attrs.update({
            "placeholder":"password"
        })

        self.fields['password2'].widget.attrs.update({
            "placeholder":"password confirm"
        })

        self.fields['email'].widget.attrs.update({
            "placeholder":"email"
        })

        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class":"form-control"
            })

        

class AddArticleForm(ModelForm):
    class Meta:
        model  = Article
        fields = ("title", "description", "author")


    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__( *args, **kwargs)

        self.fields['title'].widget.attrs.update({
            "placeholder":"title"
        })

        self.fields['description'].widget.attrs.update({
            "placeholder":"Content"
        })

        self.fields['author'].widget.attrs.update({
            "placeholder":"author"
        })

        self.fields['description'].strip = False


        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class":"form-control"
            })

        


        
