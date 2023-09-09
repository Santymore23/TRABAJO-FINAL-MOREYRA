from django import forms
from django.contrib.auth.models import User 
from .models import *

class EnviarMensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor','contenido']
    emisor = forms.ModelChoiceField(queryset=User.objects.all(), widget= forms.HiddenInput(), required= False)
    
    
    