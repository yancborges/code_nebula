<?php

	echo 'For Loop';

	// For
	for($i = 0; $i < 10; $i++) {
		echo $i;
	}

	echo '<br>While Loop';

	// While
	$i = 0;
	while($i < 10) {
		echo $i;
		$i++;
	}

	echo '<br>Do-while Loop';

	// Do While
	$i = 0;
	do{
		echo $i;
		$i++;
	}
	while($i < 10);

	echo '<br>Foreach Loop';

	// For each
	$burgers = ['Super cheese','Salada','Bacon','Bacon-egg'];
	foreach($burgers as $dish){
		echo $dish;
		echo '<br>';
	}

?>