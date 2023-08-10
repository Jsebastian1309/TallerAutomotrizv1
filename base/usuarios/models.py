from django.db import models
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
    correo_arl= models.EmailField(max_length=40,verbose_name="Correo Arl",blank=False)
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
    
    nombreusuario = models.CharField(max_length=20, verbose_name="Nombre De Usuario", blank=False, default='')
    correo_personal = models.EmailField(max_length=50, verbose_name="Correo Personal", blank=False, default='')
    contraseña = models.CharField(max_length=20, verbose_name="Contraseña", blank=False, default='')
    confirmarcontraseña = models.CharField(max_length=20, verbose_name="Confirmar Contraseña", blank=False, default='')
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
    
    def __str__(self):
        return f"({self.identificacion}) {self.nombres} {self.apellidos}"

    def clean(self):
        if self.contraseña != self.confirmarcontraseña:
            raise ValidationError("Las contraseñas no coinciden.")

        if self.tipo_usuario in ['Administrador', 'Mecanico', 'Secretaria']:
            if not self.rh:
                raise ValidationError('El campo Factor RH es obligatorio para este tipo de usuario.')
            if not self.direccion:
                raise ValidationError('El campo Dirección es obligatorio para este tipo de usuario.')
            if not self.contraseña:
                raise ValidationError('El campo Contraseña es obligatorio para este tipo de usuario.')
            if not self.confirmarcontraseña:
                raise ValidationError('El campo Confirmar Contraseña es obligatorio para este tipo de usuario.')
        elif self.tipo_usuario == 'Cliente':
            if self.arl is not None:
                raise ValidationError('Un usuario de tipo Cliente no puede tener una ARL.')
            if self.direccion:
                raise ValidationError('Un usuario de tipo Cliente no puede tener una dirección.')

    class Meta:
        verbose_name_plural = "usuarios"
         
 

