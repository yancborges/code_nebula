const http = require('http');

http.createServer((req, res) => {
	res.write('Hi, this is actually a web server!');
	res.end();
}).listen(5000, () => console.log('Server running...'));