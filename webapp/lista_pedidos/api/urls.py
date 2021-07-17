from django.conf.urls import url
from django.urls import path

from lista_pedidos.api.views import (
	CentroDistribucionCreateAPIView,
	CentroDistribucionDeleteAPIView,
	CentroDistribucionDetailAPIView,
	CentroDistribucionListAPIView,
	CentroDistribucionUpdateAPIView,
	DetallePedidoCreateAPIView,
	DetallePedidoDeleteAPIView,
	DetallePedidoDetailAPIView,
	DetallePedidoListAPIView,
	DetallePedidoUpdateAPIView,
	EmpresaAsociadaCreateAPIView,
	EmpresaAsociadaDeleteAPIView,
	EmpresaAsociadaDetailAPIView,
	EmpresaAsociadaListAPIView,
	EmpresaAsociadaUpdateAPIView,
	PedidoCreateAPIView,
	PedidoDeleteAPIView,
	PedidoDetailAPIView,
	PedidoListAPIView,
	PedidoUpdateAPIView,
	PedidosUrgentesListAPIView,
	SucursalCreateAPIView,
	SucursalDeleteAPIView,
	SucursalDetailAPIView,
	SucursalListAPIView,
	SucursalUpdateAPIView
	)

urlpatterns = [
    path(r'', PedidoListAPIView.as_view(), name='list-pedido'),
    path(r'create/', PedidoCreateAPIView.as_view(), name='create-pedido'),
    url(r'^(?P<numero_pedido>\d+)/$', PedidoDetailAPIView.as_view(), name='detail-pedido'),
    url(r'(?P<numero_pedido>\d+)/delete/', PedidoDeleteAPIView.as_view(), name='delete-pedido'),
    url(r'^(?P<numero_pedido>\d+)/edit/$', PedidoUpdateAPIView.as_view(), name='update-pedido'),
    path(r'detalle-pedido/', DetallePedidoListAPIView.as_view(), name='list-detalle-pedido'),
    path(r'create-detalle-pedido/', DetallePedidoCreateAPIView.as_view(), name='create-detalle-pedido'),
    url(r'detalle-pedido/(?P<id_detalle>\d+)/$', DetallePedidoDetailAPIView.as_view(), name='detail-detalle-pedido'),
    url(r'detalle-pedido/(?P<id_detalle>\d+)/delete/', DetallePedidoDeleteAPIView.as_view(), name='delete-detalle-pedido'),
    url(r'detalle-pedido/(?P<id_detalle>\d+)/edit/$', DetallePedidoUpdateAPIView.as_view(), name='update-detalle-pedido'),
    path(r'centro-distribucion/', CentroDistribucionListAPIView.as_view(), name='list-centro-distribucion'),
    path(r'create-centro-distribucion/', CentroDistribucionCreateAPIView.as_view(), name='create-centro-distribucion'),
    url(r'centro-distribucion/(?P<pedido>\d+)/$', CentroDistribucionDetailAPIView.as_view(), name='detail-centro-distribucion'),
    url(r'centro-distribucion/(?P<pedido>\d+)/delete/', CentroDistribucionDeleteAPIView.as_view(), name='delete-centro-distribucion'),
    url(r'^centro-distribucion/(?P<pedido>\d+)/edit/$', CentroDistribucionUpdateAPIView.as_view(), name='update-centro-distribucion'),
    path(r'sucursal/', SucursalListAPIView.as_view(), name='list-sucursal'),
    path(r'create-sucursal/', SucursalCreateAPIView.as_view(), name='create-sucursal'),
    url(r'sucursal/(?P<pedido>\d+)/$', SucursalDetailAPIView.as_view(), name='detail-sucursal'),
    url(r'sucursal/(?P<pedido>\d+)/delete/', SucursalDeleteAPIView.as_view(), name='delete-sucursal'),
    url(r'^sucursal/(?P<pedido>\d+)/edit/$', SucursalUpdateAPIView.as_view(), name='update-sucursal'),
    path(r'empresa-asociada/', EmpresaAsociadaListAPIView.as_view(), name='list-empresa-asociada'),
    path(r'create-empresa-asociada/', EmpresaAsociadaCreateAPIView.as_view(), name='create-empresa-asociada'),
    url(r'empresa-asociada/(?P<pedido>\d+)/$', EmpresaAsociadaDetailAPIView.as_view(), name='detail-empresa-asociada'),
    url(r'empresa-asociada/(?P<pedido>\d+)/delete/', EmpresaAsociadaDeleteAPIView.as_view(), name='delete-empresa-asociada'),
    url(r'^empresa-asociada/(?P<pedido>\d+)/edit/$', EmpresaAsociadaUpdateAPIView.as_view(), name='update-empresa-asociada'),
    
    path(r'pedidos-urgentes/', PedidosUrgentesListAPIView.as_view(), name='pedidos-urgentes'),
]