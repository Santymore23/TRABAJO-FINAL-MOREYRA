from django.shortcuts import render
from AppViajes.models import *
from django.http import HttpResponse
from AppViajes.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

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
    fields = ['Destino','Atraccion_principal','Descripcion', 'Imagen']
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
class ConsejosList(ListView):
    context_object_name = "consejo"
    queryset = Consejos.objects.all()
    template_name = "AppViajes/ConsejosList.html"

class ConsejosCrear(CreateView):
    model = Consejos
    success_url = reverse_lazy("consejos_list")
    fields = ['Destino','Comida','Hoteles', 'Transporte', 'Tips_generales']
    template_name = "AppViajes/ConsejosCrear.html"

class ConsejosDetalle(DetailView):
    model = Consejos
    context_object_name = "consejo"
    template_name = "AppViajes/ConsejosDetalle.html"

class ConsejosBorrar(DeleteView):
    model = Consejos 
    success_url = reverse_lazy("consejos_list")
    context_object_name = "consejo"
    template_name = "AppViajes/ConsejosBorrar.html"
    
    
    
    
    
    
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

class PaginasDetalle(DetailView):
    model = Paginas_web
    context_object_name = "pagina"
    template_name = "AppViajes/PaginasDetalle.html"

class PaginasBorrar(DeleteView):
    model = Paginas_web 
    success_url = reverse_lazy("paginas_list")
    context_object_name = "pagina"
    template_name = "AppViajes/PaginasBorrar.html"

        #LOGIN
def LoginPagina(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password = contraseña)
            if user is not None:
                login(request,user)
                return render(request,"AppViajes/inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppViajes/inicio.html",{"mensaje":"Datos invalidos"})
        else:
            return render(request,"AppViajes/inicio.html",{"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()
    return render (request,"AppViajes/Login.html",{"form": form})
    
                
            
    
    
 
        
        #REGISTRO
class Registro (FormView):
    template_name = "AppViajes/Registro.html"
    form_class = RegistroUsuarioForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("inicio")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registro, self).form_valid(form)

        
    
    
    
    
    



   



