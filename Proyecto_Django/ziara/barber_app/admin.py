from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=['nombre_cliente','email_cliente']
    search_fields=['nombre_cliente']


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=['nombre_usuario','tipo_usuario']
    


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display=['nombre_servicio']
    


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre_producto','stock']
    


@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display=['nombre_especialidad']
    


@admin.register(Disponibilidad_barbero)
class Disponibilidad_barberoAdmin(admin.ModelAdmin):
    list_display=['dia_semana','hora_inicio','hora_final']
    


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display=['fecha_hora']
    


@admin.register(Inventario_movimiento)
class Inventario_movimientoAdmin(admin.ModelAdmin):
    list_display=['tipo','fecha_hora','cantidad']
    

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display=['fecha_hora']
    

@admin.register(Detalle_venta)
class Detalle_ventaAdmin(admin.ModelAdmin):
    list_display=['cantidad']
    
@admin.register(Evaluacione)
class EvaluacioneAdmin(admin.ModelAdmin):
    list_display=['calificacion']
    


