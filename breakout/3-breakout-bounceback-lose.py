# Prompt
# python script for a Breakout style game. the paddle is paddle.png. the ball is ball.png. the paddle can move left and right. when the ball hits the paddle it bounces back. if the ball goes off the bottom of the screen the game ends.

import pygame

# Initialize pygame
pygame.init()

# Set screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Breakout')

# Load the images
paddle_image = pygame.image.load('paddle.png')
ball_image = pygame.image.load('ball.png')

# Set the paddle's starting position
paddle_x = (SCREEN_WIDTH - paddle_image.get_width()) / 2
paddle_y = SCREEN_HEIGHT - paddle_image.get_height()

# Set the ball's starting position
ball_x = (SCREEN_WIDTH - ball_image.get_width()) / 2
ball_y = paddle_y - ball_image.get_height()

# Set the ball's starting velocity
ball_dx = 0.5
ball_dy = -0.5

# Set the game to run
running = True

# Main game loop
while running:
    # Check for events
    for event in pygame.event.get():
        # Handle closing the window
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        elif event.type == pygame.KEYDOWN:
            # Handle left and right arrow keys
            if event.key == pygame.K_LEFT:
                paddle_x -= 10
            elif event.key == pygame.K_RIGHT:
                paddle_x += 10

    # Update the ball's position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check if the ball has hit the left or right side of the screen
    if ball_x < 0 or ball_x > SCREEN_WIDTH - ball_image.get_width():
        ball_dx *= -1

    # Check if the ball has hit the top of the screen
    if ball_y < 0:
        ball_dy *= -1

    # Check if the ball has hit the paddle
    if (
        ball_x > paddle_x and
        ball_x < paddle_x + paddle_image.get_width() and
        ball_y == paddle_y
    ):
        ball_dy *= -1

    # Check if the ball has gone off the bottom of the screen
    if ball_y > SCREEN_HEIGHT:
        # Stop the game
        running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddle
    screen.blit(paddle_image, (paddle_x, paddle_y))

    # Draw the ball
    screen.blit(ball_image, (ball_x, ball_y))

    # Update the screen
    pygame.display.update()

# Close the window
pygame.quit()

