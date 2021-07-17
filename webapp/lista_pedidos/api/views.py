from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView
	)

from lista_pedidos.models import (
	CentroDistribucion,
	DetallePedido,
	EmpresaAsociada,
	Pedido,
	Sucursal
	)
from .serializers import (
	CentroDistribucionCreateSerializer,
	CentroDistribucionDetailSerializer,
	CentroDistribucionListSerializer,
	DetallePedidoCreateSerializer,
	DetallePedidoDetailSerializer,
	DetallePedidoListSerializer,
	EmpresaAsociadaCreateSerializer,
	EmpresaAsociadaDetailSerializer,
	EmpresaAsociadaListSerializer,
	PedidoCreateSerializer,
	PedidoDetailSerializer,
	PedidoListSerializer,
	PedidosUrgentesSerializer,
	SucursalCreateSerializer,
	SucursalDetailSerializer,
	SucursalListSerializer
	)

class PedidoCreateAPIView(CreateAPIView):
	queryset = Pedido.objects.all()
	serializer_class = PedidoCreateSerializer

class PedidoDeleteAPIView(DestroyAPIView):
	queryset = Pedido.objects.all()
	serializer_class = PedidoDetailSerializer
	lookup_field = 'numero_pedido'
	lookup_url_kwarg = 'numero_pedido'

class PedidoDetailAPIView(RetrieveAPIView):
	queryset = Pedido.objects.all()
	serializer_class = PedidoDetailSerializer
	lookup_field = 'numero_pedido'
	lookup_url_kwarg = 'numero_pedido'

class PedidoListAPIView(ListAPIView):
	queryset = Pedido.objects.all()
	serializer_class = PedidoListSerializer

class PedidoUpdateAPIView(UpdateAPIView):
	queryset = Pedido.objects.all()
	serializer_class = PedidoDetailSerializer
	lookup_field = 'numero_pedido'
	lookup_url_kwarg = 'numero_pedido'

class DetallePedidoCreateAPIView(CreateAPIView):
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoCreateSerializer

class DetallePedidoDeleteAPIView(DestroyAPIView):
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoDetailSerializer
	lookup_field = 'id_detalle'
	lookup_url_kwarg = 'id_detalle'

class DetallePedidoDetailAPIView(RetrieveAPIView):
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoDetailSerializer
	lookup_field = 'id_detalle'
	lookup_url_kwarg = 'id_detalle'

class DetallePedidoListAPIView(ListAPIView):
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoListSerializer

class DetallePedidoUpdateAPIView(UpdateAPIView):
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoDetailSerializer
	lookup_field = 'id_detalle'
	lookup_url_kwarg = 'id_detalle'

class CentroDistribucionCreateAPIView(CreateAPIView):
	queryset = CentroDistribucion.objects.all()
	serializer_class = CentroDistribucionCreateSerializer

class CentroDistribucionDeleteAPIView(DestroyAPIView):
	queryset = CentroDistribucion.objects.all()
	serializer_class = CentroDistribucionDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class CentroDistribucionDetailAPIView(RetrieveAPIView):
	queryset = CentroDistribucion.objects.all()
	serializer_class = CentroDistribucionDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class CentroDistribucionListAPIView(ListAPIView):
	queryset = CentroDistribucion.objects.all()
	serializer_class = CentroDistribucionListSerializer

class CentroDistribucionUpdateAPIView(UpdateAPIView):
	queryset = CentroDistribucion.objects.all()
	serializer_class = CentroDistribucionDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class SucursalCreateAPIView(CreateAPIView):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalCreateSerializer

class SucursalDeleteAPIView(DestroyAPIView):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class SucursalDetailAPIView(RetrieveAPIView):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class SucursalListAPIView(ListAPIView):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalListSerializer

class SucursalUpdateAPIView(UpdateAPIView):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class EmpresaAsociadaCreateAPIView(CreateAPIView):
	queryset = EmpresaAsociada.objects.all()
	serializer_class = EmpresaAsociadaCreateSerializer

class EmpresaAsociadaDeleteAPIView(DestroyAPIView):
	queryset = EmpresaAsociada.objects.all()
	serializer_class = EmpresaAsociadaDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class EmpresaAsociadaDetailAPIView(RetrieveAPIView):
	queryset = EmpresaAsociada.objects.all()
	serializer_class = EmpresaAsociadaDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class EmpresaAsociadaListAPIView(ListAPIView):
	queryset = EmpresaAsociada.objects.all()
	serializer_class = EmpresaAsociadaListSerializer

class EmpresaAsociadaUpdateAPIView(UpdateAPIView):
	queryset = EmpresaAsociada.objects.all()
	serializer_class = EmpresaAsociadaDetailSerializer
	lookup_field = 'pedido'
	lookup_url_kwarg = 'pedido'

class PedidosUrgentesListAPIView(ListAPIView):
	serializer_class = PedidosUrgentesSerializer
	filer_fields = ('numero_pedido')

	def get_queryset(self, *args, **kwargs):
		queryset = Pedido.objects.filter(urgente=True,tipo_pedido='1',fecha_surtido=None,cliente__tipo_cliente="PLATINO")
		return queryset
