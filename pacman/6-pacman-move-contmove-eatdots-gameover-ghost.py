# Prompt
# python code for a pacman clone. the player can move pacman around. holding down a movement key continues movement. pacman can eat the dots. if pacman touches a ghost the game is over and print "GAME OVER" on the screen for 4 seconds. pygame.

import pygame
import time

# Set up the Pygame window
pygame.init()
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player
player_size = 20
player_pos = [200, 200]

# Set up the dot
dot_size = 10
dot_pos = [100, 100]

# Set up the ghost
ghost_size = 20
ghost_pos = [300, 300]

# Set up the game over text
game_over_font = pygame.font.SysFont("Arial", 30)
game_over_text = game_over_font.render("GAME OVER", True, white)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (window_width / 2, window_height / 2)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Check if the player has eaten the dot
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    dot_rect = pygame.Rect(dot_pos[0], dot_pos[1], dot_size, dot_size)
    if player_rect.colliderect(dot_rect):
        dot_pos = [300, 300]

    # Check if the player has collided with the ghost
    ghost_rect = pygame.Rect(ghost_pos[0], ghost_pos[1], ghost_size, ghost_size)
    if player_rect.colliderect(ghost_rect):
        game_over = True

    # Draw the game
    window.fill(black)
    pygame.draw.rect(window, white, player_rect)
    pygame.draw.rect(window, white, dot_rect)
    pygame.draw.rect(window, white, ghost_rect)
    if game_over:
        window.blit(game_over_text, game_over_rect)
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Close the game
# Human intervention
time.sleep(4)
pygame.quit()

