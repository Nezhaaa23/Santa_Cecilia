from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Modelo Computación
class Computacion(models.Model):
    id_material = models.AutoField(primary_key=True)
    nombre_material = models.CharField(max_length=255)
    tipo_material = models.CharField(max_length=255)
    cantidad_material = models.IntegerField()

    def __str__(self):
        return self.nombre_material


# Modelo Aseo
class Aseo(models.Model):
    id_insumo = models.AutoField(primary_key=True)
    nombre_insumo = models.CharField(max_length=255)
    cantidad_insumo = models.IntegerField()
    tipo_insumo = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_insumo


# Modelo Profesores
class Profesores(models.Model):
    id_objeto = models.AutoField(primary_key=True)
    nombre_objeto = models.CharField(max_length=255)
    cantidad_objeto = models.IntegerField()
    tipo_producto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_objeto


# Signals para enviar correo en creación o actualización
@receiver(post_save, sender=Computacion)
@receiver(post_save, sender=Aseo)
@receiver(post_save, sender=Profesores)
def enviar_notificacion(sender, instance, created, **kwargs):
    # Identificar si es creación o actualización
    accion = "creado" if created else "actualizado"

    # Configurar el correo
    asunto = f'{sender.__name__} {accion}'
    mensaje = (
        f'Se ha {accion} un registro en {sender.__name__}.\n\n'
        f'Nombre: {getattr(instance, "nombre_material", None) or getattr(instance, "nombre_insumo", None) or instance.nombre_objeto}\n'
        f'Tipo: {getattr(instance, "tipo_material", None) or getattr(instance, "tipo_insumo", None) or instance.tipo_producto}\n'
        f'Cantidad: {getattr(instance, "cantidad_material", None) or getattr(instance, "cantidad_insumo", None) or instance.cantidad_objeto}'
    )
    remitente = 'tu_correo@gmail.com'  # Cambia por tu correo
    destinatarios = ['destinatario@gmail.com']  # Cambia por la lista de destinatarios

    # Enviar correo
    send_mail(asunto, mensaje, remitente, destinatarios, fail_silently=False)
