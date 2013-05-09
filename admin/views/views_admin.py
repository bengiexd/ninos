# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#@user_passes_test(not_admin)
def not_admin(user):
	if user:
		return user.groups.filter(name = 'Administradores').count() == 0
	return False

@login_required(login_url = '/login/')
def index_view(request):
	return render_to_response('admin/index.html', context_instance = RequestContext(request))

def login_view(request):
	if(request.user.is_authenticated()):
		return HttpResponseRedirect(reverse('index_view'))
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('index_view'))
				else:
					messages.error(request, 'El usuario no está activo. Contacte con el administrador.')
			else:
				messages.error(request, 'Revise el usuario o la contraseña.')

		return render_to_response('login.html', context_instance = RequestContext(request))


def logout_view(request):
	name = request.user.first_name
	logout(request)
	messages.success(request, 'Hasta pronto %'%(name))
	return render_to_response('login.html', context_instance = RequestContext(request))