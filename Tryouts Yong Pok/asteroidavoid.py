import pygame, time
from pygame.locals import *
import random
import math
import sys

from pygame import mixer

pygame.font.init()

pygame.init()

# Width and Height
sw = 800
sh = 600

# Frames Per second
FPS = 60
framesPerSec = pygame.time.Clock()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen and Menu
window = pygame.display.set_mode((sw, sh))
window.fill(BLACK)
pygame.display.set_caption("Asteroids")

speed = 5

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

# game mechanics
lives = 3

# Bullets

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(player.rect.midtop))
        self.fired = False
        
    # this checks for player input
    def fire(self, player):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_SPACE] and self.fired == False:
            self.rect = (self.surf.get_rect(center=(player.rect.midtop)))
            self.fired = True
         # Speed of the bullets
        if self.fired == True:
            window.blit(self.image, self.rect)
            self.rect.move_ip(0, -5)

            if (self.rect.top < 1):
                self.rect.top = 600
                self.fired = False

    def resetPos(self):
        self.rect.top = 600
        self.fired = False


# bulletImg = pygame.image.load('images/bullet.png')
# bulletX = 0
# bulletY = 480
# bulletX_change = 5
# bulletY_change = 20
# bullet_state = "ready"


# def fire_bullet(x, y):
#    global bullet_state
#    bullet_state = "fire"
#    window.blit(bulletImg, (x + 16, y + 10))

# Collision mechanics    
#def isCollision(enemyX, enemyY, bulletX, bulletY):
   # distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    #if distance < 27:
    #    return True
    #else:
    #    return False


# This controls the asteroid movement / speed and where they spawn.
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AsteroidPics/asteroid32.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(random.randint(32, 600), (random.randint(-100, 0))))

    def move(self, score, destroyed):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600) or destroyed == True:
            self.rect.center = (random.randint(30, 600), (random.randint(-100, 0)))
            score += 1

        return score

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class AsteroidXY(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AsteroidPics/asteroid64.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(random.randint(32, 600), (random.randint(-100, 0))))

    def move(self, score, destroyed):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600) or destroyed == True:
            self.rect.center = (random.randint(30, 600), (random.randint(-100, 0)))
            score += 1

        return score

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    # The Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/ufo.png")
        self.surf = pygame.Surface((64,64))
        self.rect = self.surf.get_rect(center=(random.randint(64,600), (random.randint(-100, 0))))

    def move(self,score, destroyed):
        self.rect.move_ip(1,1)    
        if (self.rect.bottom > 600) or destroyed == True:
           self.rect.center = (random.randint(0,0 ), (random.randint(-100, 0)))
           score += 1
    
        return score 

    def draw(self, surface):
        surface.blit(self.image, self.rect)   

    def checkoffScreen(self):
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:     
            return True



    # Player Character movement and where they spawn

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/spaceship.png")
        self.surf = pygame.Surface((100, 150))
        self.rect = self.surf.get_rect(center=(400, 525))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressedKeys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < sw:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        if self.rect.top > 0:
            if pressedKeys[K_UP]:
                self.rect.move_ip(0, -5)

        if self.rect.bottom < sh:
            if pressedKeys[K_DOWN]:
                self.rect.move_ip(0, 5)


# The background looping infinitely here
class Background:
    def __init__(self):
        self.backgroundImage = pygame.image.load("images/starry.png")
        self.rectBGimage = self.backgroundImage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = -self.rectBGimage.height
        self.bgX2 = 0
 
        self.moveSpeed = 5

    def update(self):
        self.bgY1 += self.moveSpeed
        self.bgY2 += self.moveSpeed

        if self.bgY1 > self.rectBGimage.height:
            self.bgY1 = -self.rectBGimage.height

        if self.bgY2 > self.rectBGimage.height:
            self.bgY2 = -self.rectBGimage.height

    def render(self):
        window.blit(self.backgroundImage, (self.bgX1, self.bgY1))
        window.blit(self.backgroundImage, (self.bgX2, self.bgY2))


