from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms

from products.models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

 

class bookForm(forms.ModelForm):
    class Meta:
        model= book
        fields=('tittle','image','content','caticory')
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class categoryform(forms.ModelForm):
    class Meta:
        model= Catecory
        fields=('name',"pic" )
        
class users(forms.ModelForm):
    class Meta:
        model=user
        fields='__all__'
class commentform(forms.ModelForm):
    class Meta: 
    
     model = Comment
     fields=('body', )
    
class replyform(forms.ModelForm):
    class Meta: 
    
     model = Comment
     fields=('reply', )
class ForbiddenWordsForm(forms.ModelForm):
    forbidden_word = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ForbiddenWords
        fields = ('forbidden_word',)     
    


        

        


        