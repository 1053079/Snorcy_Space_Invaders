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
        # Creating the enemies/Temperary until the create multipe enemy
        # function is fixed (Niels)
        self.enemy_1 = Enemy('alien1')
        self.enemy_2 = Enemy('alien2')
        self.enemy_3 = Enemy('alien3')

    def create_multiple_enemy_1(self, num_enemy_1):
        # Function to spawn multiple enemies (Niels)
        self.enemies_1 = []
        number_of_enemies = num_enemy_1
        # Loops through the number of enemies and pushes as many
        # enemies in the list (Niels)
        for num in range(number_of_enemies):
            self.enemies_1.append(Enemy('alien1'))
        # Loops through the enemy list and renders the enemies (Niels)
        for enemies in self.enemies_1:
            enemies.render()

    def run(self):
        # Function for what the game need to run (Niels)
        # self.create_multiple_enemy_1(3)
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

    # Calls the game class (Niels)
    game.run()

    # Puts game on 60fps (Niels)
    clock.tick(60)

    # Update the screen (Niels)
    pygame.display.update()
