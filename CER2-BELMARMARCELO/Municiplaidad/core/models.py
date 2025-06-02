from django.db import models
from django.contrib.auth.models import User



class ObjetosReciclable(models.Model):
    TIPO_MATERIAL_CHOICES = [
        ('papel_carton', 'Papel y Cartón - Materiales reciclables como papel y cartón usados'),
        ('plasticos', 'Plásticos reciclables - Botellas, envases, etc.'),
        ('vidrios', 'Vidrios - Botellas, frascos, vidrios limpios'),
        ('latas', 'Latas - De aluminio o acero'),
        ('electronicos', 'Electrónicos pequeños - Aparatos electrónicos pequeños reciclables'),
        ('textiles', 'Textiles - Ropa y telas reciclables'),
        ('voluminosos', 'Voluminosos reciclables - Objetos grandes reciclables'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_ruta', 'En ruta'),
        ('completado', 'Completado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoMaterial = models.CharField(max_length=20, choices=TIPO_MATERIAL_CHOICES)
    cantidadMaterial = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)
    fechaEstimada = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_tipoMaterial_display()} - {self.cantidadMaterial} unidades - Estado: {self.get_estado_display()}'


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username