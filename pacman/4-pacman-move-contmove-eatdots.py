# Prompt
# python code for a pacman clone. the player can move pacman around. holding down a movement key continues movement. pacman can eat the dots. 

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Pacman Clone")

# Create a player character
player = pygame.Rect(330, 250, 20, 20)

# Create some ghosts
ghost1 = pygame.Rect(300, 200, 20, 20)
ghost2 = pygame.Rect(360, 200, 20, 20)

# Create some dots
dots = []
for x in range(300, 350, 10):
    for y in range(300, 310, 10):
        dot = pygame.Rect(x, y, 10, 10)
        dots.append(dot)

# Create a list of all game objects
game_objects = [player, ghost1, ghost2] + dots

# Define the player's speed
speed = 1

# Define the player's score
score = 0

# Game loop
done = False
while not done:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Handle keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
    elif keys[pygame.K_DOWN]:
        player.y += speed
    elif keys[pygame.K_LEFT]:
        player.x -= speed
    elif keys[pygame.K_RIGHT]:
        player.x += speed

    # Update the game state
    for dot in dots:
        if dot.colliderect(player):
            dots.remove(dot)
            score += 1

    # Draw the game elements
    screen.fill(BLACK)
    for game_object in game_objects:
        pygame.draw.rect(screen, WHITE, game_object)

    # Draw the player's score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.flip()

# Close the window
pygame.quit()

