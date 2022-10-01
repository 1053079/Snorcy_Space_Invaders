import pygame
import random

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock


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
            # self.trigger()
            self.pos[0] = random.randint(0, 800)
            self.pos[1] = random.randint(-50, 0)

    # def trigger(self):
    #     trigger = 'wait'
    #     if trigger == 'wait':
    #         pygame.time.set_timer(pygame.USEREVENT, 2000)
    #         trigger = 'go'
    #     elif trigger == 'go':
    #         self.pos[0] = random.randint(0, 800)
    #         self.pos[1] = random.randint(-50, 0)

    def render(self):
        screen.blit(self.image, (self.pos))
        self.move()
        # self.trigger()
