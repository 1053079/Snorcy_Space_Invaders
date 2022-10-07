from http.client import MOVED_PERMANENTLY
import pygame
import button

pygame.init()
# Create game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNORCY Start Menu")

# Load button images
start_img = pygame.image.load('images/start-button2.png').convert_alpha()
exit_img = pygame.image.load('images/exit_button.png').convert_alpha()

# Title Rob
title_font = pygame.font.Font(None,80)

# Create button instances
start_button = button.Button(100, 240, start_img, 1)
exit_button = button.Button(450, 240, exit_img, 1)

# Tile 
text_surface = title_font.render('SNORCY',False, 'Red')


# GAME LOOP
run = True
while run:

    screen.fill((83, 41, 42))
    screen.blit(text_surface,(290,80))

    if start_button.draw(screen):
        print('Start')
    if exit_button.draw(screen):
        run = False

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()