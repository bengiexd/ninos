# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import local
from admin.forms import addLocalForm

# Locales.
def list_local_view(request):
	locales = local.objects.filter()
	context = {'locales': locales}
	return render_to_response('admin/local/list.html', context, context_instance = RequestContext(request))

def add_local_view(request):
	if request.method == "POST":
		form = addLocalForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se creó el local.')
			return HttpResponseRedirect(reverse('list_local_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addLocalForm()
	context = {'form': form}

	return render_to_response('admin/local/add.html', context, context_instance = RequestContext(request))

def edit_local_view(request, id):
	try:
		l = local.objects.get(id = id)
	except local.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addLocalForm(request.POST, instance = l)
		if form.is_valid():
			edit = form.save(commit = False)
			edit.save()
			messages.success(request, 'Se actualizó el local.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addLocalForm(instance = l)

	context = {'form': form, 'local': l}
	return render_to_response('admin/local/edit.html', context, context_instance = RequestContext(request))

def delete_local_view(request, id):
	try:
		l = local.objects.get(id = id)
	except local.DoesNotExist:
		raise Http404

	l.delete()
	messages.success(request, 'Se borró el local')
	return HttpResponseRedirect(reverse('list_local_view'))