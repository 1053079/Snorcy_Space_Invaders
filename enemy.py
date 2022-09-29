import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__()
        vec = pygame.math.Vector2
        self.width = screen_width
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        self.image = pygame.image.load('assets/alien1.png')
        self.x_pos = random.randint(0, 800)
        self.y_pos = random.randint(0, 300)
        self.pos = [self.x_pos, self.y_pos]

        self.rect = self.image.get_rect()
        # self.rect.center = (self.pos)

        self.direction = random.randint(0, 1)
        self.vel = random.randint(1, 5) / 2

        # if self.direction == 0:
        #     self.pos[0] = 0
        #     self.pos[1] = 200
        #     self.pos.y
        # if self.direction == 1:
        #     self.pos[0] = 800
        #     self.pos[1] = 200

    def move(self):
        if self.pos[0] >= (self.width):
            self.direction = 1
        elif self.pos[0] <= 0:
            self.direction = 0

        if self.direction == 0:
            self.pos[0] += self.vel
        if self.direction == 1:
            self.pos[0] -= self.vel

        self.rect.center = self.pos

    def render(self):
        self.screen.blit(self.image, (self.pos[0], self.pos[1]))
        self.move()
