from django.conf.urls import patterns,url


urlpatterns = patterns('admin.views',
	url(r'^admin/$',		'index_view',		name = 'index_view'),
	# url(r'^admin/login/$',	'login_view',		name = 'login_view'),
	# url(r'^admin/logout/$',	'logout_view',		name = 'logout_view'),

	# Locales.
	url(r'^admin/local/$',						'list_local_view',		name = 'list_local_view'),
	url(r'^admin/local/add$',					'add_local_view',		name = 'add_local_view'),
	url(r'^admin/local/edit/(?P<id>.*)/$',		'edit_local_view',		name = 'edit_local_view'),
	url(r'^admin/local/delete/(?P<id>.*)/$',	'delete_local_view',	name = 'delete_local_view'),

	# Habitaciones.
	url(r'^admin/habitacion/$',						'list_habitacion_view',		name = 'list_habitacion_view'),
	url(r'^admin/habitacion/add$',					'add_habitacion_view',		name = 'add_habitacion_view'),
	url(r'^admin/habitacion/edit/(?P<id>.*)/$',		'edit_habitacion_view',		name = 'edit_habitacion_view'),
	url(r'^admin/habitacion/delete/(?P<id>.*)/$',	'delete_habitacion_view',	name = 'delete_habitacion_view'),

	# Puntos.
	url(r'^admin/punto/$',						'list_punto_view',		name = 'list_punto_view'),
	url(r'^admin/punto/add$',					'add_punto_view',		name = 'add_punto_view'),
	url(r'^admin/punto/edit/(?P<id>.*)/$',		'edit_punto_view',		name = 'edit_punto_view'),
	url(r'^admin/punto/delete/(?P<id>.*)/$',	'delete_punto_view',	name = 'delete_punto_view'),

	# Clientes.
	url(r'^admin/cliente/$',						'list_cliente_view',		name = 'list_cliente_view'),
	url(r'^admin/cliente/add$',						'add_cliente_view',			name = 'add_cliente_view'),
	url(r'^admin/cliente/edit/(?P<id>.*)/$',		'edit_cliente_view',		name = 'edit_cliente_view'),
	url(r'^admin/cliente/delete/(?P<id>.*)/$',		'delete_cliente_view',		name = 'delete_cliente_view'),

	# Tipos.
	url(r'^admin/tipo/$',						'list_tipo_view',		name = 'list_tipo_view'),
	url(r'^admin/tipo/add$',					'add_tipo_view',		name = 'add_tipo_view'),
	url(r'^admin/tipo/edit/(?P<id>.*)/$',		'edit_tipo_view',		name = 'edit_tipo_view'),
	url(r'^admin/tipo/delete/(?P<id>.*)/$',		'delete_tipo_view',		name = 'delete_tipo_view'),

	# Productos.
	url(r'^admin/producto/$',						'list_producto_view',		name = 'list_producto_view'),
	url(r'^admin/producto/add$',					'add_producto_view',		name = 'add_producto_view'),
	url(r'^admin/producto/edit/(?P<id>.*)/$',		'edit_producto_view',		name = 'edit_producto_view'),
	url(r'^admin/producto/delete/(?P<id>.*)/$',		'delete_producto_view',		name = 'delete_producto_view'),

	# Platos.
	url(r'^admin/plato/$',						'list_plato_view',		name = 'list_plato_view'),
	url(r'^admin/plato/add$',					'add_plato_view',		name = 'add_plato_view'),
	url(r'^admin/plato/edit/(?P<id>.*)/$',		'edit_plato_view',		name = 'edit_plato_view'),
	url(r'^admin/plato/delete/(?P<id>.*)/$',	'delete_plato_view',	name = 'delete_plato_view'),

	# Usuarios.
	url(r'^admin/user/$',						'list_user_view',		name = 'list_user_view'),
	url(r'^admin/user/add$',					'add_user_view',		name = 'add_user_view'),
	url(r'^admin/user/edit/(?P<id>.*)/$',		'edit_user_view',		name = 'edit_user_view'),
	url(r'^admin/user/perm/(?P<id>.*)/$',		'perm_user_view',		name = 'perm_user_view'),
)