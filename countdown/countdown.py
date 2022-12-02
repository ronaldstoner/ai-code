# Prompt:
# python countdown timer

import time

# Set the countdown time in seconds
countdown_time = 10

# Start the countdown
while countdown_time > 0:
    print(countdown_time)
    time.sleep(1)
    countdown_time -= 1

# When the countdown reaches 0, print "Countdown complete!"
print("Countdown complete!")
