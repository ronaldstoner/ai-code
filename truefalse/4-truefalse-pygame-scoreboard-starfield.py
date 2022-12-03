# Prompt
# Python code for a true or false game using general trivia in Pygame with a visible scoreboard and moving starfield in the background

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame and set up the window
pygame.init()

# Set the width and height of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("True or False")

# Set up the fonts
font = pygame.font.Font(None, 48)

# Set up the player's score
score = 0

# Set up the questions and answers
questions = [
    ["Is the capital of Australia Sydney?", True],
    ["Is the square root of 144 16?", False],
    ["Is the sky blue?", True],
    ["Do zebras have stripes?", True]
]

# Set up the starfield
starfield = []
for i in range(100):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    starfield.append([x, y])

# Set up the game loop
done = False
clock = pygame.time.Clock()
while not done:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the starfield
    for star in starfield:
        star[1] += 1
        if star[1] > 500:
            star[1] = 0
            star[0] = random.randrange(0, 700)

    # Draw the starfield
    screen.fill(BLACK)
    for star in starfield:
        pygame.draw.ellipse(screen, WHITE, [star[0], star[1], 2, 2])

    # Draw the scoreboard
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Shut down Pygame
pygame.quit()

