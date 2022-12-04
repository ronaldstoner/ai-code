
## Adventure AI Example
This repo contains AI generated examples of python code. The code iterates as additional conditions are added. This code shows an example of a Adventure text based game clone.

|||
| --- | ----------- |
 **Prompt Progression** |
| ChatGPT |  "python code for console based text adventure" |
| ChatGPT |  "python code for console based text adventure. the player has an inventory that can be shown. inside the inventory is the book 'The Necronomicon' |
| ChatGPT |  "python code for console based text adventure. the player has an inventory that can be shown. inside the inventory is the book 'The Necronomicon'. The player should be able to check character stats." |

## Overall Notes
ChatGPT was able to get a good portion of a text based adventure game generated. It started to fail after 3 or 4 generations when adding things like enemies and larger more complex detailed rooms. The AI was good at generating a basic user interface, inventory system with item, and character stats.   

### 1 - Game skeleton
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python code for console based text adventure" |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/adventure/1.png?raw=true" width="500">
Notes: Our AI hits it out of the park, personalizing the Adventure experience by asking the user for their name. We get a concept of two rooms, inside and outside - each with a description. Movement is implented as expected would be for a text adventure. 

### 2 - Inventory
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python code for console based text adventure. the player has an inventory that can be shown. inside the inventory is the book 'The Necronomicon' " |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/adventure/2.png?raw=true" width="500">
Notes: The AI listens and implements an item system. We can locate and retrieve one item "The Necronomicon" by entering the inside room, looking, and taking the item. The 'inventory' command works and shows us either our empty inventory, or real ultimate power once we've obtained the book. 

### 3 - Character stats
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python code for console based text adventure. the player has an inventory that can be shown. inside the inventory is the book 'The Necronomicon'. The player should be able to check character stats." |  
<img src="https://github.com/ronaldstoner/ai-code/blob/main/adventure/3.png?raw=true" width="500">
Notes: What good is any Adventure RPG type game without statistics? It's no problem for the AI and we as players can now check our stats. 
