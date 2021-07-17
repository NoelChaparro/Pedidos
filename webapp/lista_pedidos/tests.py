from django.test import TestCase

from .models import Pedido
from clientes.models import Cliente

class PedidoTestCase(TestCase):
	def setUp(self):
		c = Cliente.objects.create(nombre='NOEL CHAPARRO', codigo='23112311', direccion='Chihuahua', tipo_cliente='NORMAL')
		p = Pedido.objects.create(
			cliente= c,
			fecha_creacion = "2021-07-16",
			actualizacion = "2021-07-16 00:00:00",
			fecha_surtido = "2022-07-18 00:00:00",
			urgente = True,
			tipo_pedido=1)


	def test_pedido_exist(self):
		pedido_count = Pedido.objects.all().count()
		self.assertEqual(pedido_count,1)