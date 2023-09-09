from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    usuario = models.ForeignKey (User, on_delete=models.CASCADE, related_name= "emisor")
    receptor = models.ForeignKey (User, on_delete=models.CASCADE, related_name= "receptor",null=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add= True)
    class Meta:
        ordering = ['fecha']


