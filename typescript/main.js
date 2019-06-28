"use strict";
exports.__esModule = true;
var message = "Hi";
console.log(message);
var isFirstTime = true;
var numerOfTimes = 0;
var name = 'Hajimaru';
var sentence = "My name is " + name;
console.log(sentence);
var n = null;
var u = undefined;
var list1 = [1, 2, 3];
var list2 = [1, 2, 3];
var person1 = ['Dad', 56];
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
var c = Color.Green;
console.log(c);
var randomValue = 10;
randomValue = true;
randomValue = 'meeh';
var isThatAVar = 10;
var mutant;
function add(num1, num2, number3) {
    if (number3 === void 0) { number3 = 5; }
    return num1 + num2;
}
function fullname(person) {
    console.log(person.firstName + " " + person.lastName);
}
var p = {
    firstName: 'Meenkeo',
    lastName: 'mee'
};
fullname(p);
var Employee = /** @class */ (function () {
    function Employee(name) {
        this.employeeName = name;
    }
    Employee.prototype.greet = function () {
        console.log("Morning mr." + this.employeeName);
    };
    return Employee;
}());
var employee1 = new Employee('Ismael');
console.log(employee1.employeeName);
employee1.greet();
