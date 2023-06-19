from django.urls import path
from .views import inicio,sobrenosotros,productos,carrito,datosenvio,escribenos,donaciones,menustock,crear,eliminar,modificar

urlpatterns=[ 
    path('', inicio, name="inicio"),
    path('2_SobreNosotros/', sobrenosotros, name="sobrenosotros"),
    path('3_Productos/', productos, name="productos"),
    path('4_Carrito/', carrito, name="carrito"),
    path('5_DatosEnvio/', datosenvio, name="datosenvio"),
    path('6_Escribenos/', escribenos, name="escribenos"),
    path('7_Donaciones/', donaciones, name="donaciones"),
    path('8_Stock/', menustock, name="menustock"),
    path('9_Crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar")
   

]