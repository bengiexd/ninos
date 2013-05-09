# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import stock_producto, punto, producto
from admin.forms import addStockProductosForm, consumoStockProductosForm, pedidoStockProductosForm

from datetime import datetime
import base64

# Locales.
@login_required(login_url = '/login/')
def list_stock_producto_view(request):
	stock = stock_producto.objects.raw('SELECT *, SUM(cantidad) AS saldo FROM admin_stock_producto GROUP BY punto_destino_id, producto_id HAVING saldo > 0;')
	
	context = {'stock': stock}
	return render_to_response('admin/stock-producto/list.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def add_stock_producto_view(request):
	if request.method == "POST":
		form = addStockProductosForm(request.POST)
		r = request.POST.copy()
		
		try:
			_hecho_por = request.user
			_punto_destino = punto.objects.get(id = r.get('punto_destino'))
			_punto_origen = r.get('punto_destino')
			_producto  = producto.objects.get(id = r.get('producto'))
			_cantidad = eval(r.get('cantidad'))
			_detalle = r.get('detalle')
			_fecha = datetime.now()
		
			if (_cantidad > 0):
				
				s = stock_producto(hecho_por = _hecho_por, punto_origen = _punto_origen, punto_destino = _punto_destino,
								producto = _producto, cantidad = _cantidad, detalle = _detalle, fecha = _fecha)
				s.save()
				messages.success(request, 'Se agrego los productos.')
				return HttpResponseRedirect(reverse('list_stock_producto_view'))			
			else:
				messages.error(request, 'Cantidad no es válida')
		except:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addStockProductosForm()
	context = {'form': form}

	return render_to_response('admin/stock-producto/add.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def consumo_stock_producto_view(request, oid, pid):
	if request.method == "POST":
		form = consumoStockProductosForm(request.POST)
		r = request.POST.copy()
		
		try:
			_hecho_por = request.user
			_punto_destino = punto.objects.get(id = r.get('oid')) #oid : punto_origen_id
			_punto_origen = r.get('oid')
			_producto  = producto.objects.get(id = r.get('pid')) #pid : producto_id
			_cantidad = eval(r.get('cantidad'))
			_detalle = r.get('detalle')
			_fecha = datetime.now()
			
			_stk = stock_producto.objects.raw('SELECT *, SUM(cantidad) AS saldo FROM admin_stock_producto WHERE producto_id=\'%s\' AND punto_destino_id=\'%s\' GROUP BY producto_id;' % (_producto.id, _punto_destino.id))
			_max_cant = _stk[0].saldo  #eval(r.get('maxp'))
		
			if (_cantidad > 0 and _cantidad <= _max_cant):
				_cantidad = _cantidad*-1 #debe ser negativa
				s = stock_producto(hecho_por = _hecho_por, punto_origen = _punto_origen, punto_destino = _punto_destino,
								producto = _producto, cantidad = _cantidad, detalle = _detalle, fecha = _fecha)
				s.save()
				messages.success(request, 'Se consumio los productos.')
				return HttpResponseRedirect(reverse('list_stock_producto_view'))			
			else:
				messages.error(request, 'Cantidad no es válida')
		except:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = consumoStockProductosForm(initial={'oid': oid, 'pid': pid})
	context = {'form': form}

	return render_to_response('admin/stock-producto/consumo.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def pedido_stock_producto_view(request, oid, pid):
	if request.method == "POST":
		form = pedidoStockProductosForm(request.POST)
		r = request.POST.copy()
		
		try:
			_hecho_por = request.user
			_punto_destino = punto.objects.get(id = r.get('punto_destino'))
			_punto_origen = r.get('oid')
			_producto  = producto.objects.get(id = r.get('pid')) #pid : producto_id
			_cantidad = eval(r.get('cantidad'))
			_detalle = r.get('detalle')
			_fecha = datetime.now()
			
			_stk = stock_producto.objects.raw('SELECT *, SUM(cantidad) AS saldo FROM admin_stock_producto WHERE producto_id=\'%s\' AND punto_destino_id=\'%s\' GROUP BY producto_id;' % (_producto.id, r.get('oid')))
			_max_cant = _stk[0].saldo
		
			if (_cantidad > 0 and _cantidad <= _max_cant):
				_cantidad = _cantidad
				s = stock_producto(hecho_por = _hecho_por, punto_origen = _punto_origen, punto_destino = _punto_destino,
								producto = _producto, cantidad = _cantidad, detalle = _detalle, fecha = _fecha)
				s.save()
				
				s = stock_producto(hecho_por = _hecho_por, punto_origen = _punto_origen, punto_destino = punto.objects.get(id = r.get('oid')),
								producto = _producto, cantidad = _cantidad*-1, detalle = _detalle, fecha = _fecha)
				s.save()				
				messages.success(request, 'Se efectuo pedido de los productos.')
				return HttpResponseRedirect(reverse('list_stock_producto_view'))			
			else:
				messages.error(request, 'Cantidad no es válida')
		except:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = pedidoStockProductosForm(initial={'oid': oid, 'pid': pid})
	context = {'form': form}

	return render_to_response('admin/stock-producto/pedido.html', context, context_instance = RequestContext(request))