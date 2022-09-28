import pygame
import math

pygame.init()

# Frames per Second
timer = pygame.time.Clock()
FPS = 30

# Screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# Image
background = pygame.image.load("images/starry.png").convert()
background_width = background.get_width()
background_height = background.get_height()
background = pygame.transform.scale(background, (WIDTH, background_height))
background_rect = background.get_rect()

scroll = 0
panels = math.ceil(HEIGHT / background_height) + 2

# Loop
running = True
while running:
    timer.tick(FPS)
    for i in range(panels):
        screen.blit(background, (i * background_height + scroll - background_height, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scroll += 5
    if abs(scroll) > background_width:
        scroll = 0

    pygame.display.flip()
pygame.quit()

