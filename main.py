import pygame
from lib.button import Button
from lib.game import Game

pygame.init()

# Background Music (Rhandell)
pygame.mixer.music.load("assets/bgm.mp3")
pygame.mixer.music.play(-1)  

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()

# game variables Start menu (Rob)
start_menu = True
start_menu_main = "main"
play_game = False

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load button images (Rob)
start_img = pygame.image.load('images/SnorcyStartButton.png').convert_alpha()
exit_img = pygame.image.load('images/SnorcyExitButton.png').convert_alpha()
tutorial_image = pygame.image.load(
    "images/SnorcyTutorialButton.png").convert_alpha()
back_image = pygame.image.load("images/SnorcyBackButton.png").convert_alpha()
arrowkeys_image = pygame.image.load("images/arrows.png").convert_alpha()

# Display Background Image (Shaq)
background = pygame.image.load('Tryout Shaq/Images/Galaxy2-800x600.png')
overlap = pygame.image.load('Tryout Shaq/Images/Galaxy2-800x600.png')

# Caption and icon (Rob)
pygame.display.set_caption("Snorcy: Shooter Game")
icon = pygame.image.load('images/Snow1.png').convert()
pygame.display.set_icon(icon)

# Title Game (Rob)
font = pygame.font.Font('assets/Pixeltype.ttf', 120)
title_surface = font.render('The Return of Thanos', False, (219, 13, 13))
title_rect = title_surface.get_rect(midtop=(400, 110))

# Text Turtorial (Rob)
font_tutorial = pygame.font.Font('assets/Pixeltype.ttf', 60)
tutorial_text_surface = font_tutorial.render(
    "Welcome to our game.", False, (252, 194, 3))
tutorial_rect = tutorial_text_surface.get_rect(
    center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/10))
arrowkeys_image = pygame.image.load("images/arrows.png").convert_alpha()
arrowkeys_rect = arrowkeys_image.get_rect(midbottom = (200,350))
font_arrow_text = pygame.font.Font('assets/Pixeltype.ttf',60)
arrow_text_surface = font_arrow_text.render("To Move Around.", False,(252,194,3))
arrow_rect = arrow_text_surface.get_rect(center = (40,100))

# pause menu (Rob)
font_pause = pygame.font.Font('assets/Pixeltype.ttf', 30)
pause_text_surface = font_pause.render(
    "Press Esc to pause", False, (252, 194, 3))
pause_rect = pause_text_surface.get_rect(
    center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))


# Position 1st And 2nd Background Image (Shaq)
b_pos = 0
o_pos = -600

# Speed Automatic Scroller (Shaq)
speed = 0.5

# Rotate The Image With Degrees (Shaq)
background = pygame.transform.rotate(background, 90)
overlap = pygame.transform.rotate(overlap, 90)

# Default Value For Level & Lives (Shaq)
points = 1
lives = 5

# Time
time = 60
TIMER = pygame.USEREVENT
pygame.time.set_timer(TIMER, 1000)

# Font for text (Shaq)
font = pygame.font.SysFont("Showcard Gothic", 30)

# Draw Text (Shaq)
lives_label = font.render(f"Lives: {lives}", 1, (255, 255, 255))
points_label = font.render(f"Points: {points}", 1, (255, 255, 255))

# Create button instances (Rob)
start_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)
exit_button = Button(SCREEN_WIDTH/2, 280, exit_img, 1)
tutorial_button = Button(-2, 5, tutorial_image, 1)
back_button = Button(795 - 105, 595 - 62, back_image, 0.8)

score = 0
destroyed = False

game = Game()
running = True

while running:
    screen.fill((BLACK))

    if start_menu == True:
        screen.fill((83, 41, 42))
        if start_menu_main == "main":
            screen.blit(title_surface, title_rect)
            if exit_button.draw(screen):
                running = False
            if tutorial_button.draw(screen):
                start_menu_main = "tutorial"
            if start_button.draw(screen):
                start_menu = False
        if start_menu_main == "tutorial":
            screen.blit(arrowkeys_image, arrowkeys_rect)
            screen.blit(tutorial_text_surface, tutorial_rect)
            if back_button.draw(screen):
                start_menu_main = "main"
    else:
        # Draw Background Image On Screen (Shaq)
        screen.blit(background, (0, b_pos))
        screen.blit(overlap, (0, o_pos))

        # Draw Text On Screen (Shaq)
        screen.blit(lives_label, (10, 10))
        screen.blit(points_label, (10, 40))

        time_label = font.render(f"Time: {time}", 1, (255, 255, 255))
        screen.blit(time_label, (10, 70))

        game.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # Respawns enemies every 7.5 seconds (Niels)
            game.create_multiple_enemies(2, 2, 2)
        if event.type == pygame.USEREVENT and start_menu == False:
            time_label = font.render(f"Time: {time}", 1, (255, 255, 255))
            time -= 1

    # Background Slider (Shaq)
    if b_pos >= +SCREEN_HEIGHT:
        b_pos = -SCREEN_HEIGHT
    if o_pos >= +SCREEN_HEIGHT:
        o_pos = -SCREEN_HEIGHT

    # Speed Of Slider (Shaq)
    b_pos += speed
    o_pos += speed

    # Puts game on 60fps (Niels)
    clock.tick(60)

    # Update the screen (Niels)
    pygame.display.update()

pygame.quit()
