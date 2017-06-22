module.exports = function Route(app, server){
  // get socket.io
  var io = require('socket.io').listen(server);
  app.get('/', function(req, res){
    res.render('index');
  });
  var count = 0;
  // listen to connection from client
  io.sockets.on('connection', function(socket){
    // events for server to listen for
    socket.on("epic_click", function(data){
      count++;
    io.emit("new_count", {response: count});
    });
    socket.on("reset_count", function(data){
      count = 0;
    io.emit("new_count", {response: count});
    });
  });
};
