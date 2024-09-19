from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

# Snake Game settings
snake = [[2, 4], [3, 4], [4, 4]]  # Initial snake co-ordinates
snake_direction = "right"
food = None

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,200,150)

def draw_snake(snake):
    for segment in snake[:-1]:
        sense.set_pixel(segment[0], segment[1], green)
    head = snake[-1]
    sense.set_pixel(head[0], head[1], blue)
    

def move():
    global snake
    head = snake[-1].copy()
    if snake_direction == "right":
        head[0] = head[0] + 1 if head[0] < 7 else 0
    elif snake_direction == "left":
        head[0] = head[0] - 1 if head[0] > 0 else 7
    elif snake_direction == "up":
        head[1] = head[1] - 1 if head[1] > 0 else 7
    elif snake_direction == "down":
        head[1] = head[1] + 1 if head[1] < 7 else 0
    snake.append(head)
    snake.pop(0)

def check_collision(snake):
    head = snake[-1]
    return head in snake[:-1] or head[0] < 0 or head[0] > 7 or head[1] < 0 or head[1] > 7

def add_food():
    global food
    food = [randint(0, 7), randint(0, 7)]
    while food in snake:  # Regenerate food if it's on the snake
        food = [randint(0, 7), randint(0, 7)]
    sense.set_pixel(food[0], food[1], red)

def eat_food():
    global snake, food
    if snake[-1] == food:
        snake.insert(0, snake[0])
        add_food()

def joystick_moved(event):
    global snake_direction
    directions = {"right": "left", "left": "right", "up": "down", "down": "up"}
    if event.action == 'pressed' and directions[snake_direction] != event.direction:
        snake_direction = event.direction

sense.stick.direction_any = joystick_moved

add_food()

# Main game loop
while True:
    move()
    eat_food()
    if check_collision(snake):
        sleep(1)
        break
    sense.clear()
    draw_snake(snake)
    sense.set_pixel(food[0],food[1],red)
    sleep(0.5)

sense.show_message("Game Over!", text_colour=red)
