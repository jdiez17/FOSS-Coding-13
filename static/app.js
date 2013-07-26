var ctx;
var maze;

function draw_maze(maze, cube_dim) {
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
            ctx.fillRect(x * cube_dim, y * cube_dim, cube_dim, cube_dim);
        }
    }
}

function load_maze(complexity) {
    $.get("/maze/" + complexity, function(data) {
        maze = data['maze'];
        draw_maze(maze, complexity);
    });
}

$(document).ready(function() {
    var canvas = $($("#canvas"))[0];
    console.log(canvas);
    ctx = canvas.getContext("2d");

    load_maze(2);    
});
