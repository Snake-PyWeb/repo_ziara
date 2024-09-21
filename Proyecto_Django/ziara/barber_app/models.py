from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre_cliente=models.CharField(max_length=254)
    email_cliente=models.EmailField(max_length=254)
    direccion_cliente=models.CharField(max_length=254)
    tel_cliente=models.IntegerField()
    fecha_nacimiento=models.DateField()