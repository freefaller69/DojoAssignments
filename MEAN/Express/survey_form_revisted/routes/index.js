module.exports = function Route(app, server){
	// get the socket.io module
	var io = require('socket.io').listen(server);
	app.get('/', function(req, res) {
		res.render("index");
	});
	//listen to connection from the client side
	io.sockets.on('connection', function (socket){
		//server listens for "posting_form" event
	 	socket.on("posting_form", function (data){
	 		var random_number = Math.floor((Math.random() * 1000) + 1);
		  //emit the data to the client
		  socket.emit('updated_message', {response: data});
			socket.emit('random_number', {response: random_number});
		});
	});
};
