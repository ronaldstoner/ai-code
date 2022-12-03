# Prompt
# python script for a mazerunner

# Import the necessary libraries
import pygame

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window caption
pygame.display.set_caption("Maze Runner")

# Set the background color to black
screen.fill((0, 0, 0))

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define the maze
MAZE = [
  "#####",
  "# # #",
  "#   #",
  "# # #",
  "#####"
]

# Define the player's starting position
player_pos = (1, 1)

# Game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    # If the user closes the window, end the game loop
    if event.type == pygame.QUIT:
      running = False
  
  # Draw the maze
  for y in range(len(MAZE)):
    for x in range(len(MAZE[y])):
      if MAZE[y][x] == "#":
        # Calculate the screen coordinates
        screen_x = int(SCREEN_WIDTH / 2 + x - player_pos[0])
        screen_y = int(SCREEN_HEIGHT / 2 + y - player_pos[1])
        # Draw the wall
        pygame.draw.rect(screen, WHITE, (screen_x, screen_y, 1, 1))
      else:
        # Draw the floor
        pygame.draw.rect(screen, GREEN, (x * 20, y * 20, 20, 20))
  
  # Update the screen
  pygame.display.flip()

# Clean up and exit
pygame.quit()
exit()

