from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Articulo
from proveedores.models import Proveedor

class ArticuloTestCase(TestCase):
	def setUp(self):
		p = Proveedor.objects.create(nombre="PROCOM", direccion="AVE MORELOS 675")
		a = Articulo.objects.create(descripcion="CARGADOR USB", precio=123.45)
		a.proveedor.add(p)

	def test_articulo_exist(self):
		articulo_count = Articulo.objects.all().count()
		self.assertEqual(articulo_count,1)

class ArticuloTestAPI(APITestCase):
	def test_create_proveedor(self):
		url = reverse('proveedores-api:create-proveedor')
		data = {'nombre':'SYSCOM','direcciones':'BARRANCA DEL MUERTO 287'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
