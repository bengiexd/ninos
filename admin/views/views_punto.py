# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import punto
from admin.forms import addPuntoForm

# Habitaciones.
def list_punto_view(request):
	puntos = punto.objects.filter()
	context = {'puntos': puntos}
	return render_to_response('admin/punto/list.html', context, context_instance = RequestContext(request))

def add_punto_view(request):
	if request.method == "POST":
		form = addPuntoForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se creó el punto de venta.')
			return HttpResponseRedirect(reverse('list_punto_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addPuntoForm()
	context = {'form': form}

	return render_to_response('admin/punto/add.html', context, context_instance = RequestContext(request))

def edit_punto_view(request, id):
	try:
		p = punto.objects.get(id = id)
	except punto.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addPuntoForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			pertenece_a = form.cleaned_data['pertenece_a']
			p.nombre = nombre
			p.pertenece_a = pertenece_a
			p.save()
			messages.success(request, 'Se actualizó el punto de venta.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addPuntoForm(initial = {
			'nombre': p.nombre,
			'pertenece_a': p.pertenece_a
			})

	context = {'form': form, 'punto': p}
	return render_to_response('admin/punto/edit.html', context, context_instance = RequestContext(request))

def delete_punto_view(request, id):
	try:
		p = punto.objects.get(id = id)
	except punto.DoesNotExist:
		raise Http404

	p.delete()
	messages.success(request, 'Se borró el punto de venta.')
	return HttpResponseRedirect(reverse('list_punto_view'))