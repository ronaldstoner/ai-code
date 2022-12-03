# Prompt
# python script for a galaga clone in pygame. background is moving stars of random sizes. player is player.png and the enemy is enemy.png. the player has 3 lives which are represented by half sized player icons in the upper left corner

import pygame
from random import randint

# initialize Pygame
pygame.init()

# set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set initial positions of stars
num_stars = 100
star_positions = []
for i in range(num_stars):
    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)
    star_positions.append((x, y))

# load player and enemy images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")

# Human intervention - half the lives icon size
life_image = pygame.transform.scale(player_image, (player_image.get_width() // 2, player_image.get_height() // 2))

# set player and enemy initial positions
player_x = SCREEN_WIDTH / 2
player_y = SCREEN_HEIGHT - player_image.get_height()
enemy_x = randint(0, SCREEN_WIDTH - enemy_image.get_width())
enemy_y = 0

# set number of lives and initial position of lives icons
num_lives = 3
life_icon_x = 20
life_icon_y = 20

# set game loop speed
clock = pygame.time.Clock()

# game loop
while True:
    # get player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 10
            if event.key == pygame.K_RIGHT:
                player_x += 10

    # move enemy down
    enemy_y += 5

    # move stars
    for i in range(num_stars):
        x, y = star_positions[i]
        y += 1
        if y > SCREEN_HEIGHT:
            # if star has moved off screen, move it back to top
            y = 0
            x = randint(0, SCREEN_WIDTH)
        star_positions[i] = (x, y)

    # redraw screen
    screen.fill((0, 0, 0))
    # draw stars
    for x, y in star_positions:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))
    # draw lives icons
    for i in range(num_lives):
        screen.blit(life_image, (life_icon_x + 30 * i, life_icon_y))
    pygame.display.flip()

    # set game loop speed
    clock.tick(60)

