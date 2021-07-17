from django import forms
from django.forms import ModelForm

from .models import *

class PedidoForm(ModelForm):
	urgente = forms.BooleanField(required=False)
	class Meta:
		model = Pedido
		fields = ['cliente','fecha_surtido','urgente','tipo_pedido']
		widgets = {
			'cliente': forms.Select(),
			'fecha_surtido': forms.DateInput(format=('%Y-%m-%d')),
			'urgente': forms.BooleanField(),
			'tipo_pedido': forms.Select()
		}

class DetallePedidoForm(ModelForm):
	cantidad_articulos = forms.IntegerField(required=True)
	class Meta:
		model = DetallePedido
		fields = ['pedido','articulo','cantidad_articulos']
		widgets = {
			'pedido': forms.Select(),
			'articulo': forms.Select(),
			'cantidad_articulos': forms.IntegerField()
		}