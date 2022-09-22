import random
import pygame

# Initialzing the game
pygame.init()

# Create the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Tryouts/Niels/img/ufo.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('Tryouts/Niels/img/player.png')
player_x = 370
player_y = 480
player_x_change = 0


def player(x, y):
    screen.blit(player_img, (x, y))


# alien1
alien_1_img = pygame.image.load('Tryouts/Niels/img/alien1.png')
alien_1_x = random.randint(0, 800)
alien_1_y = random.randint(50, 150)
alien_1_x_change = 0.3
alien_1_y_change = 40


def alien_1(x, y):
    screen.blit(alien_1_img, (x, y))


# Game loop
running = True
while running:

    # Color of game window
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check wether it's left or right
        if event.type == pygame.KEYDOWN:
            # Go left
            if event.key == pygame.K_a:
                player_x_change = -0.3
            # Go right
            if event.key == pygame.K_d:
                player_x_change = 0.6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_change = 0

    # Moving the player
    player_x += player_x_change

    # Checking for boundries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    alien_1_x += alien_1_x_change

    # Aliens check for boundry, and change direction
    if alien_1_x <= 0:
        alien_1_x_change = 0.3
        alien_1_y += alien_1_y_change
    elif alien_1_x >= 736:
        alien_1_x_change = -0.3
        alien_1_y += alien_1_y_change

    player(player_x, player_y)
    alien_1(alien_1_x, alien_1_y)

    pygame.display.update()
