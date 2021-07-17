from django.conf.urls import url
from django.urls import path

from proveedores.api.views import (
	ProveedorCreateAPIView,
	ProveedorDeleteAPIView,
	ProveedorDetailAPIView,
	ProveedorListAPIView,
	ProveedorUpdateAPIView
	)

urlpatterns = [
    path(r'', ProveedorListAPIView.as_view(), name='list-proveedor'),
    path(r'create/', ProveedorCreateAPIView.as_view(), name='create-proveedor'),
    url(r'^(?P<id_proveedor>\d+)/$', ProveedorDetailAPIView.as_view(), name='detail-proveedor'),
    url(r'(?P<id_proveedor>\d+)/delete/', ProveedorDeleteAPIView.as_view(), name='delete-proveedor'),
    url(r'(?P<id_proveedor>\d+)/edit/', ProveedorUpdateAPIView.as_view(), name='update-proveedor'),
]