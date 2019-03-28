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




















