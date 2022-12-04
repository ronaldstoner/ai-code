# Prompt
# python code for console based text adventure

# This is a simple text adventure game

print("Welcome to the text adventure game!")

name = input("What is your name? ")
print("Hello, " + name + "! Let's get started.")

# Set the initial location of the player
location = "outside"

# Define the actions the player can take
actions = ["north", "south", "east", "west", "look"]

# Define the game loop
while True:
  # Print the current location
  if location == "outside":
    print("You are standing outside of a mysterious castle.")
  elif location == "inside":
    print("You are inside the castle. It is dark and eerie.")
  else:
    print("Invalid location.")

  # Print the available actions
  print("What would you like to do? Available actions: " + ", ".join(actions))
  action = input("> ")

  # Handle the player's action
  if action == "north":
    if location == "outside":
      location = "inside"
    else:
      print("You cannot go north from here.")
  elif action == "south":
    if location == "inside":
      location = "outside"
    else:
      print("You cannot go south from here.")
  elif action == "east" or action == "west":
    print("You cannot go east or west from here.")
  elif action == "look":
    if location == "outside":
      print("You see a castle in front of you.")
    elif location == "inside":
      print("You see cobwebs in the corners of the room.")
  else:
    print("Invalid action.")

