from django.conf.urls import url
from django.urls import path

from articulos.api.views import (
	ArticuloCreateAPIView,
	ArticuloDeleteAPIView,
	ArticuloDetailAPIView,
	ArticuloListAPIView,
	ArticuloUpdateAPIView
	)

urlpatterns = [
    path(r'', ArticuloListAPIView.as_view(), name='list-articulo'),
    path(r'create/', ArticuloCreateAPIView.as_view(), name='create-articulo'),
    url(r'^(?P<id_articulo>\d+)/$', ArticuloDetailAPIView.as_view(), name='detail-articulo'),
    url(r'(?P<id_articulo>\d+)/delete/', ArticuloDeleteAPIView.as_view(), name='delete-articulo'),
    url(r'(?P<id_articulo>\d+)/edit/', ArticuloUpdateAPIView.as_view(), name='update-articulo'),
]