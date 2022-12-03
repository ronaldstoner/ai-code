# Prompt
# Python script for a maze runner game that generates a random maze in pygame

import random
import pygame

# constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# generate a random maze
maze = []
for i in range(10):
    maze.append([])
    for j in range(10):
        if random.random() > 0.7:
            maze[i].append(1)
        else:
            maze[i].append(0)

# player's position
x = 0
y = 0

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and maze[x][y-1] == 0:
                y -= 1
            elif event.key == pygame.K_RIGHT and maze[x][y+1] == 0:
                y += 1
            elif event.key == pygame.K_UP and maze[x-1][y] == 0:
                x -= 1
            elif event.key == pygame.K_DOWN and maze[x+1][y] == 0:
                x += 1

    # draw the maze
    screen.fill(WHITE)
    for i in range(10):
        for j in range(10):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (i*80, j*60, 80, 60))

    # draw the player
    pygame.draw.rect(screen, BLACK, (x*80, y*60, 80, 60))

    # update the screen
    pygame.display.flip()

