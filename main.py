import pygame
from lib.enemy import Enemy
from lib.asteroid import Asteroid, AsteroidXY
from lib.button import Button
from lib.player import Player
import random

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

#Display Background Image (Shaq)
background = pygame.image.load('Tryout Shaq/Images/Galaxy2-800x600.png')
overlap = pygame.image.load('Tryout Shaq/Images/Galaxy2-800x600.png')

#Position 1st And 2nd Background Image (Shaq)
b_pos = 0
o_pos = -600

#Speed Automatic Scroller (Shaq)
speed = 0.5

#Rotate The Image With Degrees (Shaq)
background = pygame.transform.rotate(background, 90)
overlap = pygame.transform.rotate(overlap, 90)

#Default Value For Level & Lives (Shaq)
level = 1
lives = 5

#Font for text (Shaq)
font = pygame.font.SysFont("Showcard Gothic", 30)

#Draw Text (Shaq)
lives_label = font.render(f"Lives: {lives}", 1, (255, 255, 255))
level_label = font.render(f"Level: {level}", 1, (255, 255, 255))

class Game():
    def __init__(self):
        # Initial enemy spawn (Niels)
        self.create_multiple_enemies(2, 2, 2)

    # Function to spawn multiple enemies 1 (Niels)
    def create_multiple_enemies(self, num_enemy_1, num_enemy_2, num_enemy_3):
        # Push as many enemies 1 in a list (Niels)
        self.enemies_1 = []
        number_of_enemies = num_enemy_1
        for num in range(number_of_enemies):
            self.enemies_1.append(Enemy('alien1'))

        # Push as many enemies 2 in a list (Niels)
        self.enemies_2 = []
        number_of_enemies = num_enemy_2
        for num in range(number_of_enemies):
            self.enemies_2.append(Enemy('alien2'))

        # Push as many enemies 3 in a list (Niels)
        self.enemies_3 = []
        number_of_enemies = num_enemy_3
        for num in range(number_of_enemies):
            self.enemies_3.append(Enemy('alien3'))

    # Function for what the game needs to run (Niels)
    def run(self):
        # Loops through the enemy 1 list and renders the enemies (Niels)
        for enemies in self.enemies_1:
            enemies.render()
        # Loops through the enemy 2 list and renders the enemies (Niels)
        for enemies in self.enemies_2:
            enemies.render()
        # Loops through the enemy 3 list and renders the enemies (Niels)
        for enemies in self.enemies_3:
            enemies.render()

# Create button instances
start_button = Button(100, 240, start_img, 1)
exit_button = Button(450, 240, exit_img, 1)

# Adds the Asteroids into the game
A1 = Asteroid()
A2 = Asteroid()
A3 = Asteroid()
AXY1 = AsteroidXY()

asteroidGroup = pygame.sprite.Group()
asteroidGroup.add(A1)
asteroidGroup.add(A2)
asteroidGroup.add(A3)

asteroidXYGroup = pygame.sprite.Group()
asteroidXYGroup.add(AXY1)

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
    
        # Draws the asteroids on screen (Yong Pok)
        for asteroid in asteroidGroup:
        score = asteroid.move(score, destroyed)
        asteroid.draw(screen)

      for asteroidXY in asteroidXYGroup:
        score = asteroidXY.move(score, destroyed)
        asteroidXY.draw(screen)    
        game.run()

        #Draw Background Image On Screen (Shaq)
        screen.blit(background, (0, b_pos))
        screen.blit(overlap, (0, o_pos))

    # Puts game on 60fps (Niels)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # Respawns enemies every 7.5 seconds (Niels)
            game.create_multiple_enemies(2, 2, 2)

   # Draws the asteroids on screen (Yong Pok)

    for asteroid in asteroidGroup:
        score = asteroid.move(score, destroyed)
        asteroid.draw(screen)

    for asteroidXY in asteroidXYGroup:
        score = asteroidXY.move(score, destroyed)
        asteroidXY.draw(screen)

    #Background Slider (Shaq)
    if b_pos >= +SCREEN_HEIGHT:
        b_pos = -SCREEN_HEIGHT
    if o_pos >= +SCREEN_HEIGHT:
        o_pos = -SCREEN_HEIGHT

    #Speed Of Slider (Shaq)
    b_pos += speed
    o_pos += speed

    #Draw Text On Screen (Shaq)
    screen.blit(lives_label, (10, 50))
    screen.blit(level_label, (10, 10))    

    # Update the screen (Niels)
    pygame.display.update()
pygame.quit()
