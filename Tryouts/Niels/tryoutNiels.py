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


def player(x, y):
    screen.blit(player_img, (x, y))


# Game loop
running = True
while running:

    # Color of game window
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(player_x, player_y)
    pygame.display.update()
