# Generated by Django 4.1 on 2022-09-10 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
    ]
