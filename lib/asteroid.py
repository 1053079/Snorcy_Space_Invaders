import pygame, time
from pygame.locals import *
import random
from pygame import mixer

# Width and Height , speed/ frames per second
sw = 800
sh = 600
speed = 5
FPS = 60
framesPerSec = pygame.time.Clock()

# screen
window = pygame.display.set_mode((sw,sh))

# filler / player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/playership.png")
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
P1= Player()

# This controls the asteroid movement / speed and where they spawn.
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid32.png")
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
        self.image = pygame.image.load("assets/asteroid64.png")
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(center=(random.randint(32, 600), (random.randint(-100, 0))))

    def move(self, score, destroyed):
        self.rect.move_ip(1,2)
        if (self.rect.bottom > 600) or destroyed == True:
            self.rect.center = (random.randint(0, 0), (random.randint(-50, 0)))
            score += 1

        return score

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        # This controls the asteroid movement / speed and where they spawn.
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid32.png")
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
        self.image = pygame.image.load("assets/asteroid64.png")
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(center=(random.randint(32, 600), (random.randint(-100, 0))))

    def move(self, score, destroyed):
        self.rect.move_ip(1,2)
        if (self.rect.bottom > 600) or destroyed == True:
            self.rect.center = (random.randint(0, 0), (random.randint(-50, 0)))
            score += 1

        return score

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    P1.update()
    P1.draw(window)

pygame.display.update()
framesPerSec.tick(FPS)
   





