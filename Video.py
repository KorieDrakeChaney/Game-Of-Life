from manim import *
import random
import math

class Title(Tex):
    def __init__(self, title, **kwargs):
        super().__init__(title, **kwargs)
        self.to_corner(UP*2)

class ThreeDCell(Cube):
    isAlive = False
    aliveNeighbors = 0
    index = 0
    neighbors = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.isAlive = False
        self.aliveNeighbors = 0
        self.index : int
        self.prevLife = False
        self.neighbors = []

class ThreeDGrid(VGroup):
    width = 5
    height = 5
    depth = 5
    cells = []
    def __init__(self, width = 5, height = 5, depth = 5, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        self.depth = depth
        for x in range(self.width):
            for y in range(self.height, 0, -1):
                for z in range(self.depth):
                    s = ThreeDCell(stroke_color=WHITE, width =1 / (width / 5), height = 1 / (height / 5), depth=1 / (depth / 5))
                    s.move_to([x / (width / 5), y / (height / 5), z / (depth / 5)])
                    s.index = len(self.cells)
                    self.cells.append(s)
                    self.add(s)

        self.center()
        self.connect_nodes()
        self.update_grid()

class Cell(Rectangle):
    isAlive = False
    aliveNeighbors = 0
    index = 0
    neighbors = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.isAlive = False
        self.aliveNeighbors = 0
        self.index : int
        self.prevLife = False
        self.neighbors = []

class Grid(VGroup):
    width = 5
    height = 5
    cells = []
    def __init__(self, width = 5, height = 5, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        for x in range(self.width):
            for y in range(self.height, 0, -1):
                s = Cell(stroke_color=WHITE, width =1 / (width / 5), height = 1 / (height / 5))
                s.move_to([x / (width / 5), y / (height / 5), 0])
                s.index = len(self.cells)
                self.cells.append(s)
                self.add(s)

        self.center()
        self.connect_nodes()
        self.update_grid()

    def connect_nodes(self):
        for i in range(0, len(self.cells)):
                # top
                if i % self.height != 0:
                    self.cells[i].neighbors.append(self.cells[i - 1].index)
                else: 
                    self.cells[i].neighbors.append(self.cells[i + self.height - 1].index)
                # bottom
                if (i + 1) % self.height != 0:
                    self.cells[i].neighbors.append(self.cells[i + 1].index)
                else:
                    self.cells[i].neighbors.append(self.cells[i - self.height - 1].index)
                # right
                if i < (len(self.cells) - self.height):
                    self.cells[i].neighbors.append(self.cells[i + self.height].index)
                else: 
                    self.cells[i].neighbors.append(self.cells[len(self.cells) - i].index)
                #left
                if i > self.height:
                    self.cells[i].neighbors.append(self.cells[i - self.height].index)
                if (i + 1) % self.height != 0 and i < (len(self.cells) - self.height):
                    self.cells[i].neighbors.append(self.cells[i + self.height + 1].index)
                if (i + 1) % self.height != 0 and i > self.height:
                    self.cells[i].neighbors.append(self.cells[i - self.height + 1].index)
                if  i % self.height != 0 and i < (len(self.cells) - self.height):
                    self.cells[i].neighbors.append(self.cells[i + self.height - 1].index)
                if  i % self.height != 0 and i > self.height:
                    self.cells[i].neighbors.append(self.cells[i - self.height - 1].index)

    def randomize(self):
        for cell in self.cells:
            randNumber = random.randint(0, 100)
            if randNumber > 65:
                cell.isAlive = True;
                cell.set_fill(BLUE_A, opacity=1.0)
            else:
                cell.isAlive = False;
                cell.set_fill(BLUE_D, opacity=0.5)
            
    def clear(self):
        for cell in self.cells:
            cell.isAlive = False


    @staticmethod
    def still_grid(type):
        match type:
            case "block":
                grid = Grid(width = 4, height = 4)
                alive = [
                    5, 6, 9, 10
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "beehive":
                grid = Grid(width = 6, height = 5)
                alive = [
                    7, 11, 13, 16, 18, 22
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "loaf":
                grid = Grid(width = 6, height = 6)
                alive = [
                    8, 13, 15, 19, 22, 26, 27
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "boat":
                grid = Grid(width = 5, height = 5)
                alive = [
                    6, 7, 11, 13, 17
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "tub":
                grid = Grid(width = 5, height = 5)
                alive = [
                    7, 11, 13, 17
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
    
    @staticmethod   
    def oscillator_grid(type):
        match type:
            case "blinker":
                grid = Grid(width = 5, height = 5)
                alive = [
                    7, 12, 17
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "toad":
                grid = Grid(width = 6, height = 6)
                alive = [
                    9, 14, 15, 20, 21, 26
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "beacon":
                grid = Grid(width = 6, height = 6)
                alive = [
                    7, 8, 13, 22, 27, 28
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "pulsar":
                grid = Grid(width = 17, height = 17)
                alive = [
                    38, 39, 45, 46, 
                    56, 57, 61, 62, 
                    70, 73, 75, 77, 79, 82, 
                    87, 88, 89, 91, 92, 94, 95, 97, 98, 99, 
                    105, 107, 109, 111, 113, 115, 
                    123, 124, 125, 129, 130, 131, 

                    157, 158, 159, 163, 164, 165, 
                    173, 175, 177, 179, 181, 183, 
                    189, 190, 191, 193, 194, 196, 197, 199, 200, 201, 
                    206, 209, 211, 213, 215, 218, 
                    226, 227, 231, 232, 
                    242, 243, 249, 250


                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "pentadecathlon":
                grid = Grid(width = 11, height = 18)
                alive = [
                    58, 59, 66, 67, 75, 78, 83, 86, 
                    93, 96, 101, 104, 111, 114, 119, 122, 
                    130, 131, 138, 139
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid

    @staticmethod
    def spaceship_grid(type):
        match type:
            case "glider":
                grid = Grid(width = 12, height = 12)
                alive = [
                    9, 10, 13, 14
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "lightweight":
                grid = Grid(width = 20, height = 20)
                alive = [
                    9, 10, 13, 14
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "middleweight":
                grid = Grid(width = 22, height = 22)
                alive = [
                    9, 10, 13, 14
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid
            case "heavyweight":
                grid = Grid(width = 24, height = 24)
                alive = [
                    9, 10, 13, 14
                ]
                for id in alive:
                    grid.cells[id].isAlive = True
                    grid.cells[id].set_fill(BLUE_A, opacity=1.0)
                return grid

    def update_grid(self):
        
        for cell in self.cells:
            cell.aliveNeighbors = 0
            for id in cell.neighbors:
                if self.cells[id].isAlive:
                    cell.aliveNeighbors += 1
        for cell in self.cells:
            if cell.aliveNeighbors == 2:
                pass
            elif cell.aliveNeighbors == 3:
                cell.isAlive = True
            else:
                cell.isAlive = False

            if not cell.isAlive:
                cell.set_fill(BLUE_D, opacity=0.5)
            elif not cell.prevLife and cell.isAlive:
                cell.set_fill(BLUE_A, opacity=1.0)


class Intro(Scene):
    def construct(self):
        background = Square()
        background.set_fill(GREY_E, opacity=0.75)
        background.scale(10)
        self.add(background)
        START = (-3,2.5,0)
        END =   (3,2.5,0)
        block_grid = Grid.oscillator_grid("pulsar")
        block_grid.set_fill(BLUE_A, opacity=0.1)
        block_grid.update_grid()
        self.play(*[FadeIn(_) for _ in block_grid])
        for i in range(4):
            block_grid.update_grid()
            self.wait(0.5)
        block_grid.update_grid()
        self.play(block_grid.animate.shift(RIGHT * 4 + DOWN * 1.5).scale(0.75))
        block_grid.update_grid()


class Grid3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=0 * DEGREES, distance=20)
        grid = ThreeDGrid()
        self.add(grid)
        
class RuleExplanation(Scene):
    def construct(self):
        background = Square()
        background.set_fill(GREY_E, opacity=0.75)
        background.scale(10)
        viewport = Rectangle(stroke_color=BLACK, height = 5.2, width = 5.2)
        viewport.set_fill(BLACK, opacity=1) 
        viewport.move_to([0, -0.5, 0])
        title = Title("Rules");
        self.add(background, title)
        START = (-1,2.5,0)
        END =   (1,2.5,0)
        line = Line(START,END, stroke_color=YELLOW_C);
        line.set_fill(BLUE_A, opacity=1) 
        grid = Grid()
        self.play(Create(line), FadeIn(viewport),grid.animate.set_fill(BLUE_D, opacity=0.5))
        self.play(grid.animate.scale(0.75), viewport.animate.scale(0.75))
        t1 = VGroup(grid.cells[11], grid.cells[13])
        t2 = VGroup(grid.cells[7], grid.cells[17])
        self.play(grid.animate.shift(LEFT * 2), viewport.animate.shift(LEFT * 2))
        rule_one = Tex(r"Any live cell with " , r"two ", r"or ", r"three ",  r"live ", r"neighbours ", r"\\ survives", font_size=24)
        rule_one.move_to([3, 1.15, 0])
        rule_two = Tex(r'Any dead cell with ', r'three ', r'live ' , r'neighbours \\ becomes a live cell', font_size=24)
        rule_two.move_to([3, -0.4, 0])
        rule_three = Tex(r'All other live cells die in the next generation.', r'\\ Similarly, all other dead cells ' , r'stay dead', font_size=24)
        rule_three.move_to([3, -2.15, 0])
        self.wait(1)
        self.play(Write(rule_one))
        self.play(Write(rule_two))
        self.play(Write(rule_three))
        self.play(Circumscribe(rule_one))
        self.play(FadeOut(rule_two,shift=DOWN), FadeOut(rule_three,shift=DOWN), 
                rule_one.animate.shift(DOWN * 2), grid.animate.shift(ORIGIN))
        rule_two.next_to(rule_one, ORIGIN)
        rule_three.next_to(rule_one, ORIGIN)
        vals = np.arange(1,10).reshape(3,3)

        generation = Text('Generation :').scale(0.7)
        generation.move_to([-2.25, -3, 0])
        decimal = DecimalNumber(0, num_decimal_places=0, include_sign=False, unit=None)
        tracker = ValueTracker(1)   
        decimal.add_updater(lambda d: d.set_value(tracker.get_value()))
        decimal.next_to(generation, RIGHT)
        self.play(grid.cells[12].animate.set_fill(BLUE_A, opacity=1), Write(generation), Write(decimal), rule_one[1].animate.set_fill(YELLOW_C, opacity=1.0), rule_one[4].animate.set_fill(GREEN_C, opacity=1.0), rule_one[3].animate.set_fill(YELLOW_C, opacity=1.0), rule_one[5].animate.set_fill(YELLOW_C, opacity=1.0))
        self.wait(1)
        
        number_group_one = VGroup()
        neighbors_one = [6, 11, 16, 7, 17, 8, 13, 18]
        for i, c in enumerate(neighbors_one, 1):
            d = DecimalNumber(i, num_decimal_places=0, include_sign=False, unit=None)
            d.next_to(grid.cells[c], ORIGIN)
            number_group_one.add(d)
        self.play(Create(number_group_one))

        # Rule 1
        self.play(grid.cells[6].animate.set_fill(BLUE_A, opacity=1), 
        grid.cells[17].animate.set_fill(BLUE_A, opacity=1))
        self.play(Circumscribe(grid.cells[6], run_time=2, fade_out=True, buff=0), Circumscribe(grid.cells[17], run_time=2, fade_out=True, buff=0))
        self.wait(1)
        b0 = [-0.175, 0.33, 0]
        b1 = [-0.1, 0, 0]
        b2 = [0.5, 0.65, 0]

        self.play(grid.cells[12].animate.set_fill(GREEN_C, opacity=1), FadeOut(rule_one, shift=UP*1.5),  FadeIn(rule_two, shift=UP*1.5), FadeOut(number_group_one, shift=ORIGIN), Circumscribe(grid.cells[11], run_time=2, buff=0, color=BLACK))
        number_group_two = VGroup()
        neighbors_two = [5, 10, 15, 6, 16, 7, 12, 17]
        for i, c in enumerate(neighbors_two, 1):
            d = DecimalNumber(i, num_decimal_places=0, include_sign=False, unit=None)
            d.next_to(grid.cells[c], ORIGIN)
            number_group_two.add(d)
        self.play(Create(number_group_two))
        self.play(Circumscribe(grid.cells[6], run_time=2, fade_out=True , buff=0), Circumscribe(grid.cells[17], run_time=2, fade_out=True, buff=0),  Circumscribe(grid.cells[12], run_time=2, fade_out=True, buff=0))
        self.wait(1)
        self.play(grid.cells[11].animate.set_fill(GREEN_C, opacity=0.5), FadeOut(rule_two, shift=UP*1.5),  FadeIn(rule_three, shift=UP*1.5), FadeOut(number_group_two, shift=ORIGIN), 
        Circumscribe(grid.cells[17], run_time=2, buff=0, color=BLACK))
        number_group_three = VGroup()
        neighbors_three = [11, 16, 21, 12, 22, 13, 18, 23]
        for i, c in enumerate(neighbors_three, 1):
            d = DecimalNumber(i, num_decimal_places=0, include_sign=False, unit=None)
            d.next_to(grid.cells[c], ORIGIN)
            number_group_three.add(d)
        self.play(Create(number_group_three))
        self.play(Circumscribe(grid.cells[12], run_time=2, fade_out=True, buff=0))
        self.play(grid.cells[17].animate.set_fill(RED, opacity=1.0), FadeOut(number_group_three, shift=ORIGIN),  rule_three[0].animate.set_fill(GREY_E, opacity=1), rule_three[2].animate.set_fill(RED, opacity=1))
        self.wait(1)
        everything_group = VGroup()
        everything_else = [0, 5, 10, 15, 20, 1, 6, 16, 21, 2, 7, 22, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24]
        for c in everything_else:
            if c == 6: 
                self.play(grid.cells[c].animate.set_fill(RED, opacity=1), run_time=0.1)
            else:
                self.play(grid.cells[c].animate.set_fill(RED, opacity=0.5), run_time=0.1)
            everything_group.add(grid.cells[c])
        self.wait(1)
        tracker.set_value(2)
        self.play(FadeOut(rule_three, shift=UP*1.5), grid.cells[12].animate.set_fill(BLUE_A, opacity=1), grid.cells[11].animate.set_fill(BLUE_A, opacity=1), everything_group.animate.set_fill(BLUE_D, opacity=0.5), grid.cells[17].animate.set_fill(BLUE_D, opacity=0.5))

class Thumbnail(Scene):
    def construct(self):
        background = Square()
        background.set_fill(GREY_E, opacity=0.75)
        background.scale(10)
        viewport = Rectangle(stroke_color=BLACK, height = 5.2, width = 5.2)
        viewport.set_fill(BLACK, opacity=1) 
        viewport.move_to([0, -0.25, 0])
        title = Tex(r"Conway's Game of Life")
        title.to_corner(UP * 1.5)
        title.set_fill(WHITE, opacity=1)
        START = (-3, 3.5,0)
        END =   (3, 3.5,0)
        line = Line(START,END, stroke_color=YELLOW_C);
        line.set_fill(BLUE_A, opacity=1) 
        line.next_to(title, DOWN * 0.5)
        self.add(background, title, line)
        grid= Grid.oscillator_grid("pulsar")
        generation = Text('Generation :').scale(0.7)
        generation.move_to([-0.25, -3.25, 0])
        decimal = DecimalNumber(1, num_decimal_places=0, include_sign=False, unit=None)
        decimal.next_to(generation, RIGHT)
        self.add(grid, generation, decimal)

