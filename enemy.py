import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/alien1.png')
        self.rect = self.image.get_rect()
