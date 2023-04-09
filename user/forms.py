from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from user.models import Avatar


class UserRegisterForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField()
    descripcion = forms.CharField()
 
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2', 'avatar', 'descripcion']
        help_texts = {k:"" for k in fields}
    
    def clean_avatar(self):
       avatar = self.cleaned_data.get("avatar")
       if not avatar:
        raise forms.ValidationError("Debe seleccionar una imagen para su avatar.")
       return avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Ingrese su nueva ontraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    name = forms.CharField()
    imagen = forms.ImageField()
    descripcion = forms.CharField(label="Ingrese una breve descripción")
    

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name', 'imagen', 'descripcion']

