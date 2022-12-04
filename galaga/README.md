
## Galaga AI Example
This repo contains AI generated examples of python code. The code iterates as additional conditions are added. This code shows an example of a Galaga clone.

|||
| --- | ----------- |
 **Prompt Progression** |
| ChatGPT |  "python script for a galaga clone in pygame" |
| ChatGPT |  "python script for a galaga clone in pygame. background is moving stars of random sizes." |
| ChatGPT |  "python script for a galaga clone in pygame. background is moving stars of random sizes. player is player.png and the enemy is enemy.png. the player can move" |
| ChatGPT |  "python script for a galaga clone in pygame. background is moving stars of random sizes. player is player.png and the enemy is enemy.png. the player has 3 lives which are represented by half sized player icons in the upper left corner" |

## Overall Notes
ChatGPT is really good at almost recreating a Galaga like clone. Little to no human intevention was required for bug fixes and changes to timing and variables. 

### 1 - Game skeleton
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script for a galaga clone in pygame" |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/galaga/1.png?raw=true" width="300">
Notes: The AI has provided us with a pretty good start for a Galaga clone. We can see a player and enemy sprite. The enemy sprite prints across the screen and there is not much the player can do at this point. 


### 2 - Let's add stars
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script for a galaga clone in pygame. background is moving stars of random sizes." |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/galaga/2.gif?raw=true" width="300">
Notes: We add stars into the background. They may be hard to see in the picture as they are single pixels, but they are there with movements. As a bonus we get fluid keypress down movement as a gift from the AI. 

### 3 - Player movement
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script for a galaga clone in pygame. background is moving stars of random sizes. player is player.png and the enemy is enemy.png. the player can move" |  
<img src="https://github.com/ronaldstoner/ai-code/blob/main/galaga/3.gif?raw=true" width="300">
Notes: We've specified player movement as the script started to go a bit off course. As the AI giveth, the AI taketh away. We've lost continious movement, but we can still move a keypress at a time. The enemy now descends down towards the player sprite. Our stars are now a different size and everything moves at a different speed. This is due to using the prompt in a new AI session due to timeouts in the prior generation session. Think of this as a new branch off a tree.  

### 4 - Lives represented by ships
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script for a galaga clone in pygame. background is moving stars of random sizes. player is player.png and the enemy is enemy.png. the player has 3 lives which are represented by half sized player icons in the upper left corner" |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/galaga/4.gif?raw=true" width="300">
Notes: The AI has added a life counter represented by the ship sprite (width and height divided by an int) in the upper left hand corner. This plus the prior iterations shows us that we can easily piece together an interated Galaga clone through chat based AI. 
