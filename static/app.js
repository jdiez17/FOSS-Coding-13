var ctx;
var maze;
var player_coords = [-1, -1];
var x_max = y_max = 300;
var socket;

function get_fill_style(num) {
    return "red";
}

function draw_maze() {
    ctx.clearRect(0, 0, 300, 300);
    if(fov != -1 && player_coords[0] != -1) {
        ctx.restore();
        ctx.save();
        ctx.beginPath();
        ctx.arc(player_coords[0] * level, player_coords[1] * level, fov, 0, 2 * Math.PI, false);
        ctx.clip();
    } else {
        ctx.save();
    }
    for(y = 0; y < maze.length; y++) {
        for(x = 0; x < maze[y].length; x++) {
            var num = maze[y][x];
            switch(num) {
                case 0:
                    ctx.fillStyle = "white";
                    break;
                case 1:
                    ctx.fillStyle = "black";
                    break;
                case 2:
                    ctx.fillStyle = "yellow";
                    break;
                default:
                    ctx.fillStyle = get_fill_style(num);
                    if(num == player && player_coords[0] == -1) {
                        player_coords = [x, y];
                    }
                    break;
            }
            ctx.fillRect(x * level, y * level, level, level);
        }
    }

}

function load_maze(req) {
    $.get("/maze/data/" + req, function(data) {
        maze = data['maze'];
        level = data['level'];
        draw_maze();
    });
}

function valid_move(x, y) {
    if(x_max >= x && y_max >= y && x >= 0 && y >= 0) {
        if(maze[y][x] == 0 || maze[y][x] == 2)
            return true;
    }
    return false;
}

function keyhandler(ev) {
    var c = String.fromCharCode(ev.which);
    var dx, dy;
    if(c == "w") {
        dx = 0;
        dy = -1;
    }
    if(c == "a") {
        dx = -1;
        dy = 0;
    }
    if(c == "s") {
        dx = 0;
        dy = 1;
    }
    if(c == "d") {
        dx = 1;
        dy = 0;
    }
    
    var x = player_coords[0] + dx;
    var y = player_coords[1] + dy;
    if(maze[y][x] == 2) {
        alert("You win");
    }
    if(valid_move(x, y)) {
        if(!tron) {
            maze[player_coords[1]][player_coords[0]] = 0;
        }
        maze[y][x] = player;
        player_coords = [x, y];
        draw_maze();

        socket.emit('MOVE', {maze: maze});
    }
}

$(document).ready(function() {
    var canvas = $($("#canvas"))[0];
    ctx = canvas.getContext("2d");


    socket = io.connect('http://s.jdiez.me:8842');
    socket.emit('HELO', level);
    socket.on('MOVE', function(data) {
        console.log('Got updated info');
        maze = data['maze'];
        draw_maze();
    });

    load_maze(level);
    $(document).keypress(keyhandler);
});
