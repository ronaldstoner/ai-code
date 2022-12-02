# Prompt:
# python countdown timer in pygame gui

import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 400
window_height = 400

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Set the countdown time in seconds
countdown_time = 10

# Create a font for displaying the countdown
font = pygame.font.Font(None, 36)

# Create a clock to track the time
clock = pygame.time.Clock()

# Main game loop
while countdown_time > 0:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the countdown time
    countdown_time -= clock.get_time() / 1000

    # Render the current countdown time
    countdown_text = font.render(str(countdown_time), 1, (255, 255, 255))

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the countdown time on the window
    window.blit(countdown_text, (100, 100))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# When the countdown reaches 0, print "Countdown complete!"
print("Countdown complete!")

