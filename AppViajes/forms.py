from django import forms



class DestinosForm (forms.Form):
    Destino = forms.CharField(max_length=100)
    Atraccion_principal = forms.CharField(max_length=1000) 

class ConsejosForm (forms.Form):    
    Destino = forms.CharField(max_length=100)
    Comida = forms.CharField(max_length=1000)
    Hoteles = forms.CharField(max_length=1000)
    Transporte = forms.CharField(max_length=1000)
    Tips_generales = forms.CharField(max_length=3000)

class PaginasForm (forms.Form):
    Pagina = forms.CharField (max_length=100)
    Motivo = forms.CharField (max_length=1000)
    
class ContactosForm (forms.Form):
    Nombre = forms.CharField (max_length=100)
    Apellido = forms.CharField (max_length=100)
    Email = forms.EmailField(max_length=100)
    Telefono = forms.IntegerField ()
    
    


    

