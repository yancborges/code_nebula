<?php

	
	// Matching value with ==
	$num = 3456;
	if($num == 3456){
		echo 'Wow, nice!';
	}

	// === Only returns true if it also matches the datatype
	$num = '3456';
	if($num === 3456){
		echo 'Hmmmm nice integer';
	}
	else {
		echo 'Hmmm, it\'s nice, but its not a integer, dude :(';
	}

	$num = 4;
	if($num > 4){
		echo 'High!';
	}
	elseif($num < 4){
		echo 'Low!';
	}
	else{
		echo 'RIIIIGHTTTTT!';
	}

	// Operators: < > <= >= != !==
	// Logical: AND && OR || XOR

	$food = 'cheese';
	switch($food){
		case 'cheese':
			echo 'Nice';
			break;
		case 'Bread':
			echo 'Its my daddy';
			break;
		case 'Fungus':
			echo 'U ok??';
			break;
		default:
			echo 'Hungry';
	}


?>