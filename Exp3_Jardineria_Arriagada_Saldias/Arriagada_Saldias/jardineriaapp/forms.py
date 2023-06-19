from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'stock', 'imagen',  'categoria']
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'precio': 'Precio',
            'stock' : 'Stock',
            'imagen': 'Imagen',
            'categoria': 'Categoria'
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese codigo..',
                    'id': 'codigo',
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre..',
                    'id': 'nombre',
                }
            ),
            'precio':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio..',
                    'id': 'precio',
                },
            ),
            'stock':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock...',
                    'id': 'stock',
                }
            ),

            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            ),
            
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id':'categoria',
                }
            )

        }