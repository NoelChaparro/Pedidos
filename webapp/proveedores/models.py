from django.db import models

class Proveedor(models.Model):
	id_proveedor = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=80)
	direccion = models.CharField(max_length=120)

	def __str__(self):
		return self.nombre
