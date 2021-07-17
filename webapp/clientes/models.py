from django.db import models

class Cliente(models.Model):
	LISTA_TIPO_CLIENTE = (
        ('NORMAL', 'NORMAL'),
        ('PLATA', 'PLATA'),
        ('ORO', 'ORO'),
        ('PLATINO', 'PLATINO')
    )
	id_cliente = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	codigo = models.CharField(max_length=20, null=False, unique=True)
	fotografia = models.ImageField(upload_to='uploads/')
	direccion = models.CharField(max_length=100)
	tipo_cliente = models.CharField(max_length=7, choices=LISTA_TIPO_CLIENTE)

	def __str__(self):
		return self.nombre