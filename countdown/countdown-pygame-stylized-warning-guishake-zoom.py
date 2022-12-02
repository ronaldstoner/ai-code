import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((300, 200))
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
        pygame.font.quit()

# Quit Pygame when the timer is done
pygame.quit()

