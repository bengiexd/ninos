# -*- coding: utf-8 -*-

from django import forms
from admin.models import local, habitacion, cliente, tipo, producto, plato, punto
from django.contrib.auth.models import User, Permission, Group

# Administración.
class addLocalForm(forms.ModelForm):
	class Meta:
		model = local

	def __init__(self, *args, **kwargs):
		super(addLocalForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

class addHabitacionForm(forms.ModelForm):
	class Meta:
		model = habitacion

	def __init__(self, *args, **kwargs):
		super(addHabitacionForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

class addPuntoForm(forms.ModelForm):
	class Meta:
		model = punto

	def __init__(self, *args, **kwargs):
		super(addPuntoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

class addClienteForm(forms.ModelForm):
	class Meta:
		model = cliente

	def __init__(self, *args, **kwargs):
		super(addClienteForm, self).__init__(*args, **kwargs)
		self.fields['nombres'].widget.attrs['class'] = "input-xlarge"
		self.fields['apellidos'].widget.attrs['class'] = "input-xlarge"

# Cocina.
class addTipoForm(forms.ModelForm):
	class Meta:
		model = tipo

	def __init__(self, *args, **kwargs):
		super(addTipoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

class addProductoForm(forms.ModelForm):
	class Meta:
		model = producto

	def __init__(self, *args, **kwargs):
		super(addProductoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

class addPlatoForm(forms.ModelForm):
	class Meta:
		model = plato

	def __init__(self, *args, **kwargs):
		super(addPlatoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

# Usuarios
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		widgets = {
            'password': forms.PasswordInput(),
        }

# Grupos
class GroupForm(forms.Form):
	grupos = forms.ModelChoiceField(queryset=Group.objects.all(), required = True)

	def clean(self):
		return self.cleaned_data

	def __init__(self, *args, **kwargs):
		my_group = kwargs.pop('grupo', None)

		super(GroupForm, self).__init__(*args, **kwargs)
		modelchoicefields = [field for field_name, field in self.fields.iteritems() if
			isinstance(field, forms.ModelChoiceField)]

		for field in modelchoicefields:
			field.empty_label = None
			if my_group:
				field.initial = my_group