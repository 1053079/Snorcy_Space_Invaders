import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load('assets/alien1.png')
        x_pos = random.randint(0, screen_width)
        y_pos = random.randint(0, 100)
        self.pos = (x_pos, y_pos)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos)
