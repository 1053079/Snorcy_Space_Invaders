import random
from timeit import repeat
import pygame

# Initialzing the game
pygame.init()

# Create the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background
background = pygame.image.load('Tryouts/Niels/img/background.png')

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
alien_1_x_change = 3
alien_1_y_change = 40


def alien_1(x, y):
    screen.blit(alien_1_img, (x, y))


# bullet
bullet_x = 0
bullet_y = 480
bullet_img = pygame.image.load('Tryouts/Niels/img/bullet.png')
bullet_x_change = 0
bullet_y_change = 10
# You can't see the bullet (bullet_state = fire -> bullet moving)
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# Game loop
running = True
while running:

    # Color of game window
    screen.fill((BLACK))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check wether it's left or right
        if event.type == pygame.KEYDOWN:
            # Go left
            if event.key == pygame.K_a:
                player_x_change = -5
            # Go right
            if event.key == pygame.K_d:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(player_x, player_y)

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
        alien_1_x_change = 3
        alien_1_y += alien_1_y_change
    elif alien_1_x >= 736:
        alien_1_x_change = -3
        alien_1_y += alien_1_y_change

    # Bullet movement
    if bullet_state is "fire":
        fire_bullet(player_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    alien_1(alien_1_x, alien_1_y)

    pygame.display.update()
