# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from admin.models import habitacion
from admin.forms import addHabitacionForm

# Habitaciones.
@login_required(login_url = '/login/')
def list_habitacion_view(request):
	habitaciones = habitacion.objects.filter()
	context = {'habitaciones': habitaciones}
	return render_to_response('admin/habitacion/list.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def add_habitacion_view(request):
	if request.method == "POST":
		form = addHabitacionForm(request.POST)
		if form.is_valid():
			add = form.save(commit = False)
			add.save()
			messages.success(request, 'Se creó la habitación.')
			return HttpResponseRedirect(reverse('list_habitacion_view'))
		else:
			messages.error(request, 'Ingresa todos los campos.')
	else:
		form = addHabitacionForm()
	context = {'form': form}

	return render_to_response('admin/habitacion/add.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def edit_habitacion_view(request, id):
	try:
		h = habitacion.objects.get(id = id)
	except habitacion.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = addHabitacionForm(request.POST, instance = h)
		if form.is_valid():
			edit = form.save(commit = False)
			edit.save()
			messages.success(request, 'Se actualizó la habitación.')
		else:
			messages.error(request, 'Ingresa todos los campos.')

	if request.method == "GET":
		form = addHabitacionForm(instance = h)

	context = {'form': form, 'habitacion': h}
	return render_to_response('admin/habitacion/edit.html', context, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def delete_habitacion_view(request, id):
	try:
		h = habitacion.objects.get(id = id)
	except habitacion.DoesNotExist:
		raise Http404

	h.delete()
	messages.success(request, 'Se borró la habitación.')
	return HttpResponseRedirect(reverse('list_habitacion_view'))