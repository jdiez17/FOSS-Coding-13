var ctx;
var maze;
var player_coords = [-1, -1];
var x_max = y_max = 300;
var socket;
var level;

var minutes, seconds;
var seconds_elapsed = 1;

function get_fill_style(num) {
    colors = {
        3: 'red',
        4: 'blue',
        5: 'green'
    }

    return colors[num];
}

function max_time() {
    // Level    Time
    // 30       5 
    // -        -
    // n        x 
    // 
    // 30x = 5n
    // x = 5n/30
    return Math.round((5 * level) / 30)
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
        $("#timer").html(max_time())
        minutes = max_time();
        seconds = 0;
        countdown();
    });
}

function countdown() {
    seconds_elapsed++;
    if(seconds == 0) {
        if(minutes == 0) {
	    alert("Time is up");
            return;
        } else {
            minutes--;
            seconds = 59;
        }
    }
    if(minutes > 0) {
        var minute_text = minutes;
    } else {
        var minute_text = '';
    }
    $("#timer").html(minute_text + ':' + seconds);
    seconds--;

    setTimeout(countdown, 1000);
}

function valid_move(x, y) {
    if(x_max >= x && y_max >= y && x >= 0 && y >= 0) {
        if(maze[y][x] == 0 || maze[y][x] == 2)
            return true;
    }
    return false;
}

function win() {
    console.log("win");
    seconds_max = max_time() * 60;
    score = (seconds_max - seconds_elapsed) * 100;

    alert("Your score is " + score);
    minutes = seconds = 0;

    $.post('/maze/', {'fow': fov != -1 ? 'on' : 'false', 'tron': tron ? 'on' : 'off', 'level': --level, 'players': 1}, function(data) {
        console.log(data);
        location.href = data;
    });
}

function keyhandler(ev) {
    if(minutes == 0 && seconds == 0) return;
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
        win();
    }
    if(valid_move(x, y)) {
        if(!tron) {
            maze[player_coords[1]][player_coords[0]] = 0;
        }
        maze[y][x] = player;
        player_coords = [x, y];
        socket.emit('MOVE', {maze: maze});
    }
}

$(document).ready(function() {
    var canvas = $($("#canvas"))[0];
    ctx = canvas.getContext("2d");


    socket = io.connect('http://s.jdiez.me:8842');
    socket.emit('HELO', level);
    socket.on('PLYR', function(s_player) { 
        player = s_player 
        load_maze(level)
    });
    socket.on('MOVE', function(data) {
        maze = data['maze'];
        draw_maze();
    });

    $(document).keypress(keyhandler);
});
