# Prompt
# Python script that includes handling for when the ball hits the paddle

# Import necessary modules
import pygame
import sys

# Initialize game
pygame.init()

# Set screen width and height
screen_width = 800
screen_height = 600

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title and icon
pygame.display.set_caption("Breakout")
icon = pygame.image.load('paddle.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('paddle.png')
player_x = 370
player_y = 480
player_dx = 0

# Ball
ball_img = pygame.image.load('ball.png')
ball_x = 370
ball_y = 450
ball_dx = 0.3
ball_dy = 0.3

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -0.5
            if event.key == pygame.K_RIGHT:
                player_dx = 0.5

        # Handle key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dx = 0

    # Update player position
    player_x += player_dx
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - 64:
        player_x = screen_width - 64

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Handle ball collisions with screen edges
    if ball_x < 0 or ball_x > screen_width - 64:
        ball_dx *= -1
    if ball_y < 0:
        ball_dy *= -1
    if ball_y > screen_height - 64:
        ball_dy *= -1

    # Handle ball collision with paddle
    if ball_y > player_y and ball_x > player_x and ball_x < player_x + 64:
        ball_dy *= -1

    # Fill screen with background color
    screen.fill((0, 0, 0))

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw ball
    screen.blit(ball_img, (ball_x, ball_y))

    # Update screen
    pygame.display.update()

