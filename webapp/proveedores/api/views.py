from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView
	)

from proveedores.models import Proveedor
from .serializers import (
	ProveedorCreateSerializer,
	ProveedorDetailSerializer,
	ProveedorListSerializer
	)

class ProveedorCreateAPIView(CreateAPIView):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorCreateSerializer

class ProveedorDeleteAPIView(DestroyAPIView):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorDetailSerializer
	lookup_field = 'id_proveedor'
	lookup_url_kwarg = 'id_proveedor'

class ProveedorDetailAPIView(RetrieveAPIView):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorDetailSerializer
	lookup_field = 'id_proveedor'
	lookup_url_kwarg = 'id_proveedor'

class ProveedorListAPIView(ListAPIView):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorListSerializer

class ProveedorUpdateAPIView(UpdateAPIView):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorDetailSerializer
	lookup_field = 'id_proveedor'
	lookup_url_kwarg = 'id_proveedor'