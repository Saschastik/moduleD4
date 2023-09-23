from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'type', 'category', 'title', 'textPost']
