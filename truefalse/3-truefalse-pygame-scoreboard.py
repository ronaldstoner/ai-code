# Prompt
# python code for a true or false game using general trivia in Pygame with a visible scoreboard

# Import the Pygame library
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the title of the window
pygame.display.set_caption("True or False Game")

# Set up the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the background color
screen.fill(WHITE)

# Set the font for the text
font = pygame.font.SysFont("Arial", 36)

# Set the initial score to 0
score = 0

# Set the question and answer for the game
question = "Mount Everest is the tallest mountain in the world."
answer = True

# Display the question
question_text = font.render(question, 1, BLACK)
screen.blit(question_text, (100, 200))

# Display the options for the answer (true or false)
true_text = font.render("True", 1, BLACK)
screen.blit(true_text, (100, 300))
false_text = font.render("False", 1, BLACK)
screen.blit(false_text, (300, 300))

# Display the current score
score_text = font.render("Score: " + str(score), 1, BLACK)
screen.blit(score_text, (500, 500))

# Update the screen
pygame.display.flip()

# Wait for the player to make a selection
done = False
while not done:
    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the x and y coordinates of the mouse click
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            # Check if the player clicked on the true or false option
            if x > 100 and x < 200 and y > 300 and y < 350:
                # Player clicked on the true option
                if answer == True:
                    # The player was correct, so increase the score
                    score += 1
                else:
                    # The player was incorrect, so decrease the score
                    score -= 1
            elif x > 300 and x < 400 and y > 300 and y < 350:
                # Player clicked on the false option
                if answer == False:
                    # The player was correct, so increase the score
                    score += 1
                else:
                    # The player was incorrect, so decrease the score
                    score -= 1

            # Update the score on the screen
            score_text = font.render("Score: " + str(score), 1, BLACK)
            screen.blit(score_text, (500, 500))

            # Update the screen
            pygame.display.flip()

            # End the game
            done = True

