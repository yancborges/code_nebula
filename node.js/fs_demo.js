const fs = require('fs');
const path = require('path');

//fs.mkdir(path.join(__dirname,'/test'), {}, err => {
//	if(err) throw err;
//	console.log('Folder created');
//});

fs.writeFile(path.join(__dirname,'/test','hi.txt'), 'niiice', err => {
	if(err) throw err;
	console.log('File created');

	fs.appendFile(path.join(__dirname,'/test','hi.txt'), 'wuiehfuiwe', err => {
	if(err) throw err;
	console.log('File created');
	});
});

fs.readFile(path.join(__dirname, '/test', 'hi.txt'), 'utf8', (err,data) => {
	if(err) throw err;
	console.log(data);
});

