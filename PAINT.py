import pygame
import random

COLORS = {
    "red": (255, 0, 0),
    "green": (34, 139, 34),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

def start_paint_app():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Simple Paint")
    clock = pygame.time.Clock()
    
    brush_diameter = 15
    active_color = COLORS["blue"]
    last_position = None
    drawing_shape = None  # None, "rect", "circle"
    eraser_mode = False
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    active_color = COLORS["red"]
                    eraser_mode = False
                elif event.key == pygame.K_g:
                    active_color = COLORS["green"]
                    eraser_mode = False
                elif event.key == pygame.K_b:
                    active_color = COLORS["blue"]
                    eraser_mode = False
                elif event.key == pygame.K_c:
                    active_color = COLORS["cyan"]
                    eraser_mode = False
                elif event.key == pygame.K_LSHIFT:
                    active_color = COLORS["black"]
                    eraser_mode = False
                elif event.key == pygame.K_e:
                    active_color = COLORS["white"]  # Ластик
                    eraser_mode = True
                elif event.key == pygame.K_l:
                    drawing_shape = "rect"
                elif event.key == pygame.K_o:
                    drawing_shape = "circle"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    last_position = pygame.mouse.get_pos()
                    if drawing_shape == "rect":
                        draw_rect(screen, last_position, 200, 100, active_color)
                    elif drawing_shape == "circle":
                        draw_circle(screen, last_position, active_color)
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and last_position:
                if not drawing_shape:
                    paint_line(screen, last_position, pygame.mouse.get_pos(), brush_diameter, active_color)
                    last_position = pygame.mouse.get_pos()
        
        pygame.display.flip()
        clock.tick(60)

def paint_line(screen, start, end, size, color):
    pygame.draw.line(screen, color, start, end, size)

def draw_rect(screen, position, width, height, color):
    x, y = position
    pygame.draw.rect(screen, color, (x, y, width, height), 3)

def draw_circle(screen, position, color):
    x, y = position
    pygame.draw.circle(screen, color, (x, y), 50, 3)

start_paint_app()
