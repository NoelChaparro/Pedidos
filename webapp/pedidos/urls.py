"""pedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include,path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import home
from lista_pedidos.views import crear_pedido,detalle_pedido,pedido_detail_view

schema_view = get_schema_view(
   openapi.Info(
      title="Pedidos API Docs",
      default_version='v1',
      description="Pedidos Mobilender",
      terms_of_service="None",
      contact=openapi.Contact(email="noel.chaparro@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('crear-pedido/', crear_pedido, name='crear-pedido'),
    url(r'detalle-pedido/(?P<pedido>[0-9]+)/$', detalle_pedido, name='detalle-pedido'),
    path('lista-pedidos/', pedido_detail_view, name='pedidos-urgentes'),
    path(r'api/articulos/', include(('articulos.api.urls','articulos'), namespace='articulos-api')),
    path(r'api/clientes/', include(('clientes.api.urls','clientes'), namespace='clientes-api')),
    path(r'api/pedidos/', include(('lista_pedidos.api.urls','lista_pedidos'), namespace='lista-pedidos-api')),
    path(r'api/proveedores/', include(('proveedores.api.urls','proveedores'), namespace='proveedores-api')),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
