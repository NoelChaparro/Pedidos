from django.shortcuts import render, redirect, reverse

from .forms import DetallePedidoForm,PedidoForm
from articulos.models import Articulo
from clientes.models import Cliente
from .models import DetallePedido,Pedido

def crear_pedido(request):

	if request.method=='POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			cliente = request.POST['cliente']
			fecha_surtido = request.POST['fecha_surtido']
			if fecha_surtido=='':
				fecha_surtido= None
			
			if 'urgente' in request.POST:
			    urgente = True
			else:
			    urgente = False

			tipo_pedido = request.POST['tipo_pedido']
			
			pedido = Pedido.objects.create(cliente=Cliente.objects.get(id_cliente=cliente), fecha_surtido=fecha_surtido, urgente=urgente, tipo_pedido=tipo_pedido)
			
			return redirect(reverse('detalle-pedido', kwargs={"pedido":pedido.numero_pedido}))
	else:
		form = PedidoForm(auto_id='%s')
	return render(request,"crear_pedido.html", {'formulario_pedido':form})

def detalle_pedido(request, pedido):
	form = DetallePedidoForm(auto_id='%s')
	p = Pedido.objects.get(numero_pedido=pedido)
	dp = DetallePedido.objects.filter(pedido = pedido)
	context = {
		'formulario_detalle_pedido':form,
		'numero_pedido': p.numero_pedido,
		'detalle_pedidos': dp
	}
	if request.method=='POST':
		form = DetallePedidoForm(request.POST)
		pedido = Pedido.objects.get(numero_pedido=request.POST['numero_pedido'])
		articulo = Articulo.objects.get(id_articulo=request.POST['articulo'])
		cantidad = request.POST['cantidad_articulos']
		DetallePedido.objects.create(pedido=pedido, articulo=articulo, cantidad_articulos= cantidad)		

	return render(request,"detalle_pedido.html", context)

def pedido_detail_view(request):
	obj = Pedido.objects.filter(urgente=True,tipo_pedido='1',fecha_surtido=None,cliente__tipo_cliente="PLATINO")

	context = {
		'pedidos': obj,
	}

	return render(request,"pedidos.html", context)