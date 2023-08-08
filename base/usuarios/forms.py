from django import forms

from django.forms import ModelForm,widgets
from usuarios.models import Usuario,Arl

# Formulario Usuario
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["estado",]
        widgets={
            'fecha_registro': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
        
class UsuarioUpdateForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["documento","rh","fecha_registro"]
        


class ArlForm(ModelForm):
    class Meta:
        model = Arl
        fields = "__all__"
        exclude = ["estado"]
        widgets={
            'fecha_inicioafi': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_vencimientoafi': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')

        }
        
class ArlUpdateForm(ModelForm):
    
    class Meta:
        model = Arl
        fields = "__all__"
        exclude=["fecha_inicioafi"]
        widgets={
            'fecha_inicioafi': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_vencimientoafi': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')

        }
    
    