# Generated by Django 4.1.3 on 2023-01-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0003_alter_contratos_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratos',
            name='estado_de_pago',
            field=models.CharField(choices=[('1', 'AL DÍA'), ('2', 'EN MORA')], max_length=1, null=True, verbose_name='Estado de pago'),
        ),
    ]
