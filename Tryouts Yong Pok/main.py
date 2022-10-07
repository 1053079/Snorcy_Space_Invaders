import pygame
import math
import random
from asteroids import SpaceRocks
from pygame import mixer
from game import Game
pygame.font.init()

WIDTH = 800
HEIGHT = 600

# Initialize the pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

# Background Image
bg = pygame.image.load('images/background.png')
# Background moving
screen = pygame.display.set_mode((800, 600))

class Background():

    def __init__(self):
         self.bg_img = pygame.image.load('images/background.png')
         self.rectBGimg = self.bg_img.get_rect()

         self.bgY1 = 0
         self.bgX1 = 0

         self.bgY2 = self.rectBGimg.height
         self.bgX2 = 0

         self.moving_speed = 5

    def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -=self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height

    def render(self):
        screen.blit(self.bg_img, (self.bgX1, self.bgY1))
        screen.blit(self.bg_img, (self.bgX2, self.bgY2))

# Speed of frames
clock = pygame.time.Clock()
FPS = 60

clock.tick(FPS)

# Background Sound
mixer.music.load("wav/Japanize Dream.wav")
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/reimu.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/ufo.png'))
    enemyX.append(random.randint(0, 768))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready = You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 5
bulletY_change = 20
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('BungeeSpice.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('BungeeSpice.ttf', 64)
lost_font = pygame.font.Font('Bullpen3D.ttf', 128)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = lost_font.render("You DIED", True, (255, 0, 0))
    screen.blit(over_text, (WIDTH/2 -over_text.get_width()/2, 200))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
           event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        # if keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('wav/Pew.wav')
                    bullet_Sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 +  -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # Player Movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    # Enemy Movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 768:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion = pygame.mixer.Sound('wav/explosion.wav')
            explosion.set_volume(0.5)
            explosion.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 769)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
