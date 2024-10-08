# Importing modules
from gasp import *
from random import randint
from gasp.utils import read_yesorno


# Class that runs everything
class RunGame:
    # Defining key variables    
    LEFT = "4"
    RIGHT = "6"
    UP = "8"
    DOWN = "2"
    UPRIGHT = "9"
    UPLEFT = "7"
    DOWNRIGHT = "3"
    DOWNLEFT = "1"
    TELEPORT = "5"
    TOP = 46
    BOTTOM = 0
    LEFT_BOARDER = 1
    RIGHT_BOARDER = 62
    # Used to make sure the player hits the correct keys in move player
    INPUT_LIST = ["4", "6", "8", "2", "9", "7", "3", "1", "5"]
    # Variable that is used to prevent robots from spawning on each other
    robot_check = []
    robot_check2 = []
    teleport_count = 0

    # Generates player and robots on the screen
    def __init__(self):
        numbot = 0
        
        # Makes sure the player inputs a number and that it is higher than or equal to 2
        while numbot < 2:
            try:
                numbot = int(input("How many robots would you like to play against (Min 2 Robots)? "))
            except:
                numbot = int(input(f"Please enter a number.\nHow many robots would you like to play against? (Min 2 Robots) "))
        
        RunGame.teleport_count = numbot
        begin_graphics()
        self.finished = False
        self.robots = [Robot() for i in range(numbot)]
        robot_check2 = self.robots
        self.player = Player()
        self.junk = []

    # Calls the moving functions for player and robot. It will soon also check for robot on robot collisions and if all the robots are gone.
    def next_move(self):
        self.check_collisions()

        if self.finished == False:
            self.player.move()

            for bot in self.robots:
                bot.move(self.player)

    # Checks to see if A: Robot has hit the player, B: Robot has hit a Robot, or C: Robot has hit Junk
    def check_collisions(self):
        # Creates temporary variable and clears the Robots list
        alive_robots = self.robots
        self.robots = []
        
        # Main loop for all checking
        for bot in alive_robots:
            # Checks if a Robot has hit the Player
            if bot.x == self.player.x and bot.y == self.player.y:
                self.finished = True
                Text("Game Over", (320, 240), size=100)
                sleep(3)
            
            # Checks if a Robot has hit another Robot
            for thing in alive_robots:
                if bot == thing:
                    continue
                if bot.x == thing.x and bot.y == thing.y:
                    self.junk.append(bot)
                    remove_from_screen(bot.shape)
                    bot.shape = Box((10*bot.x, 10*bot.y), 10, 10, filled=True)
            
            # Checks if a Robot has hit Junk
            for thing in self.junk:
                if bot.x == thing.x and bot.y == thing.y and (bot in self.junk) == False:
                    self.junk.append(bot)
                    remove_from_screen(bot.shape)
            
            # Adds any surviving Robot back to the Robots list
            if (bot in self.junk) == False and (bot in self.robots) == False:
                self.robots.append(bot)
        
        # Checks if there are no robots left alive
        if len(self.robots) == 0:
            self.finished = True
            Text("You Win!", (320, 240), size=100)
            sleep(3)

    # Closes graphic window
    def over(self):
        end_graphics()


# Defines all player related functions
class Player:
    # Places player
    def __init__(self):
        self.safely_place()

    # Function to generate random coordinates for x and y
    def place(self):
        self.x = randint(RunGame.LEFT_BOARDER, RunGame.RIGHT_BOARDER)
        self.y = randint(RunGame.BOTTOM, RunGame.TOP)
    
    # Checks if the player has collided with something
    def collided(self, thing):
        for item in thing:
            if self.x == item.x and self.y == item.y:
                return(True)
            else:
                return(False)

    # Makes sure the player doesn't spawn on a robot
    def safely_place(self):
        self.place()

        while self.collided(RunGame.robot_check2):
            self.place()

        self.shape = Circle((10*self.x, 10*self.y), 5, filled=True)

    # Function for the teleportation ability
    def teleport(self):
        # Doesn't let the player teleport if they are "out" of teleports
        if RunGame.teleport_count > 0:
            remove_from_screen(self.shape)
            self.safely_place()
            RunGame.teleport_count -= 1

    # Function for moving the player
    def move(self):
        key = update_when("key_pressed")

        while key not in RunGame.INPUT_LIST:
            key = update_when("key_pressed")

        while key == RunGame.TELEPORT:
            self.teleport()
            key = update_when("key_pressed")

            while key not in RunGame.INPUT_LIST:
                key = update_when("key_pressed")

        if key == RunGame.UP and self.y < RunGame.TOP:
            self.y += 1
        elif key == RunGame.RIGHT and self.x < RunGame.RIGHT_BOARDER:
            self.x += 1
        elif key == RunGame.DOWN and self.y > RunGame.BOTTOM:
            self.y -= 1
        elif key == RunGame.LEFT and self.x > RunGame.LEFT_BOARDER:
            self.x -= 1
        elif key == RunGame.UPRIGHT:
            if self.x < RunGame.RIGHT_BOARDER:
                self.x += 1
            if self.y < RunGame.TOP:
                self.y += 1
        elif key == RunGame.DOWNRIGHT:
            if self.x < RunGame.RIGHT_BOARDER:
                self.x += 1
            if self.y > RunGame.BOTTOM:
                self.y -= 1
        elif key == RunGame.DOWNLEFT:
            if self.x > RunGame.LEFT_BOARDER:
                self.x -= 1
            if self.y > RunGame.BOTTOM:
                self.y -= 1
        elif key == RunGame.UPLEFT:
            if self.x > RunGame.LEFT_BOARDER:
                self.x -= 1
            if self.y < RunGame.TOP:
                self.y += 1

        move_to(self.shape, (10*self.x, 10*self.y))


# Defines all robot related functions
class Robot:
    # Places a robot
    def __init__(self):
        self.place()

    # Checks if the robot has collided with something
    def collided(self, thing):
        for item in thing:
            if self.x == item[0] and self.y == item[1]:
                return(True)
            else:
                return(False)

    # Defines where to place robot
    def place(self):
        self.x = randint(RunGame.LEFT_BOARDER, RunGame.RIGHT_BOARDER)
        self.y = randint(RunGame.BOTTOM, RunGame.TOP)
        self.coords = [self.x, self.y]

        # Makes sure a robot won't spawn on another robot
        if not self.collided(RunGame.robot_check):
            self.shape = Box((10*self.x, 10*self.y), 10, 10)
            self.coords.append(RunGame.robot_check)
    
    # Makes the robot move towards the player
    def move(self, player):
        if self.x > player.x and self.y > player.y:
            self.x -= 1
            self.y -= 1
        elif self.x < player.x and self.y > player.y:
            self.x += 1
            self.y -= 1
        elif self.x < player.x and self.y < player.y:
            self.x += 1
            self.y += 1
        elif self.x > player.x and self.y < player.y:
            self.x -= 1
            self.y += 1
        elif self.x > player.x:
            self.x -= 1
        elif self.x < player.x:
            self.x += 1
        elif self.y > player.y:
            self.y -= 1
        elif self.y < player.y:
            self.y += 1

        move_to(self.shape, (10*self.x, 10*self.y))


# Starts the game
run = RunGame()

# Loop to keep the game running
while not run.finished:
    run.next_move()
    
    # Seeing if the player wants to play again after winning or losing
    if run.finished:
        if read_yesorno("Would you like to play again? "):
            run = RunGame()

# Closes the game
run.over()

