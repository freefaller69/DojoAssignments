var express = require("express");
var path = require("path");
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.urlencoded());

app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
var port = process.env.PORT || 8000;
var server = app.listen(port, function(){
  console.log('listening on port ' + port);
});

var route = require('./routes/index.js')(app, server);
