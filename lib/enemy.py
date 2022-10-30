import pygame
import random


alien4 = pygame.image.load("assets/img/alien4.png")
alien5 = pygame.image.load("assets/img/alien5.png")
alien6 = pygame.image.load("assets/img/alien6.png")


# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Enemy Class (Yong Pok)
class Enemy(pygame.sprite.Sprite):
    def __init__(self,rank):
        super().__init__()
        self.rank = rank
        if self.rank == 1:
            self.image = alien4
        elif self.rank == 2:
            self.image = alien5
        else:
            self.image = alien6
        
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(
            center=(random.randint(32, 600), (random.randint(-100, 0))))
        self.destroyed = False

    # How the enemy moves (Yong Pok)
    def move(self):
        self.rect.move_ip(0, random.randint(3,5))
        if (self.rect.bottom > 620) or self.destroyed == True:
            self.rect.center = (random.randint(32, 600),
                                (random.randint(-100, 0)))
            self.destroyed = False
    # Draws the enemies on screen (Yong Pok)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
