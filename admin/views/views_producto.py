# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import producto
from admin.forms import addProductoForm

# Productos.
def list_producto_view(request):
	productos = producto.objects.filter()
	context = {'productos': productos}
	return render_to_response('admin/producto/list.html', context, context_instance = RequestContext(request))

def add_producto_view(request):
	if request.method == "POST":
		form = addProductoForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se creó el producto.')
			return HttpResponseRedirect(reverse('list_producto_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addProductoForm()
	context = {'form': form}

	return render_to_response('admin/producto/add.html', context, context_instance = RequestContext(request))

def edit_producto_view(request, id):
	try:
		p = producto.objects.get(id = id)
	except producto.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addProductoForm(request.POST, instance = p)
		if form.is_valid():
			edit = form.save(commit = False)
			edit.save()
			messages.success(request, 'Se actualizó el producto.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addProductoForm(instance = p)

	context = {'form': form, 'producto': p}
	return render_to_response('admin/producto/edit.html', context, context_instance = RequestContext(request))

def delete_producto_view(request, id):
	try:
		p = producto.objects.get(id = id)
	except producto.DoesNotExist:
		raise Http404

	p.delete()
	messages.success(request, 'Se borró el producto.')
	return HttpResponseRedirect(reverse('list_producto_view'))