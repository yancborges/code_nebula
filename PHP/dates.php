<?php

	echo date();
	// Parameters:

	// Date values
	// 'd' = Day
	// 'm' = Month
	// 'Y' = Year
	// 'l' = Day of the week

	// Time values
	// 'h' = Hour
	// 'i' = Minutes
	// 's' = Seconds
	// 'a' = AM/PM

	echo date('Y/m/d');
	echo date('h:i:sa');

	// Time zone
	date_default_timezone_set('America/New_York');

	// Creating a timestamp
	$timestamp = mktime(10, 14, 51, 9, 10, 1981);

	// Formatting timestamp
	echo date('Y/m/d',$timestamp);

	// Converting text to timestamp
	$timestamp2 = strtotime('7:00pm March 22 2016');
	$timestamp3 = strtotime('tomorrow');
	$timestamp4 = strtotime('next saturday');
	$timestamp5 = strtotime('+2 months');
	// It actually works!
	echo $timestamp2;

	




?>