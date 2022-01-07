from .models import Neighbour, Post, Business, Profile
from django import forms

class NeighbourForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ['user', 'name', 'description', 'location', 'population', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'neighbourhood', 'image']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['user', 'name', 'description', 'neighbourhood']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image', 'neighbourhood']