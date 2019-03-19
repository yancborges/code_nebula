<?php

	if(filter_has_var(INPUT_POST, 'data')) {
		echo 'Data found';
	}
	else {
		echo 'No data';
	}

	if(filter_has_var(INPUT_POST, 'data')) {
		$email = $_POST['data'];
		$email = filter_var($email, FILTER_SANITIZE_EMAIL);

		if(filter_input(INPUT_POST, 'data', FILTER_VALIDATE_EMAIL)) {
			echo 'Email valod!';
		}
		else {
			echo 'dats not a email';
		}
	}

	$var = '<script>alert(1)</script>';
	echo filter_var($var, FILTER_SANITIZE_SPECIAL_CHARS);

?>

<form method='post' action="<?php echo $_SERVER['PHP_SELF']; ?>">
	<input type="text" name="data">
	<button type="submit">Submit</button>
</form>