import datetime

from django.db import models
from django.core.exceptions import ValidationError
from articulos.models import Articulo
from clientes.models import Cliente

class Pedido(models.Model):
	LISTA_TIPO_PEDIDO = (
        ('1', 'CENTRO DISTRIBUCION'),
        ('2', 'SUCURSAL'),
        ('3', 'EMPRESA ASOCIADA'),
    )
	numero_pedido = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente, db_column='id_cliente', on_delete=models.PROTECT)
	fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False)
	fecha_surtido = models.DateTimeField(blank=True, null=True)
	urgente = models.BooleanField(default=False)
	tipo_pedido = models.CharField(max_length=19, choices=LISTA_TIPO_PEDIDO)

	def clean(self):
		if self.fecha_surtido != None:
			if (datetime.datetime.strftime(self.fecha_surtido, "%m/%d/%Y %H:%M")<datetime.datetime.strftime(datetime.datetime.now(), "%m/%d/%Y %H:%M")):
				raise ValidationError("El pedido se esta surtiendo antes de crearlo")
		else:
			pass

	def __str__(self):
		return str(self.numero_pedido)

class DetallePedido(models.Model):
	id_detalle = models.AutoField(primary_key=True)
	pedido = models.ForeignKey(Pedido, db_column='id_pedido', on_delete=models.PROTECT)
	articulo = models.ForeignKey(Articulo, db_column='id_articulo', on_delete=models.PROTECT)
	cantidad_articulos = models.IntegerField(null=False)

	def __str__(self):
		return self.articulo.descripcion

class CentroDistribucion(models.Model):
	pedido = models.ForeignKey(Pedido, db_column='id_pedido', on_delete=models.PROTECT)
	almacen = models.CharField(max_length=50, null=False)

	def clean(self):
		if self.pedido.tipo_pedido != '1':
			raise ValidationError('No coincide el tipo de pedido, debe de ser al Centro de Distribucion')

	def __str__(self):
		return self.almacen

class Sucursal(models.Model):
	pedido = models.ForeignKey(Pedido, db_column='id_pedido', on_delete=models.PROTECT)
	referencia = models.CharField(max_length=30, null=False)
	codigo_sucursal = models.IntegerField(null=False)

	def clean(self):
		if self.pedido.tipo_pedido != '2':
			raise ValidationError('No coincide el tipo de pedido, debe de ser a Sucursal')

	def __str__(self):
		return self.referencia

class EmpresaAsociada(models.Model):
	pedido = models.ForeignKey(Pedido, db_column='id_pedido', on_delete=models.PROTECT)
	referencia = models.CharField(max_length=30, null=False)
	codigo_socio = models.IntegerField(null=False)

	def clean(self):
		if self.pedido.tipo_pedido != '3':
			raise ValidationError('No coincide el tipo de pedido, debe de ser a Empresa Asociada')

	def __str__(self):
		return self.referencia
