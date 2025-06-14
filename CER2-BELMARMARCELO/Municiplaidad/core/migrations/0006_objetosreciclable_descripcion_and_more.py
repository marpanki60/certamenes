# Generated by Django 5.2.1 on 2025-06-02 02:50

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_perfil'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='objetosreciclable',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='objetosreciclable',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_ruta', 'En ruta'), ('completado', 'Completado')], default='pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='objetosreciclable',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objetosreciclable',
            name='usuario',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='objetosreciclable',
            name='cantidadMaterial',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='objetosreciclable',
            name='tipoMaterial',
            field=models.CharField(choices=[('papel_carton', 'Papel y Cartón - Materiales reciclables como papel y cartón usados'), ('plasticos', 'Plásticos reciclables - Botellas, envases, etc.'), ('vidrios', 'Vidrios - Botellas, frascos, vidrios limpios'), ('latas', 'Latas - De aluminio o acero'), ('electronicos', 'Electrónicos pequeños - Aparatos electrónicos pequeños reciclables'), ('textiles', 'Textiles - Ropa y telas reciclables'), ('voluminosos', 'Voluminosos reciclables - Objetos grandes reciclables')], max_length=20),
        ),
    ]
