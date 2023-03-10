# Generated by Django 4.1.3 on 2023-01-04 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la cual fue creado.', verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue actualizdo por últimavez.', verbose_name='updated at')),
                ('fecha_expedicion', models.DateField(verbose_name='Fecha de expedición')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('numero_pago_electronico', models.CharField(max_length=15)),
                ('estado', models.CharField(choices=[('1', 'PAGADA'), ('2', 'PENDIENTE')], default='2', max_length=1)),
                ('valor_pendiente_pago', models.FloatField(verbose_name='Valor pendiente de pago')),
                ('is_recargo', models.BooleanField(default=False, help_text='ayuda a saber si se le aplica recargo o no', verbose_name='Recargo')),
                ('porcentaje_recargo', models.BigIntegerField(verbose_name='Porcentaje de cargo')),
                ('valor_recargo', models.IntegerField(verbose_name='Valor de recargo')),
                ('total_a_pagar', models.IntegerField(verbose_name='Total a pagar')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.contratos')),
            ],
            options={
                'verbose_name': 'factura',
                'verbose_name_plural': 'facturas',
                'db_table': 'facturas',
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la cual fue creado.', verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue actualizdo por últimavez.', verbose_name='updated at')),
                ('lectura_anterior', models.BigIntegerField()),
                ('lectura_actual', models.BigIntegerField()),
                ('consumo_actual', models.IntegerField()),
                ('valor_unitario', models.FloatField()),
                ('valor_total', models.FloatField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.facturas')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicios')),
            ],
            options={
                'verbose_name': 'detalle_factura',
                'verbose_name_plural': 'detalles_facturas',
                'db_table': 'detalle_factura',
                'ordering': ['-created', '-updated'],
                'get_latest_by': 'created',
                'abstract': False,
                'managed': True,
            },
        ),
    ]
