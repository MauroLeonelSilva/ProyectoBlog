from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EditarPostForm(forms.Form):
    titulo= forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=150)
    cuerpo=forms.CharField(widget=forms.Textarea(attrs={'id':"editor1" ,'name':'body', 'rows':7, 'cols':60}))
    autor=forms.CharField(max_length=50)
    

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    numero_telefono = forms.IntegerField()
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':4, 'cols':30}))

class RegistroUsuarioForm(UserCreationForm):
    
    email= forms.EmailField()
    password1= forms.CharField(label="ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="repita contraseña", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model = User
        fields = [ "email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")