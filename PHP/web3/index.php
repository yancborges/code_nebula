<?php 
	
	$error_msg = '';
	$error_class = '';

	if(filter_has_var(INPUT_POST, 'submit')) {

		$name = htmlspecialchars($_POST['name']);
		$email = $_POST['email'];
		$msg = $_POST['message'];

		if(!empty($email) && !empty($name) && !empty($msg)) {
			
			if(filter_var($email, FILTER_VALIDATE_EMAIL) === false) {

				$error_msg = 'Invalid email...';
				$error_class = 'alert alert-danger';

			}
			else {
				
				$to = 'antalord@anta-services.com';
				$subjetct = 'SITE CONTACT - '.$name;
				$body = '<h3>Contact from '.$name .' </h3>
						 <br><p>Email: ' .$email .' </p>
						 <br><p>Message: '.$msg .' </p>';

				$headers = "MIME-Version: 1.0" ."\r\n";
				$headers .= "Content-Type:text/html;charset=UTF-8". "\r\n";
				$headers .= "From: ".$name. "<" .$email. ">". "\r\n";

				if(mail($to, $subjetct, $body, $headers)) {

					$error_msg = 'Email sent!';
					$error_class = 'alert alert-success';

				}
				else{
					$error_msg = 'Something went wrong, try again later.';
					$error_class = $error_class = 'alert alert-danger';
				}
			}
		}
		else {

			$error_msg = 'Some fields are empty...';
			$error_class = 'alert alert-danger';

		}
	}
?>

<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	<title>Contact form</title>
</head>
<body>
	<nav class="navbar navbar-default">
		<div class="container">
			<div class="navbar-header">
				<a class="navabar-brand" href="index.php">Home</a>
			</div>
		</div>
	</nav>
	<div class="container">
		<?php if($error_msg != ''): ?>
			<div class="<?php echo $error_class; ?>"><?php echo $error_msg ?></div>
		<?php endif; ?>
		<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
			<div class="form-group">
				<label>Name</label>
				<input type="text" name="name" class="form-control" value="<?php echo isset($_POST['name']) ? $name : ''; ?>">
			</div>
			<div class="form-group">
				<label>Email</label>
				<input type="text" name="email" class="form-control" value="<?php echo isset($_POST['email']) ? $email : ''; ?>">
			</div>
			<div class="form-group">
				<label>Message</label>
				<input type="text" name="message" class="form-control" value="<?php echo isset($_POST['message']) ? $msg : ''; ?>">
			</div>
			<button type="submit" name="submit" class="btn btn-primary">Submit</button>
		</form>
	</div>
</body>
</html>