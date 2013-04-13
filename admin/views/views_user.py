# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
import datetime

from admin.forms import UserForm, GroupForm

def list_user_view(request):
	u = User.objects.all()
	context = {'users': u}
	return render_to_response('admin/user/list.html', context, context_instance = RequestContext(request))

def add_user_view(request):
	uform = UserForm()
	if request.method == "POST":
		data = request.POST.copy()
		data['date_joined'] = datetime.date.today()
		data['last_login'] = datetime.date.today()
		uform = UserForm(data)
		if uform.is_valid():
			user = uform.save(commit = False)
			user.set_password(data['password'])
			user.save()
			messages.success(request, 'Se creó el usuario.')
			return HttpResponseRedirect(reverse('list_user_view'))
		else:
			messages.error(request, dict(uform.errors.items()))
			context = {'form': uform}
			return render_to_response('admin/user/add.html', context, context_instance = RequestContext(request))
	else:
		uform = UserForm()
		context = {'form': uform}
		return render_to_response('admin/user/add.html', context, context_instance = RequestContext(request))

def edit_user_view(request, id):
	try:
		u = User.objects.get(id = id)
	except User.DoesNotExist:
		raise Http404

	if request.method == "POST":
		flag = False
		data = request.POST.copy()
		data['date_joined'] = datetime.date.today()
		data['last_login'] = datetime.date.today()
		if(len(data['password']) == 0):
			flag = True
			data['password'] = u.password
		form = UserForm(data, instance = u)
		if form.is_valid():
			edit = form.save(commit = False)
			if not flag:
				u.set_password(data['password'])
			edit.save()
			messages.success(request, 'Se actualizó el usuario.')
		else:
			messages.error(request, "Ingresa todos los campos. %s"%(dict(form.errors.items())))

	if request.method == "GET":
		form = UserForm(instance = u)

	context = {'form': form, 'user': u}
	return render_to_response('admin/user/edit.html', context, context_instance = RequestContext(request))

def perm_user_view(request, id):
	try:
		u = User.objects.get(id = id)
	except User.DoesNotExist:
		raise Http404

	if request.method == "GET":
		form = GroupForm()

	context = {'form': form, 'user': u}
	return render_to_response('admin/user/group.html', context, context_instance = RequestContext(request))