from django.db import models
from django.contrib.auth.models import User

# Almacen.
class stock_producto(models.Model):
	hecho_por = models.ForeignKey(User)
	producto  = models.ForeignKey('admin.producto')
	local = models.ForeignKey('admin.local')
	fecha = models.DateTimeField()
	cantidad = models.DateTimeField()

class stock_plato(models.Model):
	hecho_por = models.ForeignKey(User)
	plato  = models.ForeignKey('admin.plato')
	local = models.ForeignKey('admin.local')
	fecha = models.DateTimeField()
	cantidad = models.IntegerField()