import pygame
import time
from pygame.locals import *
import random
from pygame import mixer

# Width and Height , speed/ frames per second (Yong Pok)
sw = 800
sh = 600
speed = 5
FPS = 60
framesPerSec = pygame.time.Clock()

# screen
window = pygame.display.set_mode((sw, sh))

# This controls the asteroid movement / speed and where they spawn. (Yong Pok)
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid32.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(
            center=(random.randint(32, 600), (random.randint(-100, 0))))

    def move(self):  # score, destroyed):
        self.rect.move_ip(0, random.randint(3,5))
        if (self.rect.bottom > 620):  # or destroyed == True:
            self.rect.center = (random.randint(32, 600),(random.randint(-100, 0)))
            # score += 1

        # return score

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# diagonal Asteroid
class AsteroidXY(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid64.png")
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(
            center=((random.randint(32, 600)), (random.randint(-100, 0))))

    def move(self):  # , score, destroyed):
        self.rect.move_ip(1, 2)
        if (self.rect.bottom > 664):  # or destroyed == True:
            self.rect.center = (random.randint(0, 0), (random.randint(-50, 0)))
        #     score += 1

        # return score

    def draw(self, surface):
        surface.blit(self.image, self.rect)


pygame.display.update()
framesPerSec.tick(FPS)
