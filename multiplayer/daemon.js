var io = require('socket.io').listen(8842),
    redis = require('redis-client');

io.sockets.on('connection', function(socket) {
    console.log(socket);

    socket.emit('asdf', {bru: 'bra'});
});
