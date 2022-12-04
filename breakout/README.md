
## Breakout AI Example
This repo contains AI generated examples of python code. The code iterates as additional conditions are added. This code shows an example of a Breakout clone.

|||
| --- | ----------- |
 **Prompt Progression** |
| ChatGPT |  "python script for a Breakout style game" |
| ChatGPT |  "python script that includes handling for when the ball hits the paddle" |
| ChatGPT |  "python script for a Breakout style game. the paddle is paddle.png. the ball is ball.png. the paddle can move left and right. when the ball hits the paddle it bounces back. if the ball goes off the bottom of the screen the game ends." |

## Overall Notes
ChatGPT was really good about generating a simple Breakout example. We see simple examples of physics and collision detection. Due to either limitations in the HTTP request body size, the length of time ChatGPT can output a response, or just code issues cause problems with further iterations such as scoring and top blocks to break.  

### 1 - Game skeleton
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script for a Breakout style game" |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/breakout/1.gif?raw=true" width="300">
Notes: We get a pretty good breakout style skeleton with a paddle at the bottom and a ball that can move. Our paddle has fluid user keypress movement. Edges are detected for bounce back. Our paddle listens to user input but cannot detect when it hits the ball.

### 2 - Paddle hits
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script that includes handling for when the ball hits the paddle" |  

<img src="https://github.com/ronaldstoner/ai-code/blob/main/breakout/2.gif?raw=true" width="300">
Notes: The AI gives us collision detection and we can now reverse the physics of the ball direction when the paddle detects a 'hit'. 

### 3 - Game over
|||
| --- | ----------- |
| **AI** | **Prompt** |
| ChatGPT |  "python script for a Breakout style game. the paddle is paddle.png. the ball is ball.png. the paddle can move left and right. when the ball hits the paddle it bounces back. if the ball goes off the bottom of the screen the game ends." |  
<img src="https://github.com/ronaldstoner/ai-code/blob/main/breakout/3.gif?raw=true" width="300">
Notes: We've lost fluid movement, collision detection, and have fallen back to indidivual key-presses for each movement. What we have gained is a game end condition when the ball passes the paddle and hits the bottom of the screen. Next iterations would attempt to include a GAME OVER message, but due to limitiations the entire code could not be generated. 
