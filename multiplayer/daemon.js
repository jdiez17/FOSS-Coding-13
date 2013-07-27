var io = require('socket.io').listen(8842),
    redis = require('redis').createClient();

var broadcast_groups = {};
var players = {};

io.sockets.on('connection', function(socket) {
    socket.on('HELO', function(id) { 
        if(id in broadcast_groups) {
            broadcast_groups[id].push(socket);
        } else {
            broadcast_groups[id] = [socket];
        }

        socket.bgroup = id;

        console.log(players);
        if(id in players) {
            plyr = ++players[id];
        } else {
            players[id] = 3;
            plyr = 3;
        }
        socket.emit('PLYR', plyr);
    });
    socket.on('MOVE', function(data) {
        key = 'maze.' + socket.bgroup + '.config';
        redis.hset(key, 'maze', JSON.stringify(data['maze']));
        if(socket.bgroup in broadcast_groups) {
            for(i = 0; i < broadcast_groups[socket.bgroup].length; i++) {
                broadcast_groups[socket.bgroup][i].emit('MOVE', data);
            }
        }
    });
});
