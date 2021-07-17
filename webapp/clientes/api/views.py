from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView
	)

from clientes.models import Cliente
from .serializers import (
	ClienteCreateSerializer,
	ClienteDetailSerializer,
	ClienteListSerializer
	)

class ClienteCreateAPIView(CreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteCreateSerializer

class ClienteDeleteAPIView(DestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteDetailSerializer
	lookup_field = 'codigo'
	lookup_url_kwarg = 'codigo_cliente'

class ClienteDetailAPIView(RetrieveAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteDetailSerializer
	lookup_field = 'codigo'
	lookup_url_kwarg = 'codigo_cliente'

class ClienteListAPIView(ListAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteListSerializer

class ClienteUpdateAPIView(UpdateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteDetailSerializer
	lookup_field = 'codigo'
	lookup_url_kwarg = 'codigo_cliente'