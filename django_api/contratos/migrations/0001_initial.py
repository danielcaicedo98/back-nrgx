# Generated by Django 4.1.3 on 2023-01-04 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
        ('utils', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la cual fue creado.', verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue actualizdo por últimavez.', verbose_name='updated at')),
                ('direccion_instalacion', models.CharField(max_length=150, verbose_name='Dirección de instalación')),
                ('latitud', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=8, max_digits=10)),
                ('tipo_de_uso', models.CharField(choices=[('1', 'Recidencial'), ('2', 'Comercial')], default='1', max_length=1, verbose_name='Tipo de uso')),
                ('estrato', models.IntegerField(verbose_name='Estrato socioeconomico')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('2', 'Inactivo'), ('3', 'Suspendido')], max_length=1, verbose_name='Estado')),
                ('estado_de_pago', models.CharField(choices=[('1', 'AL DÍA'), ('2', 'EN MORA')], max_length=1, verbose_name='Estado de pago')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.ciudades')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sericios', models.ManyToManyField(related_name='servicios_contrato', to='servicios.servicios')),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contratos',
                'db_table': 'contratos',
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
                'managed': True,
            },
        ),
    ]
