from django.db import models

# Create your models here.

    
#class Administrador(models.Model):
    #idAdministrador identificador unico
    #idUsuario relacionado con usuarios
    
#Class Barbero(models.Model):
    #idBarbero
    #idUsuario
    #IdAdministrador
    
#class Barbero_Especialide(models.Model):
    #id
    #idBarbero
    #idEspcialidad
    


class Usuario(models.Model):
    #idUsuario
    nombre_usuario=models.CharField(max_length=254)   # Nombre completo del usuario.
    email_usuario=models.EmailField() #Correo electrónico usado para autenticación.
    contraseña=models.CharField(max_length=254)
    tipo_usuario=models.CharField(max_length=254)
    
    #Relacion con Administrador , Barberos,Clientes 
    


class Cliente(models.Model):
    #idCliente
    #idUsuario
    nombre_cliente = models.CharField(max_length=254)  
    email_cliente = models.EmailField()
    direccion_cliente=models.CharField(max_length=254)
    tel_cliente=models.IntegerField()
    fecha_nacimiento=models.DateField()
    


class Servicio(models.Model):
    #idServicio
    nombre_servicio=models.CharField(max_length=254)
    descripcion_producto=models.TextField()
    duracion=models.IntegerField()
    precio_producto=models.DecimalField(max_digits=10, decimal_places=2)
    
    #Un servicio puede estar relacionado con muchas citas
    


class Producto(models.Model):
    #IdProducto
    nombre_producto=models.CharField(max_length=254)
    descripcion_producto=models.TextField()
    precio_producto=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    
    #Un producto puede tener multiples movimientos de inventario y puede aparecer en varias ventas


class Especialidade(models.Model):
    #idEspecialidad
    nombre_especialidad=models.CharField(max_length=254)
    
    #Relaciona los barberos con sus especialidades por medio de la tabla barbero_especialidad
    



class Disponibilidad_barbero(models.Model):
    #id
    #idBarbero
    dia_semana=models.CharField(max_length=10)
    hora_inicio=models.TimeField()
    hora_final=models.TimeField()
    
    #Un barbero puede tener múltiples registros de disponibilidad (relación uno a muchos)


class Cita(models.Model):
    #id
    fecha_hora=models.DateTimeField()
    #idCliente fk
    #IdServicio fk
    #idBarbero fk
    


class Inventario_movimiento(models.Model):
    #id
    #idProducto
    tipo=models.CharField(max_length=100)
    cantidad=models.IntegerField()
    fecha_hora=models.DateTimeField()
    
    #idProducto → Productos.idProducto (relación muchos a uno).
    


class Venta(models.Model):
    #id
    fecha_hora=models.DateTimeField()
    #idCliente
    #idBarbero
    
    #idCliente → Clientes.idCliente (relación muchos a uno). idBarbero → Barberos.idBarbero (relación muchos a uno).
    

class Detalle_venta(models.Model):
    #id
    #idVenta
    #IdProducto
    cantidad=models.IntegerField()
    


class Evaluacione(models.Model):
    #id
    #idCita
    calificacion=models.IntegerField()
    comentarios=models.TextField()
    