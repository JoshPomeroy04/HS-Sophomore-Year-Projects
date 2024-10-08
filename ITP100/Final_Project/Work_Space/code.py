# Importing modules
import pygame
import time
import random

# Initializing pygame
pygame.init()

# Creates screen
display = pygame.display.set_mode((810, 600))

# Sets the speed to run at
clock = pygame.time.Clock()

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
forest_green = (11, 102, 35)
mint_green = (152, 251, 152)
emerald_green = (80, 220, 100)
black = (0, 0, 0)

# Sets window background
display.fill(emerald_green)

# Sets text font
font = pygame.font.Font("freesansbold.ttf", 32)

# Sets window caption
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Makes black lines 
def checkerboard():
    if showline == True:
        display.fill(emerald_green)
        loop = 0
        xdraw = 0
        ydraw = 0
        for num in range(1, 55):
            pygame.draw.line(display, black, (xdraw, 0), (xdraw, 600))
            xdraw += 15

        for num in range(1, 41):
            pygame.draw.line(display, black, (0, ydraw), (810, ydraw))
            ydraw += 15
        pygame.display.update()
    else:
        display.fill(emerald_green)

# Function to display a text message on screen
def message(msg, color, x, y, size):
    font = pygame.font.SysFont("comicsansms", size)
    text = font.render(msg, True, color)
    display.blit(text, [x, y])

# Resets everything regarding the snake. (Location, size, and movement vector)
def reset_snake():
    checkerboard()
    snake_loc = [list(size)[0]/2, list(size)[1]/2]
    snake = [[list(size)[0]/2, list(size)[1]/2], [list(size)[0]/2 - 15, list(size)[1]/2], [list(size)[0]/2 - 30, list(size)[1]/2]]
    moving = ""
    for square in snake:
        pygame.draw.rect(display,forest_green, [square[0], square[1], 15, 15])

