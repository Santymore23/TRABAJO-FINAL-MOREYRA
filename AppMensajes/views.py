from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from django.http import Http404
from .forms import *
# Create your views here.

@login_required
def MensajeMostrar (request):
    mensajes_recibidos = Mensaje.objects.filter(receptor = request.user)
    mensajes_enviados = Mensaje.objects.filter(usuario = request.user)
    mensajes = list (mensajes_recibidos) + list (mensajes_enviados)
    mensajes.sort (key=lambda x:x.fecha)
    return render (request, "AppMensajes/MensajesList.html", {"mensajes_recibidos": mensajes_recibidos, "mensajes_enviados": mensajes_enviados, "mensajes": mensajes})


@login_required
def MensajeEnviar (request):
    if request.method == "POST":
        emisor = request.user
        form = EnviarMensajeForm(request.POST)
        form.fields ['emisor'].initial = emisor.id
        if form.is_valid():
            receptor_nombre = form.cleaned_data ['receptor']
            mensaje_contenido = form.cleaned_data ['mensaje']
            try:
                receptor = User.objects.get (username = receptor_nombre)
                mensaje = Mensaje(usuario= emisor, receptor = receptor, contenido = mensaje_contenido)
                mensaje.save()
                return redirect ("mensaje_mostrar")
            except User.DoesNotExist:
                raise Http404
    else:
        form = EnviarMensajeForm()
        return render (request, "AppMensajes/FormMensaje.html", {"form":form})
            
        
           
    