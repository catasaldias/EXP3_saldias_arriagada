from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria=models.CharField(max_length=100, blank=True, verbose_name="Nombre de categoria")


    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo=models.CharField(primary_key=True, max_length=4, verbose_name="Codigo")
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    precio=models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Precio")
    stock=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Stock")
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name="Imagen")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.codigo


#COMENTARIOS
#Para Catalina: 1.-El import de validators puesto y los datos nuevos que puse uno es para que el precio no fuera 0 y revisar cuantos objetos hay en stock
#2.- me entere muy tarde que podria confundirse con la pagina "productos" pero no son lo mismo. lo siento
#3.-El import MinValueValidator es para revisar que cosas como el precio y el stock no sean negativos
#4.-use codigo como primary key no se me ocurria otra cosa por que nombres era mala idea como primary key :p
#5.-este sera el resplado para el cambio de nombre
#6.- ¿se podra hacer ahora lo del hacer una como interfaz base y trabajar desde ahi?

