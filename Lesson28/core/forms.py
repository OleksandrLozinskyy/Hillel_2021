from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'content': forms.Textarea(attrs={'class': 'form-control',}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
        }