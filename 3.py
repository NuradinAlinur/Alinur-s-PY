import pygame
import sys
import random
import time

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
BLUE = (0, 0, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Переменные игры
SPEED = 5
SCORE = 0
COINS = 0

# Настройка шрифтов
font = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 22)
game_over = font.render("Game Over", True, WHITE)

# Фоновое изображение
background = pygame.image.load("AnimatedStreet.png")

# Окно игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")

# Классы объектов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = -50
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = -50
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

# Создание спрайтов
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, coin)

enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

# Событие увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 0.2
    
    scores_text = font_small.render(f"Score: {SCORE}", True, WHITE)
    coins_text = font_small.render(f"Coins: {COINS}", True, WHITE)
    screen.blit(scores_text, (10, 10))
    screen.blit(coins_text, (SCREEN_WIDTH - 120, 10))
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
        pygame.display.update()
        time.sleep(2)
        running = False
    
    collected_coin = pygame.sprite.spritecollideany(player, coins)
    if collected_coin:
        collected_coin.kill()
        COINS += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
