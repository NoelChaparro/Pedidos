from rest_framework.serializers import ModelSerializer

from clientes.models import Cliente

class ClienteCreateSerializer(ModelSerializer):
	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'codigo',
			'direccion',
			'tipo_cliente',
			'fotografia',
		]

class ClienteDetailSerializer(ModelSerializer):
	class Meta:
		model = Cliente
		fields = [
			'id_cliente',
			'nombre',
			'codigo',
			'direccion',
			'tipo_cliente',
			'fotografia',
		]

class ClienteListSerializer(ModelSerializer):
	class Meta:
		model = Cliente
		exclude = []