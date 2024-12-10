from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail


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
    
class Extraescolar(models.Model):
    id_extraescolar = models.AutoField(primary_key=True)
    nombre_extraescolar = models.CharField(max_length=255)
    cantidad_extraescolar = models.IntegerField()
    tipo_extraescolar = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_extraescolar
    
class InteEscolar(models.Model):
    id_inteescolar = models.AutoField(primary_key=True)
    nombre_inteescolar = models.CharField(max_length=255)
    cantidad_inteescolar = models.IntegerField()
    tipo_inteescolar = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_inteescolar

@receiver(post_save, sender=Extraescolar)
@receiver(post_save, sender=InteEscolar)
@receiver(post_save, sender=Computacion)
@receiver(post_save, sender=Aseo)
@receiver(post_save, sender=Profesores)
def enviar_notificacion_guardar(sender, instance, created, **kwargs):
    accion = "creado" if created else "actualizado" ####

    
    asunto = f'{sender.__name__} {accion}'
    mensaje = (
        f'Se ha {accion} un registro en {sender.__name__}.\n\n'
        f'Nombre: {getattr(instance, "nombre_material", None) or getattr(instance, "nombre_insumo", None)or getattr(instance, "nombre_extraescolar", None)or getattr(instance, "nombre_inteescolar", None) or instance.nombre_objeto}\n'
        f'Tipo: {getattr(instance, "tipo_material", None) or getattr(instance, "tipo_insumo", None)or getattr(instance, "tipo_extraescolar", None)or getattr(instance, "tipo_inteescolar", None) or instance.tipo_producto}\n'
        f'Cantidad: {getattr(instance, "cantidad_material", None) or getattr(instance, "cantidad_insumo", None)or getattr(instance, "cantidad_extraescolar", None)or getattr(instance, "cantidad_inteescolar", None) or instance.cantidad_objeto}'
    )
    remitente = 'santacecilia.direccion@gmail.com'  
    destinatarios = ['destinatario@gmail.com']  

    send_mail(asunto, mensaje, remitente, destinatarios, fail_silently=False)

@receiver(post_save, sender=Extraescolar)
@receiver(post_save, sender=InteEscolar)
@receiver(post_delete, sender=Computacion)
@receiver(post_delete, sender=Aseo)
@receiver(post_delete, sender=Profesores)
def enviar_notificacion_eliminacion(sender, instance, **kwargs):
    asunto = f'Producto dentro del area {sender.__name__} fue eliminado'
    mensaje = (
        f'Se ha eliminado un registro en {sender.__name__}.\n\n'
        f'Nombre: {getattr(instance, "nombre_material", None) or getattr(instance, "nombre_insumo", None)or getattr(instance, "nombre_extraescolar", None)or getattr(instance, "nombre_inteescolar", None) or instance.nombre_objeto}\n'
        f'Tipo: {getattr(instance, "tipo_material", None) or getattr(instance, "tipo_insumo", None)or getattr(instance, "tipo_extraescolar", None)or getattr(instance, "tipo_inteescolar", None) or instance.tipo_producto}\n'
        f'Cantidad: {getattr(instance, "cantidad_material", None) or getattr(instance, "cantidad_insumo", None)or getattr(instance, "cantidad_extraescolar", None)or getattr(instance, "cantidad_inteescolar", None) or instance.cantidad_objeto}'
    )
    remitente = 'santacecilia.direccion@gmail.com'  
    destinatarios = ['destinatario@gmail.com'] 

    send_mail(asunto, mensaje, remitente, destinatarios, fail_silently=False)