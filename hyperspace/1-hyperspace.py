# Prompt
# python code for a hyperspace starfield animation 

import random
import time

# Set the number of stars in the starfield
num_stars = 100

# Initialize the starfield with random positions and speeds
stars = []
for i in range(num_stars):
    # Generate random (x, y) position for the star
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    # Generate a random speed for the star
    speed = random.randint(1, 10)
    stars.append((x, y, speed))

# This function moves the stars in the starfield
def move_stars():
    for i in range(num_stars):
        x, y, speed = stars[i]
        # Move the star in the x direction by its speed
        x = x + speed
        # If the star has moved off the edge of the screen,
        # wrap it around to the other side
        if x > 100:
            x = 0
        stars[i] = (x, y, speed)

# This function draws the starfield on the screen
def draw_starfield():
    for x, y, speed in stars:
        print('*', end='')
    print()

# Main animation loop
while True:
    move_stars()
    draw_starfield()
    time.sleep(0.1)

