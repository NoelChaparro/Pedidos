from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView
	)

from articulos.models import Articulo
from .serializers import (
	ArticuloCreateSerializer,
	ArticuloDetailSerializer,
	ArticuloListSerializer
	)

class ArticuloCreateAPIView(CreateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloCreateSerializer

class ArticuloDeleteAPIView(DestroyAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloDetailSerializer
	lookup_field = 'id_articulo'
	lookup_url_kwarg = 'id_articulo'

class ArticuloDetailAPIView(RetrieveAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloDetailSerializer
	lookup_field = 'id_articulo'
	lookup_url_kwarg = 'id_articulo'

class ArticuloListAPIView(ListAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloListSerializer

class ArticuloUpdateAPIView(UpdateAPIView):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloDetailSerializer
	lookup_field = 'id_articulo'
	lookup_url_kwarg = 'id_articulo'