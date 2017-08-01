from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First and last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    marketing = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Marketing'}))
    captcha = CaptchaField()
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))