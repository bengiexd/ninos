# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import cliente
from admin.forms import addClienteForm

# Clientes.
def list_cliente_view(request):
	clientes = cliente.objects.filter().order_by('activo')
	context = {'clientes': clientes}
	return render_to_response('admin/cliente/list.html', context, context_instance = RequestContext(request))

def add_cliente_view(request):
	if request.method == "POST":
		form = addClienteForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se creó el cliente.')
			return HttpResponseRedirect(reverse('list_cliente_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addClienteForm()
	context = {'form': form}

	return render_to_response('admin/cliente/add.html', context, context_instance = RequestContext(request))

def edit_cliente_view(request, id):
	try:
		c = cliente.objects.get(id = id)
	except cliente.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addClienteForm(request.POST, instance = c)
		if form.is_valid():
			edit = form.save(commit = False)
			form.save()
			
			messages.success(request, 'Se actualizó el cliente.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addClienteForm(instance = c)

	context = {'form': form, 'cliente': c}
	return render_to_response('admin/cliente/edit.html', context, context_instance = RequestContext(request))

def delete_cliente_view(request, id):
	try:
		c = cliente.objects.get(id = id)
	except cliente.DoesNotExist:
		raise Http404

	c.delete()
	messages.success(request, 'Se borró el cliente.')
	return HttpResponseRedirect(reverse('list_cliente_view'))