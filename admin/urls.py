from django.conf.urls import patterns,url


urlpatterns = patterns('admin.views',
	url(r'^$',		'index_view',		name = 'index_view'),
	url(r'^login/$',	'login_view',		name = 'login_view'),
	url(r'^logout/$',	'logout_view',		name = 'logout_view'),

	# Locales.
	url(r'^local/$',						'list_local_view',		name = 'list_local_view'),
	url(r'^local/add$',					'add_local_view',		name = 'add_local_view'),
	url(r'^local/edit/(?P<id>.*)/$',		'edit_local_view',		name = 'edit_local_view'),
	url(r'^local/delete/(?P<id>.*)/$',	'delete_local_view',	name = 'delete_local_view'),

	# Habitaciones.
	url(r'^habitacion/$',						'list_habitacion_view',		name = 'list_habitacion_view'),
	url(r'^habitacion/add$',					'add_habitacion_view',		name = 'add_habitacion_view'),
	url(r'^habitacion/edit/(?P<id>.*)/$',		'edit_habitacion_view',		name = 'edit_habitacion_view'),
	url(r'^habitacion/delete/(?P<id>.*)/$',	'delete_habitacion_view',	name = 'delete_habitacion_view'),

	# Puntos.
	url(r'^punto/$',						'list_punto_view',		name = 'list_punto_view'),
	url(r'^punto/add$',					'add_punto_view',		name = 'add_punto_view'),
	url(r'^punto/edit/(?P<id>.*)/$',		'edit_punto_view',		name = 'edit_punto_view'),
	url(r'^punto/delete/(?P<id>.*)/$',	'delete_punto_view',	name = 'delete_punto_view'),

	# Clientes.
	url(r'^cliente/$',						'list_cliente_view',		name = 'list_cliente_view'),
	url(r'^cliente/add$',						'add_cliente_view',			name = 'add_cliente_view'),
	url(r'^cliente/edit/(?P<id>.*)/$',		'edit_cliente_view',		name = 'edit_cliente_view'),
	url(r'^cliente/delete/(?P<id>.*)/$',		'delete_cliente_view',		name = 'delete_cliente_view'),

	# Tipos.
	url(r'^tipo/$',						'list_tipo_view',		name = 'list_tipo_view'),
	url(r'^tipo/add$',					'add_tipo_view',		name = 'add_tipo_view'),
	url(r'^tipo/edit/(?P<id>.*)/$',		'edit_tipo_view',		name = 'edit_tipo_view'),
	url(r'^tipo/delete/(?P<id>.*)/$',		'delete_tipo_view',		name = 'delete_tipo_view'),

	# Productos.
	url(r'^producto/$',						'list_producto_view',		name = 'list_producto_view'),
	url(r'^producto/add$',					'add_producto_view',		name = 'add_producto_view'),
	url(r'^producto/edit/(?P<id>.*)/$',		'edit_producto_view',		name = 'edit_producto_view'),
	url(r'^producto/delete/(?P<id>.*)/$',		'delete_producto_view',		name = 'delete_producto_view'),

	# Platos.
	url(r'^plato/$',						'list_plato_view',		name = 'list_plato_view'),
	url(r'^plato/add$',					'add_plato_view',		name = 'add_plato_view'),
	url(r'^plato/edit/(?P<id>.*)/$',		'edit_plato_view',		name = 'edit_plato_view'),
	url(r'^plato/delete/(?P<id>.*)/$',	'delete_plato_view',	name = 'delete_plato_view'),

	# Usuarios.
	url(r'^user/$',						'list_user_view',		name = 'list_user_view'),
	url(r'^user/add$',					'add_user_view',		name = 'add_user_view'),
	url(r'^user/edit/(?P<id>.*)/$',		'edit_user_view',		name = 'edit_user_view'),
	url(r'^user/perm/(?P<id>.*)/$',		'perm_user_view',		name = 'perm_user_view'),
	
	#Stock productos
	url(r'^stock-producto/$',			'list_stock_producto_view',		name = 'list_stock_producto_view'),
)