# Prompt
# python code for a hyperspace starfield animation in pygame with randomly sized stars

import random
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and frame rate
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the number of stars in the starfield
num_stars = 100

# Initialize the starfield with random positions, speeds, and sizes
stars = []
for i in range(num_stars):
    # Generate random (x, y) position for the star
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    # Generate a random speed and size for the star
    speed = random.randint(1, 10)
    size = random.randint(1, 5)
    stars.append((x, y, speed, size))

# This function moves the stars in the starfield
def move_stars():
    for i in range(num_stars):
        x, y, speed, size = stars[i]
        # Move the star in the x direction by its speed
        x = x + speed
        # If the star has moved off the edge of the screen,
        # wrap it around to the other side
        if x > SCREEN_WIDTH:
            x = 0
        stars[i] = (x, y, speed, size)

# This function draws the starfield on the screen
def draw_starfield():
    screen.fill((0, 0, 0))  # Fill the screen with black
    for x, y, speed, size in stars:
        # Draw the star as a white circle at its position
        pygame.draw.circle(screen, (255, 255, 255), (x, y), size)
    pygame.display.flip()  # Update the screen

# Main animation loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_stars()
    draw_starfield()

    clock.tick(FPS)  # Limit the frame rate

