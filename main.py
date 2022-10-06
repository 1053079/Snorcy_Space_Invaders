import pygame
from enemy import Enemy
from player import Player

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
        # Creating the enemies

        self.enemy_1 = Enemy('alien1')
        self.enemy_2 = Enemy('alien2')
        self.enemy_3 = Enemy('alien3')

    # def create_multiple(self):
    #     self.enemies_1 = []
    #     for e_1 in range(3):
    #         self.enemies_1.append(Enemy('alien1'))
    #         return self.enemies_1[e_1]

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

            # Keybindings
            keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # Left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # Right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # Up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # Down
            player.y += player_vel

    game.run()

    clock.tick(60)

    pygame.display.update()