background = Background()

INCREASE_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED, 3000)

# This function draws the enemy and player classes
P1 = Player()
A1 = Asteroid()
A2 = Asteroid()
A3 = Asteroid()
AXY1 = AsteroidXY()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()
B1 = Bullet(P1)

asteroidGroup = pygame.sprite.Group()
asteroidGroup.add(A1)
asteroidGroup.add(A2)
asteroidGroup.add(A3)

asteroidXYGroup = pygame.sprite.Group()
asteroidXYGroup.add(AXY1)

enemyGroup = pygame.sprite.Group()
enemyGroup.add(E1)
enemyGroup.add(E2)
enemyGroup.add(E3)

bullets = pygame.sprite.Group()
bullets.add(B1)

# Fonts for game
font = pygame.font.SysFont("BungeeSpice.ttf", 60)
gameover = font.render("Game Over", True, WHITE)

score = 0
destroyed = False

# Game Loop

while True:
    scoreRender = font.render("Score:" + str(score), True, WHITE)
    background.update()
    background.render()
    window.blit(scoreRender, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == INCREASE_SPEED:
            speed += 0.5

    if pygame.sprite.spritecollideany(P1, asteroidGroup):
        damage = pygame.mixer.Sound('wav/thud.wav')
        damage.play()
        window.fill(RED)
        window.blit(gameover, (400, 300))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()

    for entity in bullets:
        entity.fire(P1)

    for asteroid in asteroidGroup:
        if pygame.sprite.spritecollide(asteroid, bullets, False):
            explosion = pygame.mixer.Sound('wav/explosion.wav')
            explosion.set_volume(0.5)
            explosion.play()
            destroyed = True
            score = score + 5
            asteroid.move(score, destroyed)
            window.blit(asteroid.image, asteroid.rect)
            B1.resetPos()
            destroyed = False

    for asteroid in asteroidGroup:
        score = asteroid.move(score, destroyed)
        asteroid.draw(window)

     # Diagnoal Asteroids
    for asteroidXY in asteroidXYGroup:
         if pygame.sprite.spritecollideany(P1, asteroidXYGroup):
          damage = pygame.mixer.Sound('wav/thud.wav')
          damage.play()
          window.fill(RED)
          window.blit(gameover, (400, 300))
          pygame.display.update()
          time.sleep(2)
          pygame.quit()

    for asteroidXY in asteroidXYGroup:
     if pygame.sprite.spritecollide(asteroidXY, bullets, False):
            explosion = pygame.mixer.Sound('wav/explosion.wav')
            explosion.set_volume(0.5)
            explosion.play()
            destroyed = True
            score = score + 5
            asteroidXY.move(score, destroyed)
            window.blit(asteroidXY.image, asteroidXY.rect)
            B1.resetPos()
            destroyed = False     
    
    for asteroidXY in asteroidXYGroup:
        score = asteroidXY.move(score, destroyed)
        asteroidXY.draw(window)
        

     # Enemy mechanics
    for enemy in enemyGroup:
        if pygame.sprite.spritecollideany(P1, enemyGroup):
         damage = pygame.mixer.Sound('wav/thud.wav')
         damage.play()
         window.fill(RED)
         window.blit(gameover, (400, 300))
         pygame.display.update()
         time.sleep(2)
         pygame.quit()

    for enemy in enemyGroup:
        if pygame.sprite.spritecollide(enemy, bullets, False):
            explosion = pygame.mixer.Sound('wav/explosion.wav')
            explosion.set_volume(0.5)
            explosion.play()
            destroyed = True
            score = score + 5
            enemy.move(score, destroyed)
            window.blit(enemy.image, enemy.rect)
            B1.resetPos()
            destroyed = False   

    for enemy in enemyGroup:
        score = enemy.move(score, destroyed)
        enemy.draw(window)


    P1.update()
    P1.draw(window)

    pygame.display.update()
    framesPerSec.tick(FPS)
