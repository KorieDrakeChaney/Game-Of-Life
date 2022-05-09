extends Node2D

export(PackedScene) var Cell;

const CELLSIZE : int = 10;

onready var SCREEN_SIZE = get_viewport_rect().size;

var cell_array = [];
var count : int;
var generation : int = 0;
var play : bool = true;
var color : bool = true;

func _ready():
	create_grid();
	random_grid();
	connect_nodes();

func create_grid(): 
	for x in range(0, SCREEN_SIZE.x / CELLSIZE):
		for y in range(0, SCREEN_SIZE.y / CELLSIZE):
			var cell = Cell.instance();
			cell.isAlive = false;
			cell.position = Vector2(CELLSIZE * x + CELLSIZE / 2, CELLSIZE * y + CELLSIZE / 2);
			cell.pos = Vector2(x, y);
			cell.index = cell_array.size();
			cell_array.append(cell);
			add_child(cell);

func alive_process():
	generation += 1;
	
	if generation % 30 == 0:
		if(count + 1 > cell_array.size() - 1):
			count = 0;
		else:
			count += 1;
	
	for cell in cell_array:
		cell.aliveNeighbors = 0;
		for id in cell.neighbors:
			if cell_array[id].isAlive:
				cell.aliveNeighbors += 1;
		cell.prevLife = cell.isAlive;
	
	for cell in cell_array:
		if cell.aliveNeighbors == 2:
			pass;
		elif cell.aliveNeighbors == 3:
			cell.isAlive = true;
		else:
			cell.isAlive = false;


func connect_nodes():
	var cell_y = SCREEN_SIZE.y / CELLSIZE;
	var cell_x = SCREEN_SIZE.x / CELLSIZE;
	for i in range(0, cell_array.size() - 1):
			# top
			if fmod(i, cell_y) != 0:
				cell_array[i].neighbors.append(cell_array[i - 1].index)
			else: 
				cell_array[i].neighbors.append(cell_array[i + cell_y - 1].index)
			# bottom
			if fmod(i + 1, cell_y) != 0:
				cell_array[i].neighbors.append(cell_array[i + 1].index)
			else:
				cell_array[i].neighbors.append(cell_array[i - cell_y + 1].index)
			# right
			if cell_array[i].pos.x < cell_x - 1:
				cell_array[i].neighbors.append(cell_array[i + cell_y].index)
			else: 
				cell_array[i].neighbors.append(cell_array[i - ((cell_y) * (cell_x - 1))].index)
			#left
			if cell_array[i].pos.x > 0:
				cell_array[i].neighbors.append(cell_array[i - cell_y].index)
			else:
				cell_array[i].neighbors.append(cell_array[i + ((cell_y ) * (cell_x - 1))].index)
				
			
			if fmod(i + 1, cell_y) != 0 and i < (cell_array.size() - cell_y):
				cell_array[i].neighbors.append(cell_array[i + cell_y + 1].index)
			if fmod(i + 1, cell_y) != 0 and i > cell_y:
				cell_array[i].neighbors.append(cell_array[i - cell_y + 1].index)
			if fmod(i, cell_y) != 0 and i < (cell_array.size() - cell_y):
				cell_array[i].neighbors.append(cell_array[i + cell_y - 1].index)
			if fmod(i, cell_y) != 0 and i > cell_y:
				cell_array[i].neighbors.append(cell_array[i - cell_y - 1].index)

func check_box(mousePos : Vector2):
	
	var result = mousePos / CELLSIZE;
	result = Vector2(ceil(result.x) - 1, ceil(result.y) - 1);
	
	for cell in cell_array:
		if result == cell.pos:
			if cell.isAlive:
				cell.isAlive = false;
				cell.modulate = cell_array[count].deadColor;
			else:
				cell.isAlive = true;
				cell.modulate = cell_array[count].aliveColor;
	
func random_grid():
	for cell in cell_array:
		var randNumber = rand_range(0, 1);
		if randNumber > 0.85:
			cell.isAlive = true;
		else:
			cell.isAlive = false;

func clear():
	for cell in cell_array:
		cell.isAlive = false;


func _unhandled_input(event):
	if event is InputEventKey:
		if event.pressed and event.scancode == KEY_ESCAPE:
				get_tree().quit();
		if event.pressed and event.scancode == KEY_R:
				random_grid();
		if event.pressed and event.scancode == KEY_SPACE:
				play = !play;
		if event.pressed and event.scancode == KEY_C:
			color = !color;
		if event.pressed and event.scancode == KEY_V:
			clear();
			
	if event is InputEventMouseButton:
		if event.pressed:
			check_box(get_global_mouse_position());

func _on_Timer_timeout():
	if(play):
		alive_process();
	for cell in cell_array:
		if color:
			if !cell.isAlive:
				cell.modulate = Color(lerp(cell.modulate, cell_array[count].deadColor, 0.1));
			elif !cell.prevLife && cell.isAlive:
				cell.modulate = cell_array[count].aliveColor;
			elif cell.prevLife and cell.isAlive:
				cell.modulate = Color(lerp(cell.modulate, cell_array[count].staticColor, 0.1))
		else:
			if cell.isAlive:
				cell.modulate = Color(0, 0, 0)
			else:
				cell.modulate = Color(1, 1, 1)
