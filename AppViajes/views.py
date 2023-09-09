from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from AppViajes.models import *
from django.http import HttpResponse, Http404
from AppViajes.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio (request):
    avatar = None
    if request.user.is_authenticated:
        avatars = Avatar.objects.filter(user=request.user.id)
        if avatars:
            avatar = avatars[0].Imagen.url
    return render(request,"AppViajes/inicio.html", {"avatar":avatar})

def Acerca_de_mi (request):
    return render (request,"AppViajes/AcercaDeMi.html",{})


          #DESTINOS
class DestinoList(LoginRequiredMixin, ListView):
    context_object_name = "destino"
    queryset = Destinos.objects.all()
    template_name = "AppViajes/DestinosList.html"

class DestinoCrear(LoginRequiredMixin, CreateView):
    model = Destinos
    success_url = reverse_lazy("destinos_list")
    fields = ['Destino','Atraccion_principal','Descripcion', 'Imagen']
    template_name = "AppViajes/DestinosCrear.html"

class DestinoDetalle (LoginRequiredMixin, DetailView):
    model = Destinos
    context_object_name = "destino"
    template_name = "AppViajes/DestinosDetalle.html"
    
class DestinoBorrar (LoginRequiredMixin, DeleteView):
    model = Destinos
    success_url = reverse_lazy("destinos_list")
    context_object_name = "destino"
    template_name = "AppViajes/DestinosBorrar.html"

class DestinoEditar(LoginRequiredMixin, UpdateView):
    model = Destinos
    form_class = DestinosEditar
    success_url = reverse_lazy('destinos_list')
    context_object_name = 'destino'
    template_name = "AppViajes/DestinosEditar.html"

    
        #CONSEJOS    
class ConsejosList(LoginRequiredMixin, ListView):
    context_object_name = "consejo"
    queryset = Consejos.objects.all()
    template_name = "AppViajes/ConsejosList.html"

class ConsejosCrear(LoginRequiredMixin, CreateView):
    model = Consejos
    success_url = reverse_lazy("consejos_list")
    context_object_name = "consejo"
    fields = ['Destino','Comida','Hoteles', 'Transporte', 'Tips_generales']
    template_name = "AppViajes/ConsejosCrear.html"

class ConsejosDetalle(LoginRequiredMixin, DetailView):
    model = Consejos
    context_object_name = "consejo"
    template_name = "AppViajes/ConsejosDetalle.html"

class ConsejosBorrar(LoginRequiredMixin, DeleteView):
    model = Consejos 
    success_url = reverse_lazy("consejos_list")
    context_object_name = "consejo"
    template_name = "AppViajes/ConsejosBorrar.html"

class ConsejosEditar(LoginRequiredMixin, UpdateView):
    model = Consejos
    form_class = ConsejosEditar
    success_url = reverse_lazy('consejos_list')
    context_object_name = 'consejo'
    template_name = "AppViajes/ConsejosEditar.html" 
    
      
        #CONTACTOS

class ContactosList(LoginRequiredMixin, ListView):
    context_object_name = "contactos"
    queryset = Contactos.objects.all()
    template_name = "AppViajes/ContactosList.html"

class ContactosCrear(LoginRequiredMixin, CreateView):
    model = Contactos
    success_url = reverse_lazy("contactos_list")
    fields = ['Nombre','Apellido','Email','Telefono']
    template_name = "AppViajes/ContactosCrear.html"

class ContactosDetalle(LoginRequiredMixin, DetailView):
    model = Contactos
    context_object_name = "contacto"
    template_name = "AppViajes/ContactosDetalle.html"

class ContactosBorrar(LoginRequiredMixin, DeleteView):
    model = Contactos 
    success_url = reverse_lazy("contactos_list")
    context_object_name = "contacto"
    template_name = "AppViajes/ContactosBorrar.html"

class ContactosEditar(LoginRequiredMixin, UpdateView):
    model = Contactos
    form_class = ContactosEditar
    success_url = reverse_lazy('contactos_list')
    context_object_name = 'contacto'
    template_name = "AppViajes/ContactosEditar.html" 
       
        #PAGINAS WEB
class PaginasList(LoginRequiredMixin, ListView):
    context_object_name = "pagina"
    queryset = Paginas_web.objects.all()
    template_name = "AppViajes/PaginasList.html" 

class PaginasCrear(LoginRequiredMixin, CreateView):
    model = Paginas_web
    success_url = reverse_lazy("paginas_list")
    fields = ['Pagina','Motivo', 'Link']
    template_name = "AppViajes/PaginasCrear.html"

class PaginasDetalle(LoginRequiredMixin, DetailView):
    model = Paginas_web
    context_object_name = "pagina"
    template_name = "AppViajes/PaginasDetalle.html"

class PaginasBorrar(LoginRequiredMixin, DeleteView):
    model = Paginas_web 
    success_url = reverse_lazy("paginas_list")
    context_object_name = "pagina"
    template_name = "AppViajes/PaginasBorrar.html"

class PaginasEditar(LoginRequiredMixin, UpdateView):
    model = Paginas_web
    form_class = PaginasEditar
    success_url = reverse_lazy('paginas_list')
    context_object_name = 'pagina'
    template_name = "AppViajes/PaginasEditar.html" 

        #LOGIN
class LoginPagina(LoginView):
    template_name = 'AppViajes/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')
    
    def post (self,request):
        form = self.form_class(request, data=request.POST) 
        print ("POST")
        if form.is_valid():
            print ("VALID")
            info = form.cleaned_data
            username = info ["username"]
            password = info ["password"]
            user = authenticate(username= username, password= password)
            mensaje = f"Bienvenido de nuevo, { username }"
            if user is not None:
                login(request,user)
                return render (request,"AppViajes/inicio.html", {"mensaje":mensaje})
            else:
                return render (request,self.template_name,{"form":form, "mensaje": "datos invalidos"})
        else:
            return render (request, self.template_name,{"form": form, "mensaje": "datos invalidos"})
                
        #REGISTRO
class Registro (FormView):
    template_name = "AppViajes/Registro.html"
    form_class = RegistroUsuarioForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("inicio")
    
    def form_valid(self, form):
        user = form.save()
        mensaje = "Gracias por registrarte"
        if user is not None:
            login(self.request, user)
        return super(Registro, self).form_valid(form)
    
        #PERFIL
def EditarUsuario(request):
    usuario =request.user
    if request.method == "POST":
        form = EditarUsuarioForm (request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.username = info["username"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.nombre = info["nombre"]
            usuario.apellido = info["apellido"]
            usuario.save()
            mensaje = f" El usuario {usuario.username} ({usuario.nombre} {usuario.apellido}) ha cambiado sus datos"
            return render (request,"AppViajes/inicio.html", {"mensaje": mensaje})
        else:

            return render (request,"AppViajes/EditarPerfil.html", {"nombreusuario":usuario.username, "form":form})
    else:
        form = EditarUsuarioForm(instance=usuario)
        return render (request,"AppViajes/EditarPerfil.html",{"nombreusuario":usuario.username, "form": form})
     
    



        
    
    
    
    
    



   



