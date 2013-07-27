var ctx;
var maze;
var player_coords;
var x_max = y_max = 300;

function get_fill_style(num) {
    return "red";
}

function draw_maze() {
    ctx.clearRect(0, 0, 300, 300);
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
                    if(num == player) {
                        player_coords = [x, y];
                    }
                    break;
            }
            ctx.fillRect(x * level, y * level, level, level);
        }
    }
}

function load_maze(req) {
    $.get("/maze/" + req, function(data) {
        maze = data['maze'];
        level = req;
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
        maze[player_coords[1]][player_coords[0]] = 0;
        maze[y][x] = player;
        draw_maze();
    }

}

$(document).ready(function() {
    var canvas = $($("#canvas"))[0];
    console.log(canvas);
    ctx = canvas.getContext("2d");

    load_maze(level);
    $(document).keypress(keyhandler);
});
