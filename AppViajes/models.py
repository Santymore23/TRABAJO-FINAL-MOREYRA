from django.db import models

# Create your models here.
class Destinos (models.Model):
    Destino = models.CharField(max_length=100)
    Atraccion_principal = models.CharField(max_length=1000)
    
class Acerca_de_mi (models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Edad = models.IntegerField ()
    Info = models.CharField(max_length=1000)

class Consejos (models.Model):
    Comida = models.CharField(max_length=1000)
    Hoteles = models.CharField(max_length=1000)
    Tips_generales = models.CharField(max_length=3000) 
    
      