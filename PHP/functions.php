<?php

	function test(){
		echo 'Hey, printing something here, dont disturb me!';
	}

	test();

	function rateName($name){
		echo "Oh my god! $name looks like a dog name.";
	}

	rateName('Rex');

	function realConvertion($dollar){
		return $dollar * 4;
	}

	echo realConvertion(20.30);

	
	$food = 'Bacon';
	function makeASandwich(&$food){
		$food = $food . ' bread' . ' cheese';
	}

	makeASandwich($food);
	echo $food;

?>