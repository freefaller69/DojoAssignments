module.exports = function Route(app, server){
  // get socket.io
  var io = require('socket.io').listen(server);
  app.get('/', function(req, res){
    res.render('index');
  });
  var chat_history = [];
  //listen to connection from client
  io.sockets.on('connection', function(socket){
    console.log('user connected ' + socket.id);
    // events for server to listen for
    socket.on('disconnect', function(){
    console.log('user disconnected ' + socket.id);
    });
    socket.on('send_text', function(message){
      chat_history.push(message);
      io.emit('new_message', message );
    });

    socket.on("userJoin", function(){
      socket.emit("new_user", chat_history);
    });

  });
};
