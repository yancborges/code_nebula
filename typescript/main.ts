export {};

let message = "Hi";
console.log(message);

let isFirstTime: boolean = true;
let numerOfTimes: number = 0;
let name: string = 'Hajimaru';

let sentence: string = `My name is ${name}`;
console.log(sentence);

let n: null = null;
let u: undefined = undefined;

let list1: number[] = [1,2,3];
let list2: Array<number> = [1,2,3];

let person1: [string, number] = ['Dad', 56];

enum Color {Red, Green, Blue};
let c: Color = Color.Green;

console.log(c);

let randomValue: any = 10;
randomValue = true;
randomValue = 'meeh';

let isThatAVar: unknown = 10;

let mutant: number | boolean;


function add(num1: number, num2?: number, number3: number = 5): number {
	return num1 + num2;
}


interface Person {
	firstName: string;
	lastName: string;
}

function fullname(person: Person) {
	console.log(`${person.firstName} ${person.lastName}`);
}

let p = {
	firstName: 'Meenkeo',
	lastName: 'mee'
}

fullname(p);



class Employee {
	public employeeName: string;
	protected document: number;
	// and private for total restriction

	constructor(name: string, document: number) {
		this.employeeName = name;
		this.document = document;
	}

	greet() {
		console.log(`Morning mr.${this.employeeName}`);
	}
}

let employee1 = new Employee('Ismael',156548);
console.log(employee1.employeeName);
employee1.greet();

class Manager extends Employee {
	constructor(managerName: string) {
		super(managerName,489562);
	}

	command() {
		console.log(`WHOS IN CHARGE HERE HUH?`);
	}
}

let m1 = new Manager('Jinja');
m1.greet();
m1.command();
