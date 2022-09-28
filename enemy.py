import pygame


class Enemy():
    def __init__(self):
        self.image = pygame.image.load('/assets/alien1.png')
        self.rect = self.image.get_rect()
