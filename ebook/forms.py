from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class addbookForm(ModelForm):
    class Meta:
        model=Books
        fields=fields=['name', 'title', 'book_img', 'bookfile', 'aftor', 'cost', 'janr',  'user_id']
        widgets={
            'name': forms.TextInput(attrs={'class': 'addbook-text',}),
            'title': forms.Textarea(attrs={'class': 'addbook-area',}),
            'book_img': forms.FileInput(attrs={'class': 'addbook-file', 'v-on:change':'getimgname', 'required':True}),
            'bookfile': forms.FileInput(attrs={'class': 'addbook-file', 'v-on:change':'getfilegname', 'required':True}),
            'aftor': forms.TextInput(attrs={'class': 'addbook-text',  }),
            'cost': forms.TextInput(attrs={'class': 'addbook-text',  }),
            'janr': forms.TextInput(attrs={'class': 'addbook-text',  'v-model':'janr_id'}),
        }

class updateForm(ModelForm):
    class Meta:
        model=Books
        fields=fields=['name', 'title', 'book_img', 'bookfile', 'aftor', 'cost', 'janr',  'user_id']
        widgets={
            'name': forms.TextInput(attrs={'class': 'addbook-text',  }),
            'title': forms.Textarea(attrs={'class': 'addbook-area',  }),
            'book_img': forms.FileInput(attrs={'class': 'addbook-file', 'v-on:change':'getimgname'}),
            'bookfile': forms.FileInput(attrs={'class': 'addbook-file', 'v-on:change':'getfilegname'}),
            'aftor': forms.TextInput(attrs={'class': 'addbook-text', }),
            'cost': forms.TextInput(attrs={'class': 'addbook-text',}),
            'janr': forms.TextInput(attrs={'class': 'addbook-text',  'v-model':'janr_id'}),
        }

class CreateReader(forms.ModelForm):
    class Meta:
        model=Reader
        fields=['user', 'firstname', 'lastname', 'email', 'phone', 'user_img']
        widgets={
            'user_img':forms.FileInput()
        }

class CreateUser(UserCreationForm):
        class Meta:
            model=User
            fields=fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class JanrForm(forms.ModelForm):
    class Meta:
        model=Janr
        fields='__all__'