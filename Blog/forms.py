from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog


class DummyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "cols": 20}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))


class CreateUser(UserCreationForm):
    password1 = forms.CharField(label="Enter Your Password",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Re-Enter Your Password",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", 'password1', 'password2', 'email']
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class LogUser(AuthenticationForm):
    username = forms.CharField(label="Enter Your Username",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Enter Your Password",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', "Description"]
        widgets = {
            "Title": forms.TextInput(attrs={"class": "form-control"}),
            "Description": forms.Textarea(attrs={"class": "form-control", "cols": 30, "rows": 8}),

        }
        labels = {
            "Title": "Enter The Title For Your Post",
            "Description": "Enter The Description of Your Post",
        }
