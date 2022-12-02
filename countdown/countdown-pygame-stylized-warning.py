# Prompt: 
# python countdown timer in pygame with font numbers and a background that blinks red for the last 3 seconds

import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

# Set the countdown timer duration in seconds
duration = 10

# Create a font object to use for the countdown timer
font = pygame.font.Font("digital-7.ttf", 36)

# Main game loop
while duration > 0:
  # Check for any events (e.g. key presses, mouse clicks)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Render the countdown timer text
  text = font.render(str(duration), 1, (255, 255, 255))

  # Set the background color
  if duration < 4:
    # Blink the background red for the last 3 seconds
    if duration % 2 == 0:
      window.fill((0, 0, 0))
    else:
      window.fill((255, 0, 0))
  else:
    # Set the background to black for the rest of the countdown
    window.fill((0, 0, 0))

  # Blit the text to the screen
  window.blit(text, (window_width / 2, window_height / 2))

  # Update the display
  pygame.display.update()

  # Decrement the countdown timer
  duration -= 1

  # Pause for one second before updating the countdown timer again
  time.sleep(1)

# The countdown timer has finished, so exit the program
pygame.quit()
sys.exit()
