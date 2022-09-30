import pygame
from enemy import Enemy

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Game():
    def __init__(self):
        self.enemy_1 = Enemy('alien1')
        self.enemy_2 = Enemy('alien2')
        self.enemy_3 = Enemy('alien3')

    def run(self):
        self.enemy_1.render()
        self.enemy_2.render()
        self.enemy_3.render()


game = Game()
running = True

while running:
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.run()

    clock.tick(60)

    pygame.display.update()
