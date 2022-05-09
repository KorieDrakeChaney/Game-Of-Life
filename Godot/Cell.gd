extends MeshInstance2D

enum State {ALIVE, DEAD}

var isAlive : bool = false;
var aliveNeighbors : int;
var pos : Vector2;
var deadColor : Color;
var aliveColor : Color;
var staticColor: Color;
var color : Color = Color(1, 1, 1);
var index : int;
var prevLife : bool;

var neighbors = [];

func _ready():
	randomize()
	deadColor = Color(rand_range(0.1, 0.5), rand_range(0.1, 0.5), rand_range(0.1, 0.5), 1);
	staticColor = Color(randf(), randf(), randf());
	aliveColor = Color(randf(), randf(), randf(), 0.875);
	scale = Vector2(9.0, 9.0)
