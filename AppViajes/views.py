from django.shortcuts import render
from AppViajes.models import *
from django.http import HttpResponse
from AppViajes.forms import *
# Create your views here.

def inicio (request):
    return render(request,"AppViajes/inicio.html")

def Acerca_de_mi (request):
    return render (request,"AppViajes/AcercaDeMi.html",{})

def destinos (request):
    if request.method == "POST":
        formulario = DestinosForm (request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            lugar = info["Destino"]
            atraccion = info ["Atraccion_principal"]
            destino = Destinos(Destino = lugar, Atraccion_principal = atraccion)
            destino.save()
            mensaje = "Destino Cargado"
        else:
            mensaje = "Destino no cargado"
        viajes = Destinos.objects.all()
        formulario_destino = DestinosForm()
        return render (request,"AppViajes/destinos.html",{"formulario":formulario_destino, "mensaje": mensaje, "destinos": viajes})
    else:
        viajes = Destinos.objects.all()
        formulario_destino = DestinosForm()
        return render (request,"Appviajes/destinos.html",{"formulario": formulario_destino, "destinos": viajes})

def eliminarDestino(request, id):
    destino = Destinos.objects.get(id = id)
    destino.delete()
    viajes = Destinos.objects.all()
    formulario_destino = DestinosForm()
    mensaje = "Destino eliminado"
    return render (request,"AppViajes/destinos.html",{"formulario":formulario_destino, "mensaje": mensaje, "destinos": viajes})

def editarDestino (request, id):
    destino = Destinos.objects.get(id = id)
    if request.method == "POST":
         formulario = DestinosForm (request.POST)
         if formulario.is_valid():
            info = formulario.cleaned_data
            destino.lugar = info["Destino"]
            destino.atraccion = info ["Atraccion_principal"]
            destino.save()
            mensaje = "Destino editado"
            nuevo = Destinos.objects.all()
            formulario_destino = DestinosForm()
            return render (request,"AppViajes/editarDestino.html",{"formulario":formulario_destino, "mensaje": mensaje, "destino": nuevo})
            
    else:
        formulario_destino = DestinosForm(initial={"Destino": destino.Destino, "Atraccion_principal": destino.Atraccion_principal})    
        return render (request, "Appviajes/destinos.html",{"formulario": formulario_destino, "destino": destino})

    
def consejos (request):
    if request.method == "POST":
        formulario = ConsejosForm (request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            destino = info["Destino"]
            comida = info ["Comida"]
            hoteles = info ["Hoteles"]
            transporte = info ["Transporte"]
            tips = info ["Tips_generales"]
            consejo = Consejos(Destino = destino, Comida = comida, Hoteles = hoteles, Transporte = transporte, Tips_generales = tips)
            consejo.save()
            return render (request,"AppViajes/Consejos.html",{"mensaje":"Consejo cargado"})
        return render (request,"AppViajes/Consejos.html",{"mensaje":"El consejo no fue cargado"})
    else:
        formulario_consejo = ConsejosForm()
        return render (request,"AppViajes/Consejos.html",{"formulario":formulario_consejo})

def contactos (request):
    if request.method == "POST":
        formulario = ContactosForm (request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nombre = info["Nombre"]
            apellido = info ["Apellido"]
            email = info ["Email"]
            telefono = info ["Telefono"]
            contacto = Contactos(Nombre = nombre, Apellido = apellido, Email = email, Telefono = telefono)
            contacto.save()
            mensaje = "Contacto creado"
        else:
            mensaje = "El contacto no fue cargado"
        formulario_contactos= ContactosForm()
        return render (request,"AppViajes/Contactos.html",{"mensaje":mensaje})
    else:
        formulario_contactos = ContactosForm()
        return render (request,"AppViajes/Contactos.html",{"formulario":formulario_contactos})

def paginas_web(request):
    if request.method == "POST":
        formulario = PaginasForm (request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pagina = info["Pagina"]
            motivo = info ["Motivo"]
            pagina_web = Paginas_web(Pagina = pagina, Motivo = motivo)
            pagina_web.save()
            return render (request,"AppViajes/Paginas_web.html",{"mensaje":"Pagina cargada"})
        return render (request,"AppViajes/Paginas_web.html",{"mensaje":"La pagina no fue cargada"})
    else:
        formulario_paginas= PaginasForm()
        return render (request,"AppViajes/Paginas_web.html",{"formulario":formulario_paginas})



   



