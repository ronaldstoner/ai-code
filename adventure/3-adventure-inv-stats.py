# Prompt
# python code for console based text adventure. the player has an inventory that can be shown. inside the inventory is the book "The Necronomicon". The player should be able to check character stats. 
 
# This is a simple text adventure game with an inventory system and character stats

print("Welcome to the text adventure game!")

name = input("What is your name? ")
print("Hello, " + name + "! Let's get started.")

# Set the initial location of the player
location = "outside"

# Create an empty list to store the player's inventory
inventory = []

# Define the character's stats
stats = {
  "strength": 10,
  "dexterity": 10,
  "intelligence": 10
}

# Define the actions the player can take
actions = ["north", "south", "east", "west", "look", "inventory", "stats"]

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
      # Check if the player has already found the Necronomicon
      if "Necronomicon" not in inventory:
        print("You also see a book on a pedestal. It looks ancient and foreboding.")
  elif action == "inventory":
    # Print the contents of the inventory
    if len(inventory) == 0:
      print("Your inventory is empty.")
    else:
      print("Your inventory contains:")
      for item in inventory:
        print("- " + item)
  elif action == "stats":
    # Print the character's stats
    print("Your stats:")
    for stat, value in stats.items():
      print("- " + stat + ": " + str(value))
  else:
    print("Invalid action.")

    # Check if the player is trying to take the Necronomicon
    if action == "take Necronomicon" and location == "inside":
      inventory.append("Necronomicon")
      print("You take the Necronomicon and add it to your inventory.")
    else:
      print("Invalid action.")

