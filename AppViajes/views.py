from django.shortcuts import render
from AppViajes.models import *
from django.http import HttpResponse
from AppViajes.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def inicio (request):
    return render(request,"AppViajes/inicio.html")

def Acerca_de_mi (request):
    return render (request,"AppViajes/AcercaDeMi.html",{})


          #DESTINOS
class DestinoList(ListView):
    context_object_name = "destino"
    queryset = Destinos.objects.all()
    template_name = "AppViajes/DestinosList.html"

class DestinoCrear(CreateView):
    model = Destinos
    success_url = reverse_lazy("destinos_list")
    fields = ['Destino','Atraccion_principal','Descripcion']
    template_name = "AppViajes/DestinosCrear.html"

class DestinoDetalle (DetailView):
    model = Destinos
    context_object_name = "destino"
    template_name = "AppViajes/DestinosDetalle.html"
    
class DestinoBorrar (DeleteView):
    model = Destinos
    success_url = reverse_lazy("destinos_list")
    context_object_name = "destino"
    template_name = "AppViajes/DestinosBorrar.html"
    
    



        #CONSEJOS    
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
    
    
    
        #CONTACTOS

class ContactosList(ListView):
    context_object_name = "contactos"
    queryset = Contactos.objects.all()
    template_name = "AppViajes/ContactosList.html"

class ContactosCrear(CreateView):
    model = Contactos
    success_url = reverse_lazy("contactos_list")
    fields = ['Nombre','Apellido','Email','Telefono']
    template_name = "AppViajes/ContactosCrear.html"

class ContactosDetalle(DetailView):
    model = Contactos
    context_object_name = "contacto"
    template_name = "AppViajes/ContactosDetalle.html"

class ContactosBorrar(DeleteView):
    model = Contactos 
    success_url = reverse_lazy("contactos_list")
    context_object_name = "contacto"
    template_name = "AppViajes/ContactosBorrar.html"
    
    
    
    
            #PAGINAS WEB
class PaginasList(ListView):
    context_object_name = "pagina"
    queryset = Paginas_web.objects.all()
    template_name = "AppViajes/PaginasList.html" 

class PaginasCrear(CreateView):
    model = Paginas_web
    success_url = reverse_lazy("paginas_list")
    fields = ['Pagina','Motivo', 'Link']
    template_name = "AppViajes/PaginasCrear.html"



   



