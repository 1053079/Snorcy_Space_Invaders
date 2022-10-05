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
        # Creating the enemies
        self.create_multiple_enemies(1, 1, 1)

    def create_multiple_enemies(self, num_enemy_1, num_enemy_2, num_enemy_3):
        # Function to spawn multiple enemies 1 (Niels)
        self.enemies_1 = []
        number_of_enemies = num_enemy_1
        # Loops through the number of enemies and pushes as many
        # enemies in the list (Niels)
        for num in range(number_of_enemies):
            self.enemies_1.append(Enemy('alien1'))

        # Function to spawn multiple enemies 2 (Niels)
        self.enemies_2 = []
        number_of_enemies = num_enemy_2
        for num in range(number_of_enemies):
            self.enemies_2.append(Enemy('alien2'))

        # Function to spawn multiple enemies 3 (Niels)
        self.enemies_3 = []
        number_of_enemies = num_enemy_3
        for num in range(number_of_enemies):
            self.enemies_3.append(Enemy('alien3'))

    def run(self):
        # Function for what the game need to run (Niels)

        # Loops through the enemy 1 list and renders the enemies (Niels)
        for enemies in self.enemies_1:
            enemies.render()
        # Loops through the enemy 2 list and renders the enemies (Niels)
        for enemies in self.enemies_2:
            enemies.render()
        # Loops through the enemy 3 list and renders the enemies (Niels)
        for enemies in self.enemies_3:
            enemies.render()


game = Game()
running = True

while running:
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            Enemy.TRIGGER = True
            Enemy.trigger = 'go'
    # Calls the game class (Niels)
    game.run()

    # Puts game on 60fps (Niels)
    clock.tick(60)

    # Update the screen (Niels)
    pygame.display.update()
