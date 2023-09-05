from django.db import models

# Create your models here.
class Destinos (models.Model):
    Destino = models.CharField(max_length=100)
    Atraccion_principal = models.CharField(max_length=1000)

class Consejos (models.Model):
    Destino = models.CharField(max_length=100, null = True )
    Comida = models.CharField(max_length=1000)
    Hoteles = models.CharField(max_length=1000)
    Transporte = models.CharField(max_length=1000)
    Tips_generales = models.CharField(max_length=3000)

class Paginas_web (models.Model):
    Pagina = models.CharField (max_length=100)
    Motivo = models.CharField (max_length=1000)
    
class Contactos (models.Model):
    Nombre = models.CharField (max_length=100)
    Apellido = models.CharField (max_length=100)
    Email = models.EmailField(max_length=100)
    Telefono = models.IntegerField ()
    
    
      