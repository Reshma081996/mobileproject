from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, forms, PasswordInput
from django.forms import TextInput
from django import forms
from django.db.models import CharField

from .models import Product,Orders


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        # image = forms.ImageField(widget=forms.FileInput())
        fields = ['product_name', 'price', 'specs', 'image']


        widgets = {
            'product_name': TextInput(attrs={"class": "form-control"}),
            'price': TextInput(attrs={"class": "form-control"}),
            'specs': TextInput(attrs={"class": "form-control"}),

        }

class UserRegForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email','password1','password2',]
        widgets = {
            'username': TextInput(attrs={"class": "form-control"}),
            'first_name':TextInput(attrs={"class":"form-control"}),
            'last_name': TextInput(attrs={"class": "form-control"}),
            'email': TextInput(attrs={"class": "form-control"}),

        }
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))


#userside

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['product','address','user']
        widgets = {
            'product': TextInput(attrs={"class": "form-control"}),
            'address': TextInput(attrs={"class": "form-control"}),
            'user': TextInput(attrs={"class": "form-control"}),
        }
