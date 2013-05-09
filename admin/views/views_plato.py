# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

from admin.models import plato
from admin.forms import addPlatoForm

# Platos.
@login_required(login_url = '/login/')
def list_plato_view(request):
	platos = plato.objects.filter()
	context = {'platos': platos}
	return render_to_response('admin/plato/list.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def add_plato_view(request):
	if request.method == "POST":
		form = addPlatoForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			form.save_m2m()
			messages.success(request, 'Se creó el plato.')
			return HttpResponseRedirect(reverse('list_plato_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addPlatoForm()
	context = {'form': form}

	return render_to_response('admin/plato/add.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def edit_plato_view(request, id):
	try:
		p = plato.objects.get(id = id)
	except plato.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addPlatoForm(request.POST, instance = p)
		if form.is_valid():
			edit = form.save(commit = False)
			form.save_m2m()
			edit.save()
			messages.success(request, 'Se actualizó el plato.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addPlatoForm(instance = p)

	context = {'form': form, 'plato': p}
	return render_to_response('admin/plato/edit.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def delete_plato_view(request, id):
	try:
		p = plato.objects.get(id = id)
	except plato.DoesNotExist:
		raise Http404

	p.delete()
	messages.success(request, 'Se borró el plato.')
	return HttpResponseRedirect(reverse('list_plato_view'))


@login_required(login_url = '/login/')
def json_plato_view(request):
	platos = plato.objects.filter()
	data = serializers.serialize("json", platos)
	return HttpResponse(data, mimetype = 'application/json')