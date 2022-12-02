# Prompt:
# python countdown timer in pygame with font numbers and a background that blinks red for the last 3 seconds. when the timer hits 0 the window shake and buzz. as the timer decreases increase the font to perform a zoom effect

import pygame
import time as sleeper

# Initialize Pygame
pygame.init()

# Human intervention
# Set screen resolution
screen_width = 400
screen_height = 400

# Set up the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Countdown Timer")

# Human intervention
# Set the font size 
font_size = 36

# Load the font
font = pygame.font.Font("digital-7.ttf", font_size)

# Load a sound effect for when the timer reaches 0
buzz_sound = pygame.mixer.Sound('buzz.wav')

# Set the initial time
time = 10

# Set up the background color
bg_color = (0, 0, 0)

# Set up the text color
text_color = (255, 255, 255)

# Set up the timer event
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Run the game loop
while time >= 0:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            time -= 1
            # Human intervention
            # Increase the font
            font_size += 8
            # Update the font
            font = pygame.font.Font("digital-7.ttf", font_size)
            
    # Human intervention
    # Set the background color to white, unless it's the last 3 seconds
    #if time <= 3:
    #    bg_color = (255, 0, 0)
    #else:
    #    bg_color = (255, 255, 255)

    if time < 4:
        # Blink the background red for the last 3 seconds
        if time % 2 == 0:
            screen.fill((0, 0, 0))
        else:
            screen.fill((255, 0, 0))
    else:
        # Set the background to black for the rest of the countdown
        screen.fill((0, 0, 0))

    # Render the text
    text = font.render(str(time), True, text_color)

    # Get the size of the text
    text_rect = text.get_rect()

    # Center the text
    text_rect.center = (150, 100)
    
    # Zoom in as the time decreases
    text_rect.inflate_ip(time * 5, time * 5)

    # Clear the screen and draw the text
    # Human intervention
    #screen.fill(bg_color)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

    # If the timer is up, shake the screen and play a sound
    if time == 0:
        buzz_sound.play()
        for i in range(10):
            screen.fill((0, 0, 0))
            pygame.display.update()
            pygame.time.delay(50)
            screen.fill((255, 0, 0))
            pygame.display.update()
            pygame.time.delay(50) 
        #Human intervention
        #pygame.mixer.music.load("buzz.wav")
        #pygame.mixer.music.play()

# Show the "GAME OVER" screen
# Human intervention
# Set the font size
font_size = 50
# Update the font
font = pygame.font.Font("digital-7.ttf", font_size)
game_over_text = font.render("GAME OVER", True, (255, 255, 255))
screen.fill((255,0,0))
text_width = game_over_text.get_width()
text_height = game_over_text.get_height()
screen.blit(game_over_text, (screen_width // 2 - text_width // 2, screen_height // 2 - text_height // 2))
pygame.display.update()

sleeper.sleep(3)

# Quit Pygame when the timer is done
pygame.quit()


