from django.db import models

# Create your models here.

from django.db import models
    
class Computacion(models.Model):
    id_material = models.AutoField(primary_key=True)
    nombre_material = models.CharField(max_length=255)
    tipo_material = models.CharField(max_length=255)
    cantidad_material = models.IntegerField()

    def __str__(self):
        return self.nombre_material



class Aseo(models.Model):
    id_insumo = models.AutoField(primary_key=True)
    nombre_insumo = models.CharField(max_length=255)
    cantidad_insumo = models.IntegerField()
    tipo_insumo = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_insumo



class Profesores(models.Model):
    id_objeto = models.AutoField(primary_key=True)
    nombre_objeto = models.CharField(max_length=255)
    cantidad_objeto = models.IntegerField()
    tipo_producto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_objeto