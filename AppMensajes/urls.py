from django.urls import path
from . views import *

urlpatterns = [
    path ("mensajes/mostrar", MensajeMostrar, name = "mensaje_mostrar"),
    path ("mensajes/enviar",MensajeEnviar, name = "mensajes_enviar"),
    
]