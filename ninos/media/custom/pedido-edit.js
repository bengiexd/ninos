$('#id_clientes option[selected="selected"]').text('');
$('#id_platos option[selected="selected"]').text('');

$(function() {
	var PedidoModel = Backbone.Model.extend({
		defaults: function() {
			return {
				nombre: "",
				cantidad: 1
			};
		},

		validate: function(attrs) {
			var errors =[];
			cantidad = parseInt(attrs.cantidad);
			nombre = attrs.nombre;

			if(!_.isNumber(cantidad) || cantidad < 1) {
				errors.push({name: 'cantidad', message: 'Ingresa una cantidad correcta'});
			}

			if(_.isEmpty(nombre)) {
				errors.push({name: 'cantidad', message: 'Escoge un plato'});
			}
			return errors.length > 0 ? errors : false;
		}
	});

	var PedidoCollection = Backbone.Collection.extend({
		model: PedidoModel,
	});

	var pedidos = new PedidoCollection();

	pedidos.fetch({ url: django_json_url });

	console.log(pedidos);

	//pedidos.on("add, remove", updateLista());

	var platosDOM = $('#id_platos');
	var cantidadDOM = $('#id_cantidad');

	$('#add').click(function(event) {
		date = new Date();
		idPlato = platosDOM.val();
		nombrePlato = platosDOM.find('option:selected').html();
		cantidadPlato = cantidadDOM.val();
		pedido = new PedidoModel();
		
		pedido.set({
			id: idPlato,
			nombre: nombrePlato,
			cantidad: cantidadPlato
		});

		if(pedido.isValid()) {
			addPedido(pedido);
		} else {
			alert('Revisa los datos del pedido.');
		}

		// Fixme: Es mejor usar pedidos.on('add', updateLista());
		updateLista();

		clearPedido();
	});

	$("body").on("click", ".delete", function(event){
		removePedido($(event.currentTarget).parent().parent().data("plato-id"));
		// Fixme: Es mejor usar pedidos.on('remove', updateLista());
		updateLista();
	});

	function addPedido(pedido) {
		try {
			pedidos.add(pedido);
		} catch(error) {
			console.log(error.message);
		}
	}

	function removePedido(id) {
		pedidos.remove(pedidos.get(id));
	};

	function updateLista() {
		var $ul = $('#pedido-lista tbody');
		var template = $.trim($('#pedido-template tbody').html() || "Template no encontrado");

		$ul.empty();
		pedidos.each(function(pedido) {
			$ul.append(Mustache.render(template, pedido.toJSON()));
		}, this);
	}

	function clearPedido() {
		cantidadDOM.val(1);
		platosDOM.find('option').prop('selected', false);
		platosDOM.trigger("liszt:updated");;
	}

	$('#frm-add-pedido').submit(function(e) {
		var _cliente = $('#id_clientes').val();
		if(_.isEmpty(_cliente)) {
			alert('Escoge un cliente.');
			return false;
		}
		if(pedidos.length == 0) {
			alert('Ingresa al menos un plato.');
			return false;
		} else {
			_notas = $('#id_notas').val();
			token = $('input[name="csrfmiddlewaretoken"]').val();
			$.ajax({
				url: django_url,
				type: 'POST',
				data: {
					clientes: _cliente,
					cantidad: JSON.stringify(pedidos.pluck('cantidad')),
					platos: JSON.stringify(pedidos.pluck('id')),
					notas: _notas,
					csrfmiddlewaretoken: token,
				},
				datatype: 'JSON',
				success: function(data) {
					window.location = data.url
				},
				error: function(e) {
					alert('Ocurrió un error al procesar el pedido, intenta nuevamente.');
				}
			});
		}
	});

	updateLista();

	$(window).bind('beforeunload', function(event) {
        if (pedidos.length > 0) {
            return 'El detalle de este pedido aun no ha sido guardado.';
        }
    });
});