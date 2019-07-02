const path = require('path');

console.log(path.extname(__filename));
console.log(path.parse(__filename));
console.log(path.join(__dirname,'test','hello.html'));