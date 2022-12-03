# Prompt
# python code for a pacman clone. the player can move pacman around. holding down a movement key continues movement. pacman can eat the dots. if pacman touches a ghost the game is over and print "GAME OVER" on the screen for 4 seconds. 
# Note: This was generated in a different session

import time

# define constants for the game board
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# define constants for the characters
PACMAN = "P"
DOT = "."
GHOST = "G"

# initialize the game board
board = [
    ["."] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)
]

# initialize the starting position of Pac-Man
pacman_pos = (0, 0)
board[pacman_pos[0]][pacman_pos[1]] = PACMAN

# initialize the starting position of the ghosts
ghost_pos = [(1, 1), (1, 2), (2, 1), (2, 2)]
for pos in ghost_pos:
    board[pos[0]][pos[1]] = GHOST

# print the initial game board
for row in board:
    print(" ".join(row))

# define the movement directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# initialize the movement direction of Pac-Man
direction = None

# continuously prompt the user for a movement direction
while True:
    # get the user's input
    move = input("Enter a move (UP/DOWN/LEFT/RIGHT): ")

    # set the direction based on the user's input
    if move == "UP":
        direction = UP
    elif move == "DOWN":
        direction = DOWN
    elif move == "LEFT":
        direction = LEFT
    elif move == "RIGHT":
        direction = RIGHT
    else:
        print("Invalid move!")
        continue

    # move Pac-Man in the specified direction
    pacman_x, pacman_y = pacman_pos
    pacman_x += direction[0]
    pacman_y += direction[1]

    # check if Pac-Man has moved off the board
    if not (0 <= pacman_x < BOARD_WIDTH and 0 <= pacman_y < BOARD_HEIGHT):
        print("Pac-Man has moved off the board!")
        continue

    # check if Pac-Man has collided with a ghost
    if board[pacman_x][pacman_y] == GHOST:
        print("GAME OVER")
        time.sleep(4)  # wait for 4 seconds before exiting
        break

    # update the position of Pac-Man on the board
    board[pacman_pos[0]][pacman_pos[1]] = DOT
    board[pacman_x][pacman_y] = PACMAN
    pacman_pos = (pacman_x, pacman_y)

    # print the updated game board
    for row in board:
        print(" ".join(row))

