//console.log('Hi');

//const Person = require('./person');

//const person1 = new Person('Mill', 18);
//person1.greeting();

const http = require('http');
const path = require('path');
const fs = require('fs');

const server = http.createServer((req, res) => {
	if(req.url === '/about') {
		fs.readFile(path.join(__dirname, 'about.html'), (err, content) => {
			if(err) throw err;
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.end(content);
		})
	}

	if(req.url === '/api/users') {
		const users = [
		{ name: 'A', age: 30},
		{ name: 'B', age: 20},
		{ name: 'C', age: 3}
		];
		res.writeHead(200, {'Content-Type': 'application/json'});
		res.end(JSON.stringify(users));
	}
})

const PORT = process.env.PORT || 5000;
server.listen(PORT, () => console.log(`Running at ${PORT}`));