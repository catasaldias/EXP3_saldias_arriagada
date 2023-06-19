# Generated by Django 4.2.2 on 2023-06-18 19:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=100, verbose_name='Nombre de categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio')),
                ('stock', models.BooleanField(default=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stock')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jardineriaapp.categoria', verbose_name='Categoria')),
            ],
        ),
    ]