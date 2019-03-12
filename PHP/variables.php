<!-- Normal texting -->

hi!

<!-- php code -->
<?php
	echo 'Hi my darling';
	/* Prints something */
?>

<!-- php + html -->
<h1>
	<?php
		echo 'H1 text';
	?>
</h1>

<!-- Variables -->
<?php
	
	// String
	$_string = 'Hello, my name is Goku';
	echo $_string;

	// Integer
	$_num = 4;

	// Float
	$_float = 3.6;

	// Boolean
	$_boolean = true;

	$num1 = 1;
	$num2 = 30;
	$sum = $num1 + $num2;

	$hello1 = 'Potato';
	$hello2 = 'Bread';
	$string_sum = $hello1 . ' ' . $hello2;

	echo "$hello1 $hello2";

	// Constants
	define('MESSAGE','Hey. You have a message!');
	echo message;

?>