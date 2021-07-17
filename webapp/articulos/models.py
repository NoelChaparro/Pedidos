from django.db import models
from proveedores.models import Proveedor

class Articulo(models.Model):
	id_articulo = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=150)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	proveedor = models.ManyToManyField(Proveedor, related_name='articulo')

	def __str__(self):
		return self.descripcion
