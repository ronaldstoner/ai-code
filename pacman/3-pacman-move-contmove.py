# Prompt
# python code for a pacman clone. the player can move pacman around. holding down a movement key continues movement.
 
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
dot1 = pygame.Rect(300, 300, 10, 10)
dot2 = pygame.Rect(310, 300, 10, 10)
dot3 = pygame.Rect(320, 300, 10, 10)
dot4 = pygame.Rect(330, 300, 10, 10)
dot5 = pygame.Rect(340, 300, 10, 10)

# Create a list of all game objects
game_objects = [player, ghost1, ghost2, dot1, dot2, dot3, dot4, dot5]

# Define the player's speed
speed = 1

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

    # Draw the game elements
    screen.fill(BLACK)
    for game_object in game_objects:
        pygame.draw.rect(screen, WHITE, game_object)

    # Update the screen
    pygame.display.flip()

# Close the window
pygame.quit()

