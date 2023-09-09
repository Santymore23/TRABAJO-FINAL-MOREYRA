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
    mensajes = Mensaje.objects.filter(receptor = request.user)
    return render (request, "AppMensajes/MensajesList.html", {"mensajes": mensajes})

@login_required
def MensajeEnviar (request):
    if request.method == "POST":
        form = EnviarMensajeForm(request.POST)
        if form.is_valid():
            emisor_nombre = form.cleaned_data ['emisor']
            receptor_nombre = form.cleaned_data ['receptor']
            mensaje_contenido = form.cleaned_data ['contenido']
            try:
                emisor = User.objects.get (username = emisor_nombre)
                receptor = User.objects.get (username = receptor_nombre)
                mensaje = Mensaje(usuario= emisor, receptor = receptor, contenido = mensaje_contenido)
                mensaje.save()
                return redirect (MensajeMostrar)
            except User.DoesNotExist:
                raise Http404
    else:
        form = EnviarMensajeForm()
        return render (request, "AppMensajes/FormMensaje.html", {"form":form})
            
        
           
    