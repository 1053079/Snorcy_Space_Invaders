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
        # Initializing enmey/Maybe make a function for this (Niels)
        self.image = pygame.image.load(f'assets/{alien}.png')
        # self.rect =
        self.x_pos = random.randint(0, SCREEN_WIDTH - 60)
        self.y_pos = random.randint(-50, 0)
        self.pos = [self.x_pos, self.y_pos]

        # Movement speed randomizer (Niels)
        self.vel = random.randint(5, 10) / 2

    def move(self):
        random_num = random.randint(1, 4)
        # Random movement for enemies (Niels)
        if random_num == 1:
            self.pos[1] += self.vel
        if random_num == 2:
            self.pos[0] += self.vel
        if random_num == 3:
            self.pos[0] += self.vel
            self.pos[1] += self.vel
        if random_num == 4:
            self.pos[0] -= self.vel
            self.pos[1] += self.vel
        # Enemies respawn
        self.respawn()
        # self.trigger()

    def respawn(self):
        # Respawns enemy back to top screen if not killed (Niels)
        if self.pos[1] > SCREEN_HEIGHT:
            # self.trigger()
            self.pos[0] = random.randint(0, SCREEN_WIDTH)
            self.pos[1] = random.randint(-50, 0)

    # # Not functional yet (Niels)
    # def trigger(self):
    #     # Makes the respawn wait 5 seconds (Niels)
    #     TRIGGER = pygame.USEREVENT + 1
    #     pygame.time.set_timer(TRIGGER, 10000)

    #     if self.respawn():
    #         trigger = 'wait'
    #         if trigger == 'wait' and pygame.event.get(TRIGGER):
    #             trigger = 'go'
    #         elif trigger == 'go':
    #             self.respawn()

    def render(self):
        # Draws everything on the screen (Niels)
        screen.blit(self.image, (self.pos))
        self.move()
