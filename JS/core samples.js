// All this code was taken from CODECADEMY course.
// Coding here just for more practicing and having some examples for the future.

// Basic printting and simple tools

console.log('Hey, this is a text');
console.log('Conca' + 'te' + 'nation');
console.log('The length of my yard is: ' + 'My yard'.length + ' meters.');
console.log('You should not scream!'.toUpperCase());
console.log('Im going to start with the tomatoes'.startsWith('tomatos'));
console.log('  I     need  more     space        , she said'.trim());

console.log(Math.random());
var exchange = 50.46;
console.log('You can keep the exchange. ' + Math.floor(exchange));
console.log(Math.ceil(exchange));
console.log(Number.isInteger(exchange));

// Vars

var varNameHere = 'Var value, it needs "var" for assignment';
let yourAnswer;
yourAnswer = 'Ops, it forgot it';
const Gravity = 'Assuming that gravity value is 10...';

var importantValue = 'magazine';
console.log(`Hey this still is a string printing a ${importantValue}`);
console.log(typeof importantValue);

// Conditionals

var yesValue = 'Yes';
let isThisEmpty = yesValue || true;

// functions

function isItDefault(defaultValue = 'default') {
	if(defaultValue === 'default') {
		return true;
	}
	return false;
}


const pizzaFlavor = function(flavor) {
// OR: const pizzaFlavor = (flavor) => {
	if(flavor === 'cheese') {
		return 'cheese only';
	}
	else if(flavor === 'bacon') {
		return 'bacon, cheese, and creamcheese';
	}
};

console.log(pizzaFlavor('bacon'));

const dolarPrice = value => value * 4.10;

// Scope

// ~Nothing here

// Arrays

const eatableFood = ['cheese','fish','sushi','any japanese dish','bacon'];
console.log(eatableFood.length);
eatableFood.push('Fries'); // appeding element
eatableFood.pop(); // Removing the last one
eatableFood.shift(): // Removes the first one
eatableFood.unshift('Pasta'); // Adds a new element at first position
eatableFood.slice(1,4);
var whereIsMyFishAt = eatableFood.indexOf('fish');


// Loops

//// for

for( var counter = 0; counter < 10; counter++ ) {
	console.log(counter);
}

//// while

var count = 0;
while( count < 5 ) {
	console.log(count);
	count++;
}

//// Do while

var count = 0;
do {
	console.log(count);
	count++;
} while(count < 5);


// Functions as data

const x = value => {
	if( value < 10 ) {
		return 'Hey, its greater then 10, Nice!';
	}
	else {
		return 'Silence.';
	}
}

var hey = x;
console.log(hey());
console.log(hey.name);

// Functions as parameter


const MetersToCentimeters = value => value*100;

const taggedValue = (func, value) => value + ' cm';

taggedValue(MetersToCentimeters, 59,30);


