# Main game code
def game_run():
    # Setting variables
    select = True
    select2 = True
    select3 = True
    game_over = False
    game_end = False
    score = 0
    global size
    size = ()
    small = (420, 300)
    medium = (600, 420)
    large = (810, 600)
    fonts = 0
    font1 = 32
    font2 = 25
    font3 = 20
    loc1 = [320, 250, 70, 250]
    loc2 = [250, 170, 60, 170]
    loc3 = [170, 120, 10, 120]
    loc = []
    FPS = 0
    slow = 10
    normal = 15
    fast = 30
    display = pygame.display.set_mode((810, 600))
    global showline
    showline = True
    
    # Setting map size
    while select == True:
        message("Select a map size. S, M, or L", red, 180, 250, 32)
        pygame.display.update()
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                select = False
                select2 = False
                select3 = False
                game_over = True

            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_s:
                    size = small
                    fonts = font3
                    loc = loc3
                    select = False
                elif action.key == pygame.K_m:
                    size = medium
                    fonts = font2
                    loc = loc2
                    select = False
                elif action.key == pygame.K_l:
                    size = large
                    fonts = font1
                    loc = loc1
                    select = False
    display.fill(emerald_green)

    # Setting game speed
    while select2 == True:
        message("Select a game speed. S, N, or F", red, 180, 250, 32)
        pygame.display.update()
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                select2 = False
                select3 = False
                game_over = True
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_s:
                    FPS = slow
                    select2 = False
                elif action.key == pygame.K_n:
                    FPS = normal
                    select2 = False
                elif action.key == pygame.K_f:
                    FPS = fast
                    select2 = False
    display.fill(emerald_green)

    # Option to have lines on or off
    while select3 == True:
        message("Show lines (Not recommended)? Y or N", red, 100, 250, 32)
        pygame.display.update()
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                select3 = False
                game_over = True
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_y:
                    showline = True
                    select3 = False
                elif action.key == pygame.K_n:
                    showline = False
                    select3 = False
    # Sets variables that depend on results from settings, doesn't run if player closes the game while on selection screen
    if game_over == False:
        display = pygame.display.set_mode(size)
        checkerboard()
        snake_loc = [size[0]/2, size[1]/2]
        snake = [[size[0]/2, size[1]/2], [size[0]/2 - 15, size[1]/2], [size[0]/2 - 30, size[1]/2]]
        moving = "right"
        foodx = random.randrange(0, size[0] - 15, 15)
        foody = random.randrange(0, size[1] - 15, 15)

    # Game loop
    while game_over == False:
        # Sets run speed
        clock.tick(FPS)
        
        # Detects any action like pressing a key
        for action in pygame.event.get():

            # Exits game loop if red X in top left corner is clicked
            if action.type == pygame.QUIT:
                game_over = True

            # Specificly looks to see if a key is pressed down
            if action.type == pygame.KEYDOWN:

                # Looks at what key and does something accordingly
                if action.key == pygame.K_w and moving != "down":
                    moving = "up"
                elif action.key == pygame.K_s and moving != "up":
                    moving = "down"
                elif action.key == pygame.K_d and moving != "left":
                    moving = "right"
                elif action.key == pygame.K_a and moving != "right":
                    moving = "left"

        # Sets snake_loc to a different number in intervals of 15 which then causes the snake to move a certian direction
        if moving == "right":
            snake_loc[0] += 15
        elif moving == "left":
            snake_loc[0] -= 15
        elif moving == "up":
            snake_loc[1] -= 15
        elif moving == "down":
            snake_loc[1] += 15

        # Detects if the snake eats a peice of food
        if snake_loc[0] == foodx and snake_loc[1] == foody:

            # Changes food's location
            foodx = random.randrange(0, list(size)[0], 15)
            foody = random.randrange(0, list(size)[1], 15)
            score += 1
            message("Score: " + str(score), white, 0, 0, fonts)
            pygame.display.update()

        else:

            # Removes oldest item from the list snake if a peice of food isn't eaten
            snake.pop(0)

        # Detects if snake runs into boarder and ends game
        if snake_loc[0] >= list(size)[0] or snake_loc[0] < 0 or snake_loc[1] >= list(size)[1] or snake_loc[1] < 0:
            reset_snake()
            message("Game Over", red, list(loc)[0], list(loc)[1], fonts)
            pygame.display.update()
            time.sleep(2)
            reset_snake()
            game_end = True

        # Detects if snake runs into it's self and ends game
        for square in snake:
            if snake_loc == square:
                reset_snake()
                message("Game Over", red, list(loc)[0], list(loc)[1], fonts)
                pygame.display.update()
                time.sleep(2)
                reset_snake()
                game_end = True


        # Code that runs when game ends
        while game_end == True:
            message("Play Again? Hit Y to Play Again or N to quit", blue, list(loc)[2], list(loc)[3], fonts)
            message("Score: " + str(score), white, 0, 0, fonts)
            pygame.display.update()
            
            # Detects key click and restarts game if Y and closes game if N
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                        game_over = True
                        game_end = False
                if action.type == pygame.KEYDOWN:
                    if action.key == pygame.K_y:
                        display = pygame.display.set_mode((810, 600))
                        display.fill(emerald_green)
                        game_run()
                        game_end = False
                    elif action.key == pygame.K_n:
                        game_over = True
                        game_end = False

        # Adds snake_loc to snake making it appear the snake is moving
        snake.append(list(snake_loc))
        checkerboard()

        # Draws a square for each coordinate set in snake at the specific coordinate
        for square in snake:
            pygame.draw.rect(display, forest_green, [square[0], square[1], 15, 15])
        # Draws the food    
        pygame.draw.rect(display, red, [foodx, foody, 15, 15])
        message("Score: " + str(score), white, 0, 0, fonts)
        pygame.display.update()
    
    # Ends pygame and closes the window
    pygame.quit()
    quit()
    
game_run()
