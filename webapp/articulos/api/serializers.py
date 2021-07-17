from rest_framework.serializers import ModelSerializer

from articulos.models import Articulo

class ArticuloCreateSerializer(ModelSerializer):
	class Meta:
		model = Articulo
		fields = [
			'descripcion',
			'precio',
			'proveedor',
		]

class ArticuloDetailSerializer(ModelSerializer):
	class Meta:
		model = Articulo
		fields = [
			'id_articulo',
			'descripcion',
			'precio',
			'proveedor',
		]

class ArticuloListSerializer(ModelSerializer):
	class Meta:
		model = Articulo
		exclude = []