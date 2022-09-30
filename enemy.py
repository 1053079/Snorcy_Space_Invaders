import pygame
import random

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, alien):
        super().__init__()

        self.image = pygame.image.load(f'assets/{alien}.png')
        self.x_pos = random.randint(0, SCREEN_WIDTH - 60)
        self.y_pos = random.randint(-50, 0)
        self.pos = [self.x_pos, self.y_pos]
        self.rect = self.image.get_rect()
        # Movement speed randomizer
        self.vel = random.randint(5, 10) / 2

    def move(self):
        self.pos[1] += self.vel

        if self.pos[1] > SCREEN_HEIGHT:
            self.pos[0] = random.randint(0, 800)
            self.pos[1] = random.randint(-50, 0)

    def render(self):
        screen.blit(self.image, (self.pos))
        self.move()
