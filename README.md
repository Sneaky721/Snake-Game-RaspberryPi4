Snake Game on Sense HAT
This code implements a simple Snake game using the Sense HAT library on a Raspberry Pi. The snake moves around the 8x8 LED matrix, grows by eating food, and ends the game if it collides with itself.

Requirements
Sense HAT is installed and connected to your Raspberry Pi.
Python 3.x installed with the sense_hat library. 

Gameplay
The joystick on the Sense HAT controls the snake, which moves continuously in the last input direction.

Objective: Eat the red food to grow. Avoid colliding with your own body.
Game Over: If the snake collides with itself or goes out of bounds.

Code Explanation

Variables
   sense: Initializes the Sense HAT object to interact with the LED matrix and joystick.
   snake: Stores the current coordinates of the snake on the 8x8 grid.
   snake_direction: Tracks the current direction of the snake ("right", "left", "up", or "down").
   food: Randomly generated coordinates for the food.

Colors:
   white: Displayed for the message at the end.
   green: Used for the snake body.
   blue: Used for the snake's head.
   red: Used for the food.

Functions
   draw_snake(snake): Updates the LED matrix to display the snake. The body is green, and the head is blue.

   move(): Moves the snake in the direction stored in snake_direction. The snake wraps around the grid when it hits the edges.

   check_collision(snake): Checks if the snake collides with itself.

   add_food(): Randomly places food on the grid, ensuring it doesn't spawn on the snake's body.

   eat_food(): When the snake reaches the food, it grows by adding a new segment and regenerates the food in a new location.

   joystick_moved(event): Handles joystick input to control the direction of the snake.

Game Loop
The game continuously moves the snake, checks for collisions, and redraws the snake and food. The game ends if the snake collides with itself.

At the end of the game, the message "Game Over!" is displayed in red text.

Usage
Run the code on a Raspberry Pi with a connected Sense HAT.
Use the joystick to control the snake and avoid collisions.


                   !!!!!ENJOY!!!!!
