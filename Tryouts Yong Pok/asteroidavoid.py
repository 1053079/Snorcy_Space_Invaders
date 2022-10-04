import pygame
from pygame.locals import *
import random
import os

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
bg = pygame.image.load("images/background.png")

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

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
          self.rect.move_ip( 0, 5)

P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    P1.update()
    E1.move()               

    window.fill(BLACK)
    window.blit(bg,(0,0))

    P1.draw(window)
    E1.draw(window)

    pygame.display.update()
    framesPerSec.tick(FPS)