# Generated by Django 4.1 on 2022-09-10 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='precio'),
        ),
    ]
