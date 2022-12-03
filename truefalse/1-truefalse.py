# Prompt
# python code for a true or false game using general trivia

import random

# List of trivia questions and answers
trivia_questions = [
    ("The capital of France is Paris", True),
    ("The Eiffel Tower is located in Rome", False),
    ("The currency of Japan is the Yen", True),
    ("Mount Everest is the tallest mountain in the world", True),
    ("The Great Wall of China is visible from space", False)
]

# Function to start the game
def start_game():
    print("Welcome to the True or False game!\n")
    score = 0
    
    # Shuffle the questions so they are in a random order
    random.shuffle(trivia_questions)
    
    # Loop through each question
    for question, answer in trivia_questions:
        # Print the question
        print(question)
        
        # Get the player's answer
        player_answer = input("Enter 'T' for True or 'F' for False: ")
        
        # Check if the player's answer is correct
        if player_answer.upper() == "T" and answer == True:
            print("Correct!\n")
            score += 1
        elif player_answer.upper() == "F" and answer == False:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer, "\n")
    
    # Print the player's final score
    print("Game Over! Your final score is:", score)

# Start the game
start_game()

