from rest_framework.serializers import ModelSerializer

from lista_pedidos.models import (
	CentroDistribucion,
	DetallePedido,
	EmpresaAsociada,
	Pedido,
	Sucursal
	)

class PedidoCreateSerializer(ModelSerializer):
	class Meta:
		model = Pedido
		fields = [
			'numero_pedido',
			'cliente',
			'fecha_creacion',
			'actualizacion',
			'fecha_surtido',
			'urgente',
			'tipo_pedido',
		]

class PedidoDetailSerializer(ModelSerializer):
	class Meta:
		model = Pedido
		fields = [
			'numero_pedido',
			'cliente',
			'fecha_creacion',
			'actualizacion',
			'fecha_surtido',
			'urgente',
			'tipo_pedido',
		]

class PedidoListSerializer(ModelSerializer):
	class Meta:
		model = Pedido
		exclude = []

class DetallePedidoCreateSerializer(ModelSerializer):
	class Meta:
		model = DetallePedido
		fields = [
			'pedido',
			'articulo',
			'cantidad_articulos',
		]

class DetallePedidoDetailSerializer(ModelSerializer):
	class Meta:
		model = DetallePedido
		fields = [
			'id_detalle',
			'pedido',
			'articulo',
			'cantidad_articulos',
		]

class DetallePedidoListSerializer(ModelSerializer):
	class Meta:
		model = DetallePedido
		exclude = []

class CentroDistribucionCreateSerializer(ModelSerializer):
	class Meta:
		model = CentroDistribucion
		fields = [
			'pedido',
			'almacen',
		]

class CentroDistribucionDetailSerializer(ModelSerializer):
	class Meta:
		model = CentroDistribucion
		fields = [
			'pedido',
			'almacen',
		]

class CentroDistribucionListSerializer(ModelSerializer):
	class Meta:
		model = CentroDistribucion
		exclude = []


class SucursalCreateSerializer(ModelSerializer):
	class Meta:
		model = Sucursal
		fields = [
			'pedido',
			'referencia',
			'codigo_sucursal',
		]

class SucursalDetailSerializer(ModelSerializer):
	class Meta:
		model = Sucursal
		fields = [
			'pedido',
			'referencia',
			'codigo_sucursal',
		]

class SucursalListSerializer(ModelSerializer):
	class Meta:
		model = Sucursal
		exclude = []


class EmpresaAsociadaCreateSerializer(ModelSerializer):
	class Meta:
		model = EmpresaAsociada
		fields = [
			'pedido',
			'referencia',
			'codigo_socio',
		]

class EmpresaAsociadaDetailSerializer(ModelSerializer):
	class Meta:
		model = EmpresaAsociada
		fields = [
			'pedido',
			'referencia',
			'codigo_socio',
		]

class EmpresaAsociadaListSerializer(ModelSerializer):
	class Meta:
		model = EmpresaAsociada
		exclude = []

class PedidosUrgentesSerializer(ModelSerializer):
	class Meta:
		model = Pedido
		exclude = []