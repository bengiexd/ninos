from django.db import models
from django.contrib.auth.models import User
from decimal import *

# Lugares.
class local(models.Model):
	nombre = models.CharField(max_length = 255)

	def __unicode__(self):
		return self.nombre

class habitacion(models.Model):
	nombre = models.CharField(max_length = 255)
	pertenece_a = models.ForeignKey(local)

	def __unicode__(self):
		return "%s: %s"%(self.pertenece_a, self.nombre)

class punto(models.Model):
	nombre = models.CharField(max_length = 100)
	pertenece_a	 = models.ForeignKey(local)

	def __unicode__(self):
		return "%s: %s"%(self.pertenece_a, self.nombre)

class cliente(models.Model):
	nombres = models.CharField(max_length = 255)
	apellidos = models.CharField(max_length = 255)
	hospedado_en = models.ForeignKey(habitacion)
	activo = models.BooleanField(default = True)

	def __unicode__(self):
		completo = "%s %s"%(self.nombres, self.apellidos)
		return completo

# Cocina.
class tipo(models.Model):
	RECIBOS = (
		('C', 'Comanda'),
		('D', 'Detalle de Consumo'),
	)
	nombre = models.CharField(max_length = 100)
	recibo = models.CharField(max_length = 1, choices = RECIBOS, default = 'D')

	def __unicode__(self):
		return self.nombre

class producto(models.Model):
	nombre = models.CharField(max_length = 255)
	tipo = models.ForeignKey(tipo)

	def __unicode__(self):
		return self.nombre

class plato(models.Model):
	nombre = models.CharField(max_length = 255)
	tipo = models.ForeignKey(tipo)
	precio = models.DecimalField(max_digits = 5, decimal_places = 2, default=Decimal('0.00'))
	de_venta_en = models.ManyToManyField(punto)
	
	def __unicode__(self):
		return self.nombre

#Pedidos Stock
class stock_producto(models.Model):
	hecho_por = models.ForeignKey(User)
	punto_origen = models.IntegerField()
	punto_destino = models.ForeignKey('admin.punto')
	producto  = models.ForeignKey('admin.producto')
	cantidad = models.IntegerField()
	detalle = models.CharField(max_length = 255)
	fecha = models.DateTimeField()
	
# Pedidos
class pedido(models.Model):
	ESTADOS = (
		('R', 'Recibido'),
		('A', 'Atendido'),
		('I', 'Impreso'),
		('P', 'Pagado'),
	)
	hecho_por = models.ForeignKey(User)
	para = models.ForeignKey(cliente)
	cuando = models.DateTimeField()
	estado = models.CharField(max_length = 1, choices = ESTADOS, default = 'R')
	notas = models.TextField()

class pedido_detalle(models.Model):
	pertenece_al_pedido = models.ForeignKey(pedido)
	plato = models.ForeignKey(plato)
	cantidad = models.IntegerField()