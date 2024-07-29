from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Location


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'lat', 'lng']
        widgets = {
            'lat': forms.NumberInput(attrs={'step': 'any'}),
            'lng': forms.NumberInput(attrs={'step': 'any'}),
        }
