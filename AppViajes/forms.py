from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *


class DestinosForm (forms.Form):
    Destino = forms.CharField(max_length=100)
    Atraccion_principal = forms.CharField(max_length=1000) 

class ConsejosForm (forms.Form):    
    Destino = forms.CharField(max_length=100)
    Comida = forms.CharField(max_length=1000)
    Hoteles = forms.CharField(max_length=1000)
    Transporte = forms.CharField(max_length=1000)
    Tips_generales = forms.CharField(max_length=3000)

class PaginasForm (forms.Form):
    Pagina = forms.CharField (max_length=100)
    Motivo = forms.CharField (max_length=1000)
    
class ContactosForm (forms.Form):
    Nombre = forms.CharField (max_length=100)
    Apellido = forms.CharField (max_length=100)
    Email = forms.EmailField(max_length=100)
    Telefono = forms.IntegerField ()

class DestinosEditar(forms.ModelForm):
    class Meta:
        model = Destinos
        fields = ('Destino', 'Atraccion_principal', 'Descripcion')

        widgets = {
            'Destino' : forms.TextInput(),
            'Atraccion_principal' : forms.TextInput(),
            'Descripcion' : forms.TextInput(),
                }

class ConsejosEditar (forms.ModelForm):
    class Meta:
        model = Consejos
        fields = ('Destino', 'Comida', 'Hoteles', 'Transporte', 'Tips_generales')

        widgets = {
            'Destino' : forms.TextInput(),
            'Comida' : forms.TextInput(),
            'Hoteles' : forms.TextInput(),
            'Transporte' : forms.TextInput(),
            'Tips_generales' : forms.TextInput(),
            }

class ContactosEditar (forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ('Nombre', 'Apellido', 'Email', 'Telefono')

        widgets = {
            'Nombre' : forms.TextInput(),
            'Apellido' : forms.TextInput(),
            'Email' : forms.EmailInput(),
            'Telefono' : forms.TextInput(),
        }
        
class PaginasEditar (forms.ModelForm):
    class Meta:
        model = Paginas_web
        fields = ('Pagina', 'Motivo', 'Link')

        widgets = {
            'Pagina' : forms.TextInput(),
            'Motivo' : forms.TextInput(),
            'Link' : forms.TextInput(),
        }


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        help_texts = {campo: "" for campo in fields}

class EditarUsuarioForm (UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    nombre = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput)
    apellido = forms.CharField(max_length=50, label='Apellido', widget=forms.TextInput)
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2','nombre','apellido')
        help_texts = {campo: "" for campo in fields}

        
    
        

        

    
    
    
    


    

