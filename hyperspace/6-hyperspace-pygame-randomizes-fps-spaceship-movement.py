# Prompt 
# python code for a hyperspace starfield animation in pygame with randomly sized stars and a FPS counter and a spaceship sprite that the user can move
 
import pygame
import random

# Initialize Pygame and set screen size
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load spaceship sprite
spaceship = pygame.image.load("spaceship.png")

# Human intervention
spaceship_x = 1
spaceship_y = 1

# Create a list of stars
stars = []
for i in range(200):
  x = random.randint(0, 800)
  y = random.randint(0, 600)
  size = random.randint(1, 3)
  stars.append((x, y, size))

# Initialize FPS clock
clock = pygame.time.Clock()

# Main game loop
while True:
  # Process events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  # Move spaceship based on keyboard input
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]:
    spaceship_y -= 3
  if pressed[pygame.K_DOWN]:
    spaceship_y += 3
  if pressed[pygame.K_LEFT]:
    spaceship_x -= 3
  if pressed[pygame.K_RIGHT]:
    spaceship_x += 3

  # Clear screen and draw stars
  screen.fill((0, 0, 0))
  for x, y, size in stars:
    pygame.draw.circle(screen, (255, 255, 255), (x, y), size)

  # Draw spaceship
  screen.blit(spaceship, (spaceship_x, spaceship_y))

  # Draw FPS counter
  fps = clock.get_fps()
  fps_text = f"FPS: {fps:.2f}"
  pygame.display.set_caption(fps_text)

  # Update screen
  pygame.display.flip()

  # Limit FPS
  clock.tick(60)

