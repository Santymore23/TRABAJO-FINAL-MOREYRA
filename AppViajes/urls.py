from django.urls import path, include
from AppViajes.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name= "inicio"),
    
    path("infoPersonal/",Acerca_de_mi, name= "Acerca_de_mi"),
    
    path("consejos/list/",ConsejosList.as_view(), name = "consejos_list"),
    path("consejos/nuevo/", ConsejosCrear.as_view(), name = "consejos_crear"),
    path("consejosDetalle/<pk>", ConsejosDetalle.as_view(), name = "consejos_detalles"),
    path("consejosBorrar/<pk>", ConsejosBorrar.as_view(), name = "consejos_borrar"),
    path("consejosEditar/<pk>", ConsejosEditar.as_view(), name = "consejos_editar"),
    
    path("paginas/list/",PaginasList.as_view(), name = "paginas_list"),
    path("paginas/nuevo/",PaginasCrear.as_view(), name = "paginas_crear"),
    path("paginasDetalle/<pk>", PaginasDetalle.as_view(), name = "paginas_detalles"),
    path("paginasBorrar/<pk>", PaginasBorrar.as_view(), name = "paginas_borrar"),
    path("paginasEditar/<pk>", PaginasEditar.as_view(), name = "paginas_editar"),
    
    path("contactos/list/",ContactosList.as_view(), name = "contactos_list"),
    path("contactos/nuevo/",ContactosCrear.as_view(),name = "contactos_crear"),
    path("contactosDetalle/<pk>",ContactosDetalle.as_view(), name = "contactos_detalles"),
    path("contactosBorrar/<pk>",ContactosBorrar.as_view(), name = "contactos_borrar"),
    path("contactosEditar/<pk>",ContactosEditar.as_view(), name = "contactos_editar"),
    
    path("destinos/list/",DestinoList.as_view(), name = "destinos_list"),
    path("destinos/nuevo/",DestinoCrear.as_view(), name = "destinos_crear"),
    path("destinosDetalle/<pk>", DestinoDetalle.as_view(), name = "destinos_detalles"),
    path("destinosBorrar/<pk>",DestinoBorrar.as_view(), name = "destinos_borrar"),
    path("destinosEditar/<pk>",DestinoEditar.as_view(), name = "destinos_editar"),
    
    path("registro/", Registro.as_view(), name = "registro"),
    
    path("loginpagina/",LoginPagina.as_view(), name = "Login"),
    
    path("logout/",LogoutView.as_view(template_name = "AppViajes/Logout.html"), name = "Logout"),
    
    path("perfilesList/",PerfilesList.as_view(), name = "perfiles_list"),
    path("perfilesBorrar/<pk>",PerfilesBorrar.as_view(), name = "perfiles_borrar"),
    path("editarPerfil/<pk>",EditarUsuario.as_view(), name = "Editar"),
         
]
