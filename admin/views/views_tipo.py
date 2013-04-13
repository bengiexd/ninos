# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import tipo
from admin.forms import addTipoForm

# Tipos.
def list_tipo_view(request):
	tipos = tipo.objects.filter()
	context = {'tipos': tipos}
	return render_to_response('admin/tipo/list.html', context, context_instance = RequestContext(request))

def add_tipo_view(request):
	if request.method == "POST":
		form = addTipoForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se creó el tipo.')
			return HttpResponseRedirect(reverse('list_tipo_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addTipoForm()
	context = {'form': form}

	return render_to_response('admin/tipo/add.html', context, context_instance = RequestContext(request))

def edit_tipo_view(request, id):
	try:
		t = tipo.objects.get(id = id)
	except tipo.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addTipoForm(request.POST, instance = t)
		if form.is_valid():
			edit = form.save(commit = False)
			edit.save()
			messages.success(request, 'Se actualizó el tipo.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addTipoForm(instance = t)

	context = {'form': form, 'tipo': t}
	return render_to_response('admin/tipo/edit.html', context, context_instance = RequestContext(request))

def delete_tipo_view(request, id):
	try:
		t = tipo.objects.get(id = id)
	except tipo.DoesNotExist:
		raise Http404

	t.delete()
	messages.success(request, 'Se borró el tipo.')
	return HttpResponseRedirect(reverse('list_tipo_view'))