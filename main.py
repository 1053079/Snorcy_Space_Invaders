import pygame
from lib.button import Button
from lib.player import Player
from lib.game import Game

pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()

# Start menu (Rob)
start_menu = True

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load button images (Rob)
start_img = pygame.image.load('images/start-button2.png').convert_alpha()
exit_img = pygame.image.load('images/exit_button.png').convert_alpha()

# Display Background Image (Shaq)
background = pygame.image.load('Tryout Shaq/Images/Galaxy2-800x600.png')
overlap = pygame.image.load('Tryout Shaq/Images/Galaxy2-800x600.png')

# Position 1st And 2nd Background Image (Shaq)
b_pos = 0
o_pos = -600

# Speed Automatic Scroller (Shaq)
speed = 0.5

# Rotate The Image With Degrees (Shaq)
background = pygame.transform.rotate(background, 90)
overlap = pygame.transform.rotate(overlap, 90)

# Default Value For Level & Lives (Shaq)
level = 1
lives = 5

# Font for text (Shaq)
font = pygame.font.SysFont("Showcard Gothic", 30)

# Draw Text (Shaq)
lives_label = font.render(f"Lives: {lives}", 1, (255, 255, 255))
level_label = font.render(f"Level: {level}", 1, (255, 255, 255))

# Create button instances
start_button = Button(100, 240, start_img, 1)
exit_button = Button(450, 240, exit_img, 1)

score = 0
destroyed = False

game = Game()
running = True

while running:
    screen.fill((BLACK))

    if start_menu == True:
        screen.fill((83, 41, 42))
        if exit_button.draw(screen):
            running = False
        if start_button.draw(screen):
            start_menu = False
    else:
        # Draw Background Image On Screen (Shaq)
        screen.blit(background, (0, b_pos))
        screen.blit(overlap, (0, o_pos))

        game.run()
        #     Keybindings (Rhandell)
        #    keys = pygame.key.get_pressed()
        # if keys[pygame.K_a] and player.x - player_vel > 0: # Left
        #    player.x -= player_vel
        # if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # Right
        #    player.x += player_vel
        # if keys[pygame.K_w] and player.y - player_vel > 0: # Up
        #    player.y -= player_vel
        # if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # Down
        #    player.y += player_vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # Respawns enemies every 7.5 seconds (Niels)
            game.create_multiple_enemies(2)

    # Background Slider (Shaq)
    if b_pos >= +SCREEN_HEIGHT:
        b_pos = -SCREEN_HEIGHT
    if o_pos >= +SCREEN_HEIGHT:
        o_pos = -SCREEN_HEIGHT

    # Speed Of Slider (Shaq)
    b_pos += speed
    o_pos += speed

    # Draw Text On Screen (Shaq)
    screen.blit(lives_label, (10, 50))
    screen.blit(level_label, (10, 10))

    # Puts game on 60fps (Niels)
    clock.tick(60)

    # Update the screen (Niels)
    pygame.display.update()

pygame.quit()
