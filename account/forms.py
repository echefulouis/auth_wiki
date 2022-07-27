from dataclasses import fields
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile







class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name=forms.CharField(max_length=30, required=False)
    last_name=forms.CharField(max_length=30, required=False)
    
    class Meta:
        model=User
        fields= ('username', 'first_name','last_name', 'email','password1','password2',)
        
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email =self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['bio']

# Create your models here.
