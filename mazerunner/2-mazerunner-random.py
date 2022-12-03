# Prompt
# Here is an example of a Python script for a maze runner game that generates a random maze:

import random

# define the size of the maze
MAZE_WIDTH = 30
MAZE_HEIGHT = 30

# define the maze
maze = []
for y in range(MAZE_HEIGHT):
    maze.append([])
    for x in range(MAZE_WIDTH):
        if x == 0 or x == MAZE_WIDTH - 1 or y == 0 or y == MAZE_HEIGHT - 1:
            # add walls around the perimeter of the maze
            maze[y].append("#")
        else:
            # add a random wall or empty space
            if random.random() > 0.3:
                maze[y].append("#")
            else:
                maze[y].append(" ")

# define the player's starting position
player_x = 1
player_y = 1

# define the goal position
goal_x = MAZE_WIDTH - 2
goal_y = MAZE_HEIGHT - 2

# define the move directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# define the possible moves
moves = [UP, RIGHT, DOWN, LEFT]

# define the move function
def move(direction):
    global player_x, player_y
    if direction == UP:
        player_y -= 1
    elif direction == RIGHT:
        player_x += 1
    elif direction == DOWN:
        player_y += 1
    elif direction == LEFT:
        player_x -= 1
    else:
        print("Error: invalid move direction")

# play the game
while player_x != goal_x or player_y != goal_y:
    # display the current state of the maze
    for row in maze:
        print("".join(row))
    print()

    # prompt the user for a move direction
    move_direction = input("Enter move direction (UP, RIGHT, DOWN, LEFT): ")

    # make the move
    if move_direction.upper() == "UP":
        move(UP)
    elif move_direction.upper() == "RIGHT":
        move(RIGHT)
    elif move_direction.upper() == "DOWN":
        move(DOWN)
    elif move_direction.upper() == "LEFT":
        move(LEFT)
    else:
        print("Error: invalid move direction")

# display the final state of the maze
for row in maze:
    print("".join(row))

