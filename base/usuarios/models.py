from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError('El campo debe contener solo números.')
def alphabetic_validator(value):
    if not all(char.isalpha() or char.isspace() for char in value):
            raise ValidationError('El campo debe contener solo letras y espacios.')

class Arl(models.Model):
    nombre_arl= models.CharField(max_length=20,verbose_name="Nombre Arl",blank=False,validators=[alphabetic_validator])
    telefono_arl= models.CharField(max_length=13,verbose_name="Telefono Arl",validators=[numeric_validator],blank=False)
    correo_arl= models.EmailField(max_length=50,verbose_name="Correo Arl",blank=False)
    fecha_inicioafi= models.DateField(verbose_name="Fecha de Inicio Afiliacion", help_text="MM/DD/AAAA")
    fecha_vencimientoafi= models.DateField(verbose_name="Fecha De Vencimiento Afiliacion", help_text="MM/DD/AAAA")
    
    def clean(self):
        if self.fecha_inicioafi == self.fecha_vencimientoafi:
            raise ValidationError("Las fechas de inicio y vencimiento de afiliación no pueden ser iguales.")

    def __str__(self):
        return self.nombre_arl
    
    class Meta:
        verbose_name_plural ="arls"    
        
class Usuario(models.Model):
    class TipoUsuario(models.TextChoices):
        ADMINISTRADOR = 'Administrador', _("Administrador")
        SECRETARIA = 'Secretaria', _("Secretaria")
        MECANICO = 'Mecanico', _("Mecanico")
        CLIENTE = 'Cliente', _("Cliente")
    tipo_usuario = models.CharField(max_length=13, choices=TipoUsuario.choices, verbose_name="Tipo Usuario", default=TipoUsuario.CLIENTE, blank=False)
    nombres = models.CharField(max_length=30, verbose_name="Nombres", default='', blank=False, validators=[alphabetic_validator])
    apellidos = models.CharField(max_length=30, verbose_name="Apellidos", default='', blank=False, validators=[alphabetic_validator])
    class TipoIdentificacion(models.TextChoices):
        CEDULA = 'Cédula Ciudadania', _("Cédula Ciudadania")
        TARJETA = 'Tarjeta Identidad', _("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA = 'Cédula Extrangería', _("Cédula de Extrangería")
    tipo_identificacion = models.CharField(max_length=18, choices=TipoIdentificacion.choices, verbose_name="Tipo de identificacion", default=TipoIdentificacion.CEDULA, blank=False)
    identificacion = models.CharField(max_length=10, verbose_name="Identificacion", default='', validators=[numeric_validator], unique=True, blank=False)
    telefono = models.CharField(max_length=11, verbose_name="Telefono", validators=[numeric_validator], blank=False)
    telefono2 = models.CharField(max_length=11, verbose_name="Segundo Telefono", validators=[numeric_validator], blank=False)
    
    nombreusuario = models.CharField(max_length=20, verbose_name="Nombre De Usuario", blank=True, default='')
    correo_personal = models.EmailField(max_length=50, verbose_name="Correo Personal", blank=True, default='')
    contraseña = models.CharField(max_length=20, verbose_name="Contraseña", blank=True, default='')
    confirmarcontraseña = models.CharField(max_length=20, verbose_name="Confirmar Contraseña", blank=True, default='')
    direccion = models.CharField(max_length=50, verbose_name="Dirección", blank=True)
    fecha_registro = models.DateField(verbose_name="Fecha de Registro", help_text="MM/DD/AAAA", auto_now_add=True,)
    class RH(models.TextChoices):
        OP = 'OP', _("O+")
        ON = 'ON', _("O-")
        AP = 'AP', _("A+")
        AN = 'AN', _("A-")
        BP = 'BP', _("B+")
        BN = 'BN', _("B-")
        ABP = 'ABP', _("AB+")
        ABN = 'ABN', _("AB-")
    rh = models.CharField(max_length=3, choices=RH.choices, verbose_name="Factor RH", blank=True)
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado", blank=False)
    arl = models.ForeignKey(Arl, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ARL")
    
    def save(self, *args, **kwargs):
        super(Usuario, self).save(*args, **kwargs)
        user = User.objects.create_user(username=self.nombreusuario, password=self.contraseña)
        user.first_name = self.nombres
        user.last_name = self.apellidos
        user.email = self.correo_personal
        user.save()
        if self.tipo_usuario == Usuario.TipoUsuario.ADMINISTRADOR:
            grupo = Group.objects.get(name='Administrador')
        elif self.tipo_usuario == Usuario.TipoUsuario.SECRETARIA:
            grupo = Group.objects.get(name='Secretaria')
        elif self.tipo_usuario == Usuario.TipoUsuario.MECANICO:
            grupo = Group.objects.get(name='Mecanico')
        else:
            grupo = Group.objects.get(name='Cliente')
        user.groups.add(grupo)
    def __str__(self):
        return f"({self.identificacion}) {self.nombres} {self.apellidos}"

   
    class Meta:
        verbose_name_plural = "usuarios"
         
 

