from django import forms

from django.forms import ModelForm, widgets
from servicio.models import Servicio,Detalle_servicio

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
       
       
class ServicioUpdateForm(ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        
        
class Detalle_servicioForm(ModelForm):
    class Meta:
        model = Detalle_servicio
        fields = "__all__"
        widgets={
            'fecha_servicio': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class Detalle_servicioUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_servicio
        fields = "__all__"
        exclude=["kilometraje"]
        widgets={
            'fecha_servicio': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }