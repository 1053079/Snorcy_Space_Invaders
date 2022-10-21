import pygame
import random

# Width and Height, speed(Yong Pok)
sw = 800
sh = 600
speed = 5

# screen
window = pygame.display.set_mode((sw, sh))


class Asteroid(pygame.sprite.Sprite):
    # This controls the asteroid movement / speed and where they spawn. (Yong Pok)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/img/asteroid32.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(
            center=(random.randint(32, 600), (random.randint(-100, 0))))
        self.destroyed = False

    def move(self):
        self.rect.move_ip(0, random.randint(3, 5))
        if (self.rect.bottom > 620) or self.destroyed == True:
            self.rect.center = (random.randint(32, 600),
                                (random.randint(-100, 0)))
            self.destroyed = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class AsteroidXY(pygame.sprite.Sprite):
    # diagonal Asteroid
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/img/asteroid64.png")
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(
            center=((random.randint(32, 600)), (random.randint(-100, 0))))

        self.destroyed = False

    def move(self):
        self.rect.move_ip(1, 2)
        if (self.rect.bottom > 664) or self.destroyed == True:
            self.rect.center = (random.randint(0, 0), (random.randint(-50, 0)))
            self.destroyed = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
