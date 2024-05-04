import pygame
import time
import sys
import os

pygame.init()

# Экран меню
WIDTH, HEIGHT = 1000, 800
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("ИГРА")

clock = pygame.time.Clock()

# sc = pg.display.set_mode((300, 200))
FPS = 100

# Константы основных цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# координаты круга
x = WIDTH // 2
y = HEIGHT // 2



def playing_field():
    screen.fill(WHITE)
    
    pygame.display.flip()
    
def player():
    pygame.draw.circle(screen, BLACK, (x, y), 10)

    

playing_field()
player()
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    
    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3
    playing_field()
    player()
    pygame.display.update()
    clock.tick(FPS)   


pygame.quit()