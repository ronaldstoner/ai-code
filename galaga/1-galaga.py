# Prompt
# python script for a galaga clone in pygame

import pygame

# Initialize Pygame and set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Galaga Clone")

# Load images for the player's ship and the enemy ships
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")

# Create a class for the player's ship
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update(self):
        # Move the player's ship left and right based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

# Create a class for the enemy ships
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Move the enemy ships down the screen
        self.rect.y += 5

# Create a sprite group for the player and enemies
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

# Add some enemies to the game
for i in range(10):
    enemy = Enemy(i * 80, 50)
    sprites.add(enemy)

# Main game loop
while True:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the positions of the sprites
    sprites.update()

    # Draw the sprites to the screen
    screen.fill((0, 0, 0))
    sprites.draw(screen)
    pygame.display.flip()

