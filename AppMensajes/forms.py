from django import forms
from django.contrib.auth.models import User 
from .models import *

class EnviarMensajeForm(forms.Form):
    emisor = forms.CharField (max_length=70,label="Ingrese su nombre de usuario")
    receptor = forms.CharField (max_length=70, label="Ingresar receptor")
    mensaje = forms.Textarea ()
    