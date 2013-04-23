# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import stock_producto
from admin.forms import addLocalForm

# Locales.
@login_required(login_url = '/login/')
def list_stock_producto_view(request):
	stock = stock_producto.objects.raw('SELECT *, SUM(cantidad) AS saldo FROM admin_stock_producto GROUP BY producto_id;')
	context = {'stock': stock}
	return render_to_response('admin/stock-producto/list.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def pedido_stock_producto_view(request):
	if request.method == "POST":
		form = addLocalForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se hizo el pedido.')
			return HttpResponseRedirect(reverse('pedido_stock_producto_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addLocalForm()
	context = {'form': form}

	return render_to_response('admin/stock-producto/pedido.html', context, context_instance = RequestContext(request))