var io = require('socket.io').listen(8842),
    redis = require('redis-client');

var broadcast_groups = {}

io.sockets.on('connection', function(socket) {
    socket.on('HELO', function(id) { 
        if(id in broadcast_groups) {
            broadcast_groups[id].push(socket);
        } else {
            broadcast_groups[id] = [socket];
        }

        socket.bgroup = id;
    });
    socket.on('MOVE', function(data) {
        if(socket.bgroup in broadcast_groups) {
            for(i = 0; i < broadcast_groups[socket.bgroup].length; i++) {
                console.log('broadcasting');
                broadcast_groups[socket.bgroup][i].emit('MOVE', data);
            }
        }
    });
});
