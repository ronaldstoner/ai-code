# Prompt:
#

import pygame
import time  # Human added

# Initialize Pygame and create a window
pygame.init()
screen_width=400
screen_height=400
screen = pygame.display.set_mode((screen_width, screen_height))

# Load a font for rendering the timer
font = pygame.font.Font('digital-7.ttf', 36)

# Load a sound effect for when the timer reaches 0
buzz_sound = pygame.mixer.Sound('buzz.wav')

# Set the starting time for the countdown
time_remaining = 10

# Create a Clock object to track time
clock = pygame.time.Clock()

# Main game loop
while time_remaining > 0:
    # Track the time that has passed
    time_passed = clock.tick()
    
    # Decrement the timer
    # Human modified 
    #time_remaining -= time_passed / 1000
    time_remaining -= 1

    ## Check if we are in the last 3 seconds
    #if time_remaining <= 3:
    #    # Blink the background red
    #    screen.fill((255, 0, 0))
    #else:
    #    # Clear the screen
    #    screen.fill((0, 0, 0))
    #  # Set the background color

    if time_remaining  < 4:
        # Blink the background red for the last 3 seconds
        if time_remaining % 2 == 0:
            screen.fill((0, 0, 0))
        else:
            screen.fill((255, 0, 0))
    else:
        # Set the background to black for the rest of the countdown
        screen.fill((0, 0, 0))

    # Render the timer text
    text = font.render(str(time_remaining), True, (255, 255, 255))
    # Human modified
    #screen.blit(text, (100, 100))
    screen.blit(text, (screen_width / 2, screen_height / 2))

    # Update the display
    pygame.display.flip()

    # Check if the timer has reached 0
    if time_remaining <= 0:
        # Play the buzz sound
        buzz_sound.play()

        # Shake the screen
        for i in range(10):
            # Scroll the screen to the right
            screen.scroll(10, 0)
            pygame.display.flip()
            pygame.time.delay(50)

            # Scroll the screen to the left
            screen.scroll(-10, 0)
            pygame.display.flip()
            pygame.time.delay(50)

    # Human added
    # Pause for one second before updating the countdown timer again
    time.sleep(1)

# The timer has reached 0, so explode the GUI
# (This is left as an exercise for the reader)

