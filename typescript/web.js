var express = require('express');
var app = express();
app.get('/', function (req, res) {
    res.send('Hi dudes');
});
app.listen(3000, function () {
    console.log('I am all ears');
});
