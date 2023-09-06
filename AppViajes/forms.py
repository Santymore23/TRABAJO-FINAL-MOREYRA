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

class RegistroUsuarioForm (forms.Form):
    Username =forms.CharField (max_length=20, label="Ingresar nombre de usuario")
    Email = forms.EmailField(label="Ingresar email")
    Password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    Password2 = forms.CharField(label=" Reingresar contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['Username', 'Email', 'Password1', 'Password2']
        help_texts ={k:"" for k in fields}
    
    
    
    


    

