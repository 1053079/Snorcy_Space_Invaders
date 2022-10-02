import math
import pygame

import random
from pygame import mixer

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY = 169, 169, 169
LIGHT_GREY = 211, 211, 211

# Font
score_font = pygame.font.Font('freesansbold.ttf', 32)
intro_font = pygame.font.Font('freesansbold.ttf', 64)
over_font = pygame.font.Font('freesansbold.ttf', 64)
button_font = pygame.font.Font('freesansbold.ttf', 32)

# Background
background = pygame.image.load('Tryouts/Niels/img/background.png')

# Background music
mixer.music.load('Tryouts/Niels/sound/background.wav')
mixer.music.play(-1)


# Score
score_value = 0

text_x = 10
text_y = 10


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


# Power up 1
asteroid_1_img = pygame.image.load('Tryouts/Niels/img/asteroid1.png')
asteroid_1_x = random.randint(0, 740)
asteroid_1_y = random.randint(-100, -5)
asteroid_1_x_change = 2
asteroid_1_y_change = 5


def asteroid_1(x, y):
    screen.blit((x, y))


class Button:
    def __init__(self, text, width, height, pos, elevation, screen, this_loop, next_loop, action=None):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_x_position = pos[0]
        self.original_y_position = pos[1]
        self.action = action
        self.screen = screen
        self.this_loop = this_loop
        self.next_loop = next_loop

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = WHITE

        # Botton rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = LIGHT_GREY

        # Text
        self.text_surf = button_font.render(text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_position - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color,
                         self.bottom_rect, border_radius=10)

        pygame.draw.rect(screen, self.top_color,
                         self.top_rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = GREY
            # Logic so button get pressed once
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    self.this_loop = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = WHITE


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

    # Start screen loop
    game_intro = True
    while game_intro:

        button_start = Button('Start', 225, 40, (325, 300), 6,
                              screen, game_intro, running, "play")
        button_high_score = Button('High Scores', 225, 40,
                                   (325, 360), 6, screen, game_intro, "high_scores")
        button_quit = Button('Quit', 225, 40, (325, 420),
                             6, screen, game_intro, "quit")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((BLACK))
        button_start.draw()
        button_high_score.draw()
        button_quit.draw()
        intro_text = intro_font.render("Space Invader", True, WHITE)
        screen.blit(intro_text, (200, 200))

        pygame.display.update()

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

    show_score(text_x, text_y)
    player(player_x, player_y)

    pygame.display.update()
