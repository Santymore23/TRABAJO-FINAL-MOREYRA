from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        help_texts = {campo: "" for campo in fields}
        

    
    
    
    


    

