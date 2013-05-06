# -*- coding: utf-8 -*-

from django import forms
from admin.models import local, habitacion, cliente, tipo, producto, plato, punto, stock_producto
from django.contrib.auth.models import User, Permission, Group

from admin.widgets import NumberInput

# Administración.
class addLocalForm(forms.ModelForm):
	class Meta:
		model = local

	def __init__(self, *args, **kwargs):
		super(addLocalForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = "input-xlarge"

class addStockProductosForm(forms.ModelForm):
	class Meta:
		model = stock_producto

	def __init__(self, *args, **kwargs):
		super(addStockProductosForm, self).__init__(*args, **kwargs)
		self.fields['detalle'].widget.attrs['class'] = "input-xlarge"
		
class consumoStockProductosForm(forms.Form):
	oid = forms.IntegerField()
	pid  = forms.IntegerField()
	cantidad = forms.IntegerField()
	detalle = forms.CharField(max_length = 255)
	
	def __init__(self, *args, **kwargs):
		super(consumoStockProductosForm, self).__init__(*args, **kwargs)
		self.fields['detalle'].widget.attrs['class'] = "input-xlarge"	
	
class pedidoStockProductosForm(forms.ModelForm):
	oid = forms.IntegerField()
	pid  = forms.IntegerField()

	class Meta:
		model = stock_producto
		
	def __init__(self, *args, **kwargs):
		super(pedidoStockProductosForm, self).__init__(*args, **kwargs)
		self.fields['detalle'].widget.attrs['class'] = "input-xlarge"	

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
	grupos = forms.ModelChoiceField(queryset = Group.objects.all(), required = True)

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

# Pedidos
class PedidoForm(forms.Form):
	clientes = forms.ModelChoiceField(queryset = cliente.objects.filter(activo = True), required = True)
	platos = forms.ModelChoiceField(queryset = plato.objects.all())
	cantidad = forms.CharField(widget = NumberInput(attrs={'min': 1}))
	notas = forms.CharField(required = False, widget = forms.Textarea(attrs={'class':'autogrow', 'cols': 45, 'rows': 4}))

	def __init__(self, *args, **kwargs):
		super(PedidoForm, self).__init__(*args, **kwargs)
		self.fields['clientes'].widget.attrs['data-rel'] = "chosen"
		self.fields['clientes'].widget.attrs['data-placeholder'] = "Escoje un cliente"

		self.fields['platos'].widget.attrs['data-rel'] = "chosen"
		self.fields['platos'].widget.attrs['data-placeholder'] = "Escoje un plato"

		self.fields['cantidad'].widget.attrs['class'] = "cantidad-plato"
		self.fields['cantidad'].widget.attrs['placeholder'] = "Cantidad"
		self.fields['cantidad'].widget.attrs['value'] = "1"
