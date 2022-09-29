import math
import random

import pygame
from pygame import mixer


# Initialzing the game
pygame.init()

# Create the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background
background = pygame.image.load('Tryouts/Niels/img/background.png')

# Background music
# mixer.music.load('Tryouts/Niels/sound/background.wav')
# mixer.music.play(-1)

# Clock
clock = pygame.time.Clock()

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY = 169, 169, 169
LIGHT_GREY = 211, 211, 211

# Score
score_value = 0

text_x = 10
text_y = 10

# Font
score_font = pygame.font.Font('freesansbold.ttf', 32)
intro_font = pygame.font.Font('freesansbold.ttf', 64)
over_font = pygame.font.Font('freesansbold.ttf', 64)
button_font = pygame.font.Font('freesansbold.ttf', 32)

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


# bullet
bullet_x = 0
bullet_y = 480
bullet_img = pygame.image.load('Tryouts/Niels/img/bullet.png')
bullet_x_change = 0
bullet_y_change = 10
# You can't see the bullet (bullet_state = fire -> bullet moving)
bullet_state = "ready"


class Alien():
    def __init__(self, img, x, y, x_change, y_change, num):
        # Core atributes
        file_path = f'Tryouts/Niels/img/{img}.png'
        self.alien_img = []
        # alien_x = x
        self.alien_x = [x]

        self.alien_y = [y]
        self.alien_x_change = [x_change]
        self.alien_y_change = [y_change]
        self.alien_num = num

        # Alien list
        for i in range(self.alien_num):
            self.alien_img.append(pygame.image.load(file_path))
            self.alien_x = random.randint((0, 735))


# Alien 1
alien_1_img = []
alien_1_x = []
alien_1_y = []
alien_1_x_change = []
alien_1_y_change = []
num_of_aliens_1 = 6

for i in range(num_of_aliens_1):
    alien_1_img.append(pygame.image.load('Tryouts/Niels/img/alien1.png'))
    alien_1_x.append(random.randint(0, 735))
    alien_1_y.append(random.randint(50, 150))
    alien_1_x_change.append(2.7)
    alien_1_y_change.append(40)


def alien_1(x, y, i):
    screen.blit(alien_1_img[i], (x, y))


# Alien 2
alien_2_x = []
alien_2_img = []
alien_2_y = []
alien_2_x_change = []
alien_2_y_change = []
num_of_aliens_2 = 1

for ij in range(num_of_aliens_2):
    alien_2_img.append(pygame.image.load('Tryouts/Niels/img/alien2.png'))
    alien_2_x.append(random.randint(0, 735))
    alien_2_y.append(random.randint(0, 75))
    alien_2_x_change.append(1)
    alien_2_y_change.append(40)


def alien_2(x, y, ij):
    screen.blit(alien_2_img[ij], (x, y))


# Asteroid
asteroid_1_img = pygame.image.load('Tryouts/Niels/img/asteroid1.png')
asteroid_1_x = random.randint(0, 300)
asteroid_1_y = random.randint(-75, -5)
asteroid_1_x_speed = 150
asteroid_1_y_speed = 170


# Score function


def show_score(x, y):
    score = score_font.render("Score: " + str(score_value), True, (WHITE))
    screen.blit(score, (x, y))

# Game over text


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (WHITE))
    screen.blit(over_text, (200, 250))

# Firing bullets


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Collision function


def is_collision_alien_1(alien_1_x, alien_1_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(alien_1_x - bullet_x, 2) +
                         math.pow(alien_1_y - bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False


def is_collision_alien_2(alien_2_x, alien_2_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(alien_2_x - bullet_x, 2) +
                         math.pow(alien_2_y - bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False

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
                # Fire key
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound(
                        'Tryouts/Niels/sound/laser.wav')
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, player_y)

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
    for i in range(num_of_aliens_1) or ij in range(num_of_aliens_2):

        # Game over text
        if alien_1_y[i] > 450:
            for j in range(num_of_aliens_1):
                alien_1_y[j] = 2000
            game_over_text()
            break
        elif alien_2_y[ij] > 450:
            for iji in range(num_of_aliens_2):
                alien_2_y[iji] = 2000
            game_over_text()
            break

        alien_1_x[i] += alien_1_x_change[i]
        alien_2_x[ij] += alien_2_x_change[ij]

    # Aliens check for boundry, and change direction
        if alien_1_x[i] <= 0:
            alien_1_x_change[i] = 2.7
            alien_1_y[i] += alien_1_y_change[i]
        elif alien_1_x[i] >= 736:
            alien_1_x_change[i] = -2.7
            alien_1_y[i] += alien_1_y_change[i]

        if alien_2_x[ij] <= 0:
            alien_2_x_change[ij] = 1
            alien_2_y[ij] += alien_2_y_change[ij]
        elif alien_2_x[ij] >= 736:
            alien_2_x_change[ij] = -1
            alien_2_y[ij] += alien_2_y_change[ij]

        # Colission
        collision_alien_1 = is_collision_alien_1(
            alien_1_x[i], alien_1_y[i], bullet_x, bullet_y)
        if collision_alien_1:
            explosion_sound = mixer.Sound(
                'Tryouts/Niels/sound/explosion.wav')
            explosion_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            alien_1_x[i] = random.randint(0, 735)
            alien_1_y[i] = random.randint(50, 150)

        collision_alien_2 = is_collision_alien_2(
            alien_2_x[ij], alien_2_y[ij], bullet_x, bullet_y)
        if collision_alien_2:
            explosion_sound = mixer.Sound(
                'Tryouts/Niels/sound/explosion.wav')
            explosion_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 4
            alien_2_x[ij] = random.randint(0, 735)
            alien_2_y[ij] = random.randint(0, 75)

        alien_1(alien_1_x[i], alien_1_y[i], i)
        alien_2(alien_2_x[ij], alien_2_y[ij], ij)

    # Bullet movement
    if bullet_y <= -32:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Asteroid
    screen.blit(asteroid_1_img, (asteroid_1_x, asteroid_1_y))
    mili_sec = clock.tick()
    seconds = mili_sec/1000.
    # Astroid movement x direction
    dmx = seconds * asteroid_1_x_speed
    # Asteroid movement y direction
    dmy = seconds * asteroid_1_y_speed

    asteroid_1_x += dmx
    asteroid_1_y += dmy

    show_score(text_x, text_y)
    player(player_x, player_y)

    pygame.display.update()
