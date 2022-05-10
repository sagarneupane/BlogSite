from django import forms


class DummyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":3,"cols":20}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
