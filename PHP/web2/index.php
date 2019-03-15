<?php include 'server.php'; ?>
<!DOCTYPE html>
<html>
<head>
	<title>System info</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>

	<div class="container">
		<h1>Server info</h1>
		<?php if($server): ?>
			<ul class="list-group">
				<?php foreach($sever as $key => $value): ?>
					<li class="list-group-item">
						<strong><?php echo $key; ?>: </strong>
						<?php echo $value; ?>
					</li>
				<?php endforeach; ?>
			</ul>
		<?php endif; ?>

		<h1>Client info</h1>
		<?php if($client): ?>
			<ul class="list-group">
				<?php foreach($client as $key => $value): ?>
					<li class="list-group-item">
						<strong><?php echo $key; ?>: </strong>
						<?php echo $value; ?>
					</li>
				<?php endforeach; ?>
			</ul>
		<?php endif; ?>
	</div>

</body>
</html>