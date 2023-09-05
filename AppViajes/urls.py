from django.urls import path
from AppViajes.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("infoPersonal/",Acerca_de_mi, name= "Acerca_de_mi"),
    path("consejos/",consejos,name= "consejos"),
    
    path("paginas/list/",PaginasList.as_view(), name = "paginas_list"),
    path("paginas/nuevo/",PaginasCrear.as_view(), name = "paginas_crear"),
    
    
    path("contactos/list/",ContactosList.as_view(), name = "contactos_list"),
    path("contactos/nuevo/",ContactosCrear.as_view(),name = "contactos_crear"),
    path("contactosDetalle/<pk>",ContactosDetalle.as_view(), name = "contactos_detalles"),
    path("contactosBorrar/<pk>",ContactosBorrar.as_view(), name = "contactos_borrar"),
    
    path("destinos/list/",DestinoList.as_view(), name = "destinos_list"),
    path("destinos/nuevo/",DestinoCrear.as_view(), name = "destinos_crear"),
    path("destinosDetalle/<pk>", DestinoDetalle.as_view(), name = "destinos_detalles"),
    path("destinosBorrar/<pk>",DestinoBorrar.as_view(), name = "destinos_borrar")
    
    
]
