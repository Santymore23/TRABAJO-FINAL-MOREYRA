from django.urls import path
from AppViajes.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("infoPersonal/",Acerca_de_mi, name= "Acerca_de_mi"),
    path("consejos/",consejos,name= "consejos"),
    path("destinos/",destinos,name = "destinos"),
    path("contactos/",contactos,name = "contactos"),
    path("paginas/",paginas_web, name = "paginas_web"),
    path("eliminarDestino/<id>",eliminarDestino, name= "eliminarDestino"),
    path("editarDestino/<id>",editarDestino, name = "editarDestino"),
    
    
    
]
