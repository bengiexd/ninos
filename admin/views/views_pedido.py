# -*- coding: utf-8 -*-

import datetime, json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, Http404, HttpResponse, QueryDict, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core import serializers

from admin.models import pedido, pedido_detalle, cliente, plato
from admin.forms import PedidoForm

# Pedidos.

@login_required(login_url = '/login/')
def list_pedido_view(request):
	pedidos = pedido.objects.filter()
	context = {'pedidos': pedidos}
	return render_to_response('admin/pedido/list.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def add_pedido_view(request):
	if request.method == "POST":
		dictx = request.POST.copy()
		_cliente = cliente.objects.get(id = dictx.get('clientes'))
		_cantidad = eval(dictx.get('cantidad'))
		_platos = eval(dictx.get('platos'))
		_notas = dictx.get('notas')

		try:
			p = pedido(hecho_por = request.user, para = _cliente, cuando = datetime.datetime.now(), notas = _notas)
			p.save()
		except:
			return HttpResponse(status = 500)

		for (key, _plato) in enumerate(_platos):
			pl = plato.objects.get(id = _plato)
			detalle = pedido_detalle(pertenece_al_pedido = p, plato = pl, cantidad = _cantidad[key])
			detalle.save()

		messages.success(request, 'El pedido se hizo correctamente.')

		context = {'url': reverse('list_pedido_view')}
		return HttpResponse(json.dumps(context), content_type="application/json")
	else:
		form = PedidoForm
	context = {'form': form}

	return render_to_response('admin/pedido/add.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login')
def edit_pedido_view(request, id):
	try:
		p = pedido.objects.get(id = id)
	except pedido.DoesNotExist:
		raise Http404

	form = PedidoForm
	context = {'form': form, 'pedido': p}
	return render_to_response('admin/pedido/edit.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def delete_pedido_view(request, id):
	try:
		p = pedido.objects.get(id = id)
	except pedido.DoesNotExist:
		raise Http404
	if(p.estado == 'R'):
		p.delete()
		messages.success(request, 'Se canceló el pedido.')
		return HttpResponseRedirect(reverse('list_pedido_view'))
	else:
		return HttpResponseForbidden('No se puede cancelar un pedido atendido.')

@login_required(login_url = '/login/')
def json_pedido_detalles_view(request, id):
	detalle = pedido_detalle.objects.filter(pertenece_al_pedido = id)
	data = serializers.serialize("json", detalle)
	return HttpResponse(data, mimetype = 'application/json')