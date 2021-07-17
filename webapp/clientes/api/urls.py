from django.conf.urls import url
from django.urls import path

from clientes.api.views import (
	ClienteCreateAPIView,
	ClienteDeleteAPIView,
	ClienteDetailAPIView,
	ClienteListAPIView,
	ClienteUpdateAPIView
	)

urlpatterns = [
    path(r'', ClienteListAPIView.as_view(), name='list'),
    path(r'create/', ClienteCreateAPIView.as_view(), name='create'),
    url(r'^(?P<codigo_cliente>[-\w]+)/$', ClienteDetailAPIView.as_view(), name='detail'),
    url(r'(?P<codigo_cliente>[-\w]+)/delete/', ClienteDeleteAPIView.as_view(), name='delete'),
    url(r'(?P<codigo_cliente>[-\w]+)/edit/', ClienteUpdateAPIView.as_view(), name='update'),
]