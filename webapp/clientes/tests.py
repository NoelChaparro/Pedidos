from django.test import TestCase
from .models import Cliente

class ClienteTestCase(TestCase):
	def setUp(self):
		Cliente.objects.create(nombre='NOEL CHAPARRO', codigo='23112311', direccion='Chihuahua', tipo_cliente='NORMAL')
		Cliente.objects.create(nombre='LUCIANA CHAPARRO', codigo='01010101', direccion='Cuauhtemoc', tipo_cliente='ORO')

	def test_cliente_exist(self):
		cliente_count = Cliente.objects.all().count()
		self.assertEqual(cliente_count,2)

