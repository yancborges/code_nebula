<?php

	$loggedIn = true;
	$arr = [1,2,3,5,3,7,9,4,8];

	if($loggedIn) {
		echo 'You\'re logged!';
	}
	else {
		echo 'Hey, not logged >:(';
	}

	echo($loggedIn) ? 'You\'re logged!' : 'Hey, not logged >:(';
	$isRegistered = ($loggedIn == true) ? true : false;

	$age = 10;
	$score = 40;
	echo 'Your score is: '.($score > 20 ? ($age > 10 ? 'Average:' : 'Exceptional ihaa'):($age > 10 ? 'Bad' : 'Meh'));

?>

<div>
	<?php
		if($loggedIn) { ?>
			<h1>Welcome dumb</h1>
		<?php }
	?>
</div>


<div>
	<?php if($loggedIn): ?>
		<h1>Welcome sir</h1>
	<?php else: ?>
		<h1>Welcome.. who?</h1>
	<?php endif; ?>
</div>

<div>
	<?php foreach($arr as $val): ?>
		<?php echo $val; ?>
	<?php endforeach; ?>
</div>
