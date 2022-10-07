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
        # Initializing enmey (Niels)
        self.image = pygame.image.load(f'assets/{alien}.png')
        self.rect = self.image.get_rect()
        self.x_pos = random.randint(0, SCREEN_WIDTH - 60)
        self.y_pos = random.randint(-50, 0)
        self.pos = [self.x_pos, self.y_pos]

        # Movement speed randomizer (Niels)
        self.vel = random.randint(3, 10) / 2

        # Makes the enemies wait for so many seconds (Niels)
        self.TRIGGER = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TRIGGER, 7500)

    # Function for random movement for enemies (Niels)
    def move(self):
        random_num = random.randint(1, 5)
        if random_num == 1:
            self.pos[1] += self.vel
        if random_num == 2:
            self.pos[0] += self.vel
        if random_num == 3:
            self.pos[0] += self.vel
            self.pos[1] += self.vel
        if random_num == 4 or random_num == 5:
            self.pos[0] -= self.vel
            self.pos[1] += self.vel

    # Function to respawns enemy back to top screen if not killed (Niels)
    def respawn(self):
        if self.pos[1] > SCREEN_HEIGHT:
            # self.trigger()
            self.pos[0] = random.randint(0, SCREEN_WIDTH)
            self.pos[1] = random.randint(-50, 0)

    # Function that draws everything on the screen (Niels)
    def render(self):
        screen.blit(self.image, (self.pos))
        self.move()
