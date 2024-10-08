from gasp import *

GRID_SIZE = 30
MARGIN = GRID_SIZE

BACKGROUND_COLOR = color.BLACK
WALL_COLOR = "99E5E5"

class Maze:
    def __init__(self):
        self.have_window = False
        self.game_over = False
        self.get_level()

    def get_level(self):
        f = open("map.dat")
        self.the_layout = []
        for line in f.readlines():
            self.the_layout.append(line.rstrip())


    def finished(self):
        return self.game_over
    
    def play(self):
        answered = input('Are we done yet? ') 
        if answered == 'yes':
            self.game_over = True
        else:     
            print("I'm playing")
    
    def done(self):
        print("I'm done")
        pass


the_maze = Maze()

while not the_maze.finished():
    the_maze.play()

the_maze.done()


