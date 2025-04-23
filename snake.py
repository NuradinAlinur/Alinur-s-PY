import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 820, 620
TILE_SIZE = 26
VELOCITY = 10

BG_COLOR = (45, 45, 45)
SNAKE_COLOR = (0, 160, 160)
FOOD_COLOR = (190, 10, 10)
TEXT_COLOR = (250, 250, 90)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Classic Snake Game")

font = pygame.font.Font(None, 34)


def draw_text(content, x, y, color=TEXT_COLOR):
    text_surface = font.render(content, True, color)
    screen.blit(text_surface, (x, y))


def generate_food(snake_body):
    while True:
        x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE
        if (x, y) not in snake_body:
            return x, y


def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, SNAKE_COLOR,
                         (segment[0], segment[1], TILE_SIZE, TILE_SIZE))


def draw_food(food_pos):
    pygame.draw.rect(screen, FOOD_COLOR,
                     (food_pos[0], food_pos[1], TILE_SIZE, TILE_SIZE))


def game_loop():
    start_x = 6 * TILE_SIZE
    start_y = 6 * TILE_SIZE
    snake = [(start_x, start_y), (start_x - TILE_SIZE, start_y),
             (start_x - 2 * TILE_SIZE, start_y)]
    direction = "RIGHT"
    food = generate_food(snake)
    score = 0
    level = 1
    speed = VELOCITY

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_s and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_a and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_d and direction != "LEFT":
                    direction = "RIGHT"

        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= TILE_SIZE
        elif direction == "DOWN":
            head_y += TILE_SIZE
        elif direction == "LEFT":
            head_x -= TILE_SIZE
        elif direction == "RIGHT":
            head_x += TILE_SIZE

        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False
        if (head_x, head_y) in snake:
            running = False

        snake.insert(0, (head_x, head_y))

        if (head_x, head_y) == food:
            score += 1
            food = generate_food(snake)
            if score % 3 == 0:
                level += 1
                speed += 1
        else:
            snake.pop()

        draw_snake(snake)
        draw_food(food)
        draw_text(f"Score: {score}", 20, 20)
        draw_text(f"Level: {level}", 670, 20)

        pygame.display.update()
        clock.tick(speed)

    screen.fill(BG_COLOR)
    draw_text("Game Over!", WIDTH // 2 - 90, HEIGHT // 2 - 20, FOOD_COLOR)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()


game_loop()
