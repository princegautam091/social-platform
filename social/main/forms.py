from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.FloatField()

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    mobile = forms.FloatField()
    

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile']





class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['image']

