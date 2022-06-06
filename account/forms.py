from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='LOGIN')
    password = forms.CharField(label='HASŁO' ,widget= forms.PasswordInput)


