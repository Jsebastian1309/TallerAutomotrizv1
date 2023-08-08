from django.db import models
from vehiculo.models import Vehiculo
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

def alphabetic_validator(value):
    if not value.isalpha():
        raise ValidationError('El campo debe contener solo letras.')

class Mantenimiento(models.Model):
    historial_mantenimiento= models.CharField(max_length=45,verbose_name="Historial de mantenimiento",blank=False,validators=[alphabetic_validator])
    historial_reparaciones= models.CharField(max_length=45,verbose_name="Historial de reparaciones",blank=False,validators=[alphabetic_validator])
    class EstadoMantenimiento(models.TextChoices):
        Aplazado='Aplazado',_("Aplazado")
        Iniciado='Iniciado',_("Iniciado")
        Terminado='Terminado',_("Terminado")
    estado_mantenimiento=models.CharField(max_length=10,choices=EstadoMantenimiento.choices,default=EstadoMantenimiento.Iniciado,verbose_name="Estado Mantenimiento")
   
    class Meta:
        verbose_name_plural = "Mantenimientos"
        
class Cita(models.Model):
    fecha_cita= models.DateField(verbose_name="Fecha de cita",help_text="DD/MM/AAAA",blank=False)
    hora_cita= models.TimeField(max_length=15, verbose_name="Hora de cita", help_text="HH/MM/SS",blank=False)
    contacto = models.CharField(max_length=10,verbose_name="Contacto",default='',blank=False)    
    descripcion_cita= models.CharField(max_length=50,verbose_name="Descripcion de la cita",default='',blank=False,validators=[alphabetic_validator])
    class EstadoCita(models.TextChoices):
        Programada='Programada',_("Programada")
        Pospuesta='Pospuesta',_("Pospuesta")
        Cancelada='Cancelada',_("Cancelada")
        Enproceso='En proceso',_("Enproceso")
        Finalizada='Finalizada',_("Finalizada")
    estado_cita=models.CharField(max_length=10,choices=EstadoCita.choices,default=EstadoCita.Programada,verbose_name="Estado")
   
     
    class Meta:
        verbose_name_plural = "Citas"