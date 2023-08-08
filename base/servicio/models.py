from django.db import models
from inventario.models import Repuesto 
from usuarios.models import Usuario
from django.utils.translation import gettext_lazy as _
class Servicio(models.Model):
    nombreservicio= models.CharField(max_length=20,verbose_name="Nombre de Servicio")
    tipo_servicio= models.CharField(max_length=45,verbose_name="Tipo de Servicio")
    duracion = models.DurationField(verbose_name="Duración de la cita",default="0:00:00")
    costoservicio = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Costo  Servico",default=0.000,blank=False) 
    descripcion= models.CharField(max_length=45,verbose_name="Descripción")
    def __str__(self):
        return f"${self.costoservicio}-{self.nombreservicio}"
    
    
    class Meta:
        verbose_name_plural = "Servicio"  
class Detalle_servicio(models.Model):
    fecha_servicio= models.DateField(verbose_name="Fecha de Registro", help_text="MM/DD/AAAA")
    nombres= models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={'tipo_usuario': Usuario.TipoUsuario.MECANICO},verbose_name="Mecanico")
    kilometraje = models.IntegerField( verbose_name="Kilometraje")
    estado_vehiculo = models.CharField(max_length=45, verbose_name="Estado del vehiculo")
    observaciones=models.CharField(max_length=45, verbose_name="Observaciones")
    nombrerepuesto= models.ForeignKey(Repuesto, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Costo Repuesto")
    nombreservicio = models.ForeignKey(Servicio,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Costo Servicio")
    
    class Meta:
        verbose_name_plural = "Detalle_servicio"