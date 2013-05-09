tour = new Tour({
	labels: {
		next: "Siguiente »",
		prev: "« Previo",
		end: "Fin del tour",
	},
});

tour.addStep({
	element: '#id_clientes',
	title: 'Ayuda',
	content: 'Primero escoge el cliente'
});

tour.addStep({
	element: '#section-pedido',
	title: 'Ayuda',
	content: 'Ingresa los detalles del pedido'
});

tour.addStep({
	element: '#id_cantidad',
	title: 'Ayuda',
	content: 'Primero la cantidad'
});

tour.addStep({
	element: '#id_platos',
	title: 'Ayuda',
	content: 'Luego el plato'
	//placement: 'right'
});

tour.addStep({
	element: '#add',
	title: 'Ayuda',
	content: 'Agrega el pedido'
	//placement: 'right'
});

tour.addStep({
	element: '#pedido-lista',
	title: 'Ayuda',
	content: 'Revisa los pedidos, o quitalos'
	//placement: 'right'
});

tour.start();