<?php
	if(isset($_GET['name'])) {
		// Preventing XSS
		$name = htmlentities($_GET['name']);
		echo $name;
	}
	if(isset($_POST['name'])) {
		$name = htmlentities($_POST['name']);
		echo $name;
	}
	if(isset($_REQUEST['name'])) {
		// $_REQUEST superglobal works either with POST or GET methods
		$name = htmlentities($_REQUEST['name']);
		echo $name;
	}
	echo $_SERVER['QUERY_STRING'];
?>

<!DOCTYPE html>
<html>
<head>
	<title>My site</title>
</head>
<body>
	<form method="POST" action="getAndPost.php">
		<div>
			<label>Name</label><br>
			<input type="text" name="name">
		</div>
		<div>
			<label>Email</label><br>
			<input type="text" name="email">
		</div>
		<input type="submit" value="Submit">
	</form>
	<ul>
		<li>
			<a href="getAndPost.php?name=Xuxildo">Xuxildo</a>
		</li>
		<li>
			<a href="getAndPost.php?name=BobsOrVegana">Bobs</a>
		</li>
	</ul>
	<hi><?php echo "{$name}'s Progile"; ?></hi>
</body>
</html>