import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 600
height = 400

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake block size and speed
block_size = 20
snake_speed = 15

# Fonts
font = pygame.font.SysFont(None, 35)

# Create Screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Eating Apple Game")

clock = pygame.time.Clock()

# Score Function
def show_score(score):
    value = font.render("Score: " + str(score), True, red)
    screen.blit(value, [10, 10])

# Snake drawing function
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

# Message display function
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Main loop game
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                      x1_change = -block_size
                      y1_change = 0
                  elif event.key == pygame.K_RIGHT:
                        x1_change = block_size
                        y1_change = 0
                  elif event.key == pygame.K_UP:
                        y1_change = -block_size

                        x1_change = 0
                  elif event.key == pygame.K_DOWN:
                        y1_change = block_size
                        x1_change = 0

        # Boundary Conditions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # If snake hits himself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # If apple is eaten
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()