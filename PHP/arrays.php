<?php

	// Indexed
	$food = array('Tomato','Carrot','Cheese','Nuts');
	echo $food[2];

	$prices = [3.50,2.30,1.99,3.34];
	echo $prices[0];

	$food[4] = 'Ketchup';
	$prices[4] = 0.25;

	$food[] = 'Peper';
	$prices[] = 1.30;

	echo count($food);

	print_r($food);

	var_dump($prices);

	// Associative
	$cities = array('Toronto' => 1,'Paris' => 25,'Tokyo' => 8);
	echo $cities['Toronto'];

	$cities['Singapura'] = 56;

	// Multi-Dimensional
	$hours = array(
		array('11:30',30,'Mike'),
		array('12:38',20,'George'),
		array('09:18',12,'Fernanda')
	);

	echo $hours[2][2];


?>