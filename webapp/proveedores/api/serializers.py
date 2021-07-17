from rest_framework.serializers import ModelSerializer

from proveedores.models import Proveedor

class ProveedorCreateSerializer(ModelSerializer):
	class Meta:
		model = Proveedor
		fields = [
			'nombre',
			'direccion',
		]

class ProveedorDetailSerializer(ModelSerializer):
	class Meta:
		model = Proveedor
		fields = [
			'id_proveedor',
			'nombre',
			'direccion',
		]

class ProveedorListSerializer(ModelSerializer):
	class Meta:
		model = Proveedor
		exclude = []