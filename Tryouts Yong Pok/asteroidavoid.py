import pygame
from pygame.locals import *
import random
import os
import math

pygame.init()

sw = 800
sh = 600

FPS = 60
framesPerSec = pygame.time.Clock()

BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)


window = pygame.display.set_mode ((sw, sh))
window.fill(BLACK)
pygame.display.set_caption ("Asteroids")

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

# Bullets

bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 5
bulletY_change = 20
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bulletImg, (x + 16, y + 10))

# Collision mechanics    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AsteroidPics/asteroid32.png")
        self.surf = pygame.Surface ((40, 40))
        self.rect = self.surf.get_rect(center = (random.randint(40,600), 0))

    def move(self):
        self.rect.move_ip(0,10)   
        if(self.rect.bottom > 600):
            self.rect.center = (random.randint(30,460), 0)

    def draw(self, surface):
     surface.blit(self.image, self.rect)           

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/spaceship.png")
        self.surf = pygame.Surface ((100, 150 ))
        self.rect = self.surf.get_rect(center = (400, 525))

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

class Background():
    def __init__(self):
        self.backgroundImage =pygame.image.load("images/starry.jpg")  
        self.rectBGimage = self.backgroundImage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = -self.rectBGimage.height
        self.bgX2 = 0     

        self.moveSpeed = 5

    def update(self):
        self.bgY1 += self.moveSpeed
        self.bgY2 += self.moveSpeed

        if self.bgY1> self.rectBGimage.height:
            self.bgY1 = -self.rectBGimage.height

        if self.bgY2> self.rectBGimage.height:
            self.bgY2 = -self.rectBGimage.height   
    def render(self):
        window.blit(self.backgroundImage,(self.bgX1, self.bgY1))
        window.blit(self.backgroundImage,(self.bgX2, self.bgY2))

background = Background()

P1 = Player()
E1 = Enemy()

while True:
    background.update()
    background.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    P1.update()
    E1.move()               

    P1.draw(window)
    E1.draw(window)

    pygame.display.update()
    framesPerSec.tick(FPS)