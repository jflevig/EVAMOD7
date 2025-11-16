from django import forms
from django.forms import ModelForm
from .models import Producto, Categoria, Etiqueta, Detalle

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple()
        }

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class EtiquetaForm(ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'

class DetalleForm(ModelForm):
    class Meta:
        model = Detalle
        exclude = ['producto']
        