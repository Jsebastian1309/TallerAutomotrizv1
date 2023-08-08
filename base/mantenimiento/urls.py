from django.urls import path
from mantenimiento.views import mantenimiento_crear,mantenimiento_listar,mantenimiento_modificar,mantenimiento_eliminar
from mantenimiento.views import cita_crear,cita_listar,cita_modificar,cita_eliminar

urlpatterns = [
    path('mantenimiento/', mantenimiento_listar, name="mantenimientos" ),
    path('mantenimiento/crear/', mantenimiento_crear, name="mantenimientos-crear" ),
    path('mantenimiento/modificar/<int:pk>/', mantenimiento_modificar, name="mantenimientos-modificar" ),
    path('mantenimiento/eliminar/<int:pk>/', mantenimiento_eliminar, name="mantenimientos-eliminar" ),
    
    path('citas/', cita_listar, name="citas" ),
    path('citas/crear/', cita_crear, name="citas-crear" ),
    path('citas/modificar/<int:pk>/', cita_modificar, name="citas-modificar" ),
    path('citas/eliminar/<int:pk>/', cita_eliminar, name="citas-eliminar" ),

]