from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from usuarios.models import Usuario
import datetime


def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError('El campo debe contener solo números.')
def alphabetic_validator(value):
    if not value.isalpha():
        raise ValidationError('El campo debe contener solo letras.')
class Venta(models.Model):
    identificacion=models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, verbose_name=" Nombre Cliente",default=None,limit_choices_to={'tipo_usuario': Usuario.TipoUsuario.CLIENTE})    
    fecha_venta= models.DateTimeField(verbose_name="Fecha de Venta", help_text="DD/MM/AAAA", default=datetime.date.today)
    cliente= models.CharField(max_length=25, verbose_name="Cliente",default='',blank=False,validators=[alphabetic_validator])
    vehiculo= models.CharField(max_length=10, verbose_name="Vehiculo")
    class formaPago(models.TextChoices):
        DEBITO='Debito',_("Tarjeta de Debito")
        CREDITO='Credito',_("Tarjeta de Credito")
        EFECTIVO='Efectivo',_("Efectivo")
    forma_pago= models.CharField(max_length=10, choices=formaPago.choices , verbose_name="Tipo de Pago")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=3,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
     
    class Meta:
        verbose_name_plural ="Ventas"


