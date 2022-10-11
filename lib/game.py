import pygame
from lib.asteroid import Asteroid, AsteroidXY
from lib.enemy import Enemy


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Game():
    def __init__(self):
        # Initial enemy spawn (Niels)
        self.create_multiple_enemies(2, 2, 2)

        # Adds the Asteroids into the game
        A1 = Asteroid()
        A2 = Asteroid()
        A3 = Asteroid()
        AXY1 = AsteroidXY()

    # def astroids(self):
        self.asteroidGroup = pygame.sprite.Group()
        self.asteroidGroup.add(A1)
        self.asteroidGroup.add(A2)
        self.asteroidGroup.add(A3)

        self.asteroidXYGroup = pygame.sprite.Group()
        self.asteroidXYGroup.add(AXY1)

    # def self_collision(self):
    #     collision_tolerance = 10
    #     for enemy in self.enemies:
    #         if enemy.colliderect(enemy):
    #             if (enemy.bottom - enemy.top) < collision_tolerance:
    #                 enemy.pos[0] *= -enemy.vel
    #                 print('col')
    #             if (enemy.right - enemy.left) < collision_tolerance:
    #                 enemy.pos[1] *= -enemy.vel
    #                 print('col')

    # Function to spawn multiple enemies 1 (Niels)

    def create_multiple_enemies(self, num_enemies_1, num_enemies_2, num_enemies_3):
        self.enemies = []
        number_of_enemies_1 = num_enemies_1
        number_of_enemies_2 = num_enemies_2
        number_of_enemies_3 = num_enemies_3
        for num in range(number_of_enemies_1):
            self.enemies.append(Enemy('alien1', self.enemies))
        for num in range(number_of_enemies_2):
            self.enemies.append(Enemy('alien2', self.enemies))
        for num in range(number_of_enemies_3):
            self.enemies.append(Enemy('alien3', self.enemies))

    # Function for what the game needs to run (Niels)
    def run(self):
        # Loops through the enemy 1 list and renders the enemies (Niels)
        for enemies in self.enemies:
            enemies.render()

        # Draws the asteroids on screen (Yong Pok)
        for asteroid in self.asteroidGroup:
            score = asteroid.move()
            asteroid.draw(screen)

        for asteroidXY in self.asteroidXYGroup:
            score = asteroidXY.move()
            asteroidXY.draw(screen)
