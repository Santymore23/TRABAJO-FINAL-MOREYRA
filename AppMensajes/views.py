from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from django.http import Http404
from .forms import *
# Create your views here.

@login_required
def enviar_mensaje (request):
    if request.method == "POST":
        form = EnviarMensajeForm
        if form.is_valid():
           
    