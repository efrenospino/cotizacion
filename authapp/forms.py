from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(forms.Form):
	usuario =forms.CharField(widget=forms.TextInput())
	password=forms.CharField(widget=forms.PasswordInput(render_value=False))

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'is_staff']
        widgets = {
            'password': forms.PasswordInput(),
        }
