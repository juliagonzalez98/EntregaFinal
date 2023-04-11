from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from user.models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Ingrese su nueva contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    name = forms.CharField()


    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name']
    

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]

