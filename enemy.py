import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, constraint, speed, num_aliens):
        super().__init__()
        self.image = pygame.image.load('/assets/alien1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = random.randint(0, 735)
        self.y = random.randint(-50, -10)
        self.y_change = speed
        self.x_change = 0
        self.max_x_constraint = constraint
        self.number_of_aliens = num_aliens

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self):
        self.constraint()
