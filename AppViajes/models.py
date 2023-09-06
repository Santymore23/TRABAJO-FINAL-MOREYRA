from django.db import models

# Create your models here.
class Destinos (models.Model):
    Destino = models.CharField(max_length=100)
    Atraccion_principal = models.CharField(max_length=1000)
    Descripcion = models.CharField(max_length=20000, null = True)
    Imagen = models.ImageField(upload_to='destino_images/', null= True, blank= True)
    def __str__(self) -> str:
        return f"{self.Destino} -- {self.Atraccion_principal} -- {self.Descripcion} "

class Consejos (models.Model):
    Destino = models.CharField(max_length=100, null = True )
    Comida = models.CharField(max_length=1000)
    Hoteles = models.CharField(max_length=1000)
    Transporte = models.CharField(max_length=1000)
    Tips_generales = models.CharField(max_length=3000)
    def __str__(self) -> str:
        return f"{self.Destino} -- {self.Comida} -- {self.Hoteles} -- {self.Transporte} -- {self.Tips_generales} "

class Paginas_web (models.Model):
    Pagina = models.CharField (max_length=100)
    Motivo = models.CharField (max_length=1000)
    Link = models.CharField (max_length=1000, null = True)
    def __str__(self) -> str:
        return f"{self.Pagina} -- {self.Motivo} -- {self.Link} "
    
class Contactos (models.Model):
    Nombre = models.CharField (max_length=100)
    Apellido = models.CharField (max_length=100)
    Email = models.EmailField(max_length=100)
    Telefono = models.IntegerField ()
    def __str__(self) -> str:
        return f"{self.Nombre} -- {self.Apellido} -- {self.Email} -- {self.Telefono} "
    
    
      