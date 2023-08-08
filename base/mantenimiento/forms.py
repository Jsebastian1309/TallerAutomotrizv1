from django import forms

from django.forms import ModelForm, widgets
from mantenimiento.models import Mantenimiento,Cita

class MantenimientoForm(ModelForm):
    
    class Meta:
        model = Mantenimiento
        fields = "__all__"
        
       
class MantenimientoUpdateForm(ModelForm):
    
    class Meta:
        model = Mantenimiento
        fields = "__all__"
        
        
class CitaForm(ModelForm):
    class Meta:
        model = Cita
        fields = "__all__"
        widgets={
            'fecha_cita': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'hora_cita': forms.TimeInput(attrs={'type': 'time'})
        }
       

class CitaUpdateForm(ModelForm):
    class Meta:
        model = Cita
        fields = "__all__"
        widgets={
            'fecha_cita': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'hora_cita': forms.TimeInput(attrs={'type': 'time'})
        }