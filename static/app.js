var ctx;
var maze;

function draw_maze(maze) {
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
            }
            ctx.fillRect(x * 10, y * 10, 10, 10);
        }
    }
}

function load_maze(id) {
    $.get("/maze/" + id, function(data) {
        maze = data['maze'];
        draw_maze(maze);
    });
}

$(document).ready(function() {
    var canvas = $($("#canvas"))[0];
    console.log(canvas);
    ctx = canvas.getContext("2d");

    load_maze('asdf');    
});
