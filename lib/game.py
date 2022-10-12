import pygame
from lib.asteroid import Asteroid, AsteroidXY
from lib.enemy import Enemy
from lib.player import Player

FPS = 60
FramesPerSec = pygame.time.Clock()

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
        A4 = Asteroid()
        #E1 = Enemy()
        AXY1 = AsteroidXY()

        # Initializing player
        player = Player((SCREEN_WIDTH/2, SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player)

        # def astroids(self):
        self.asteroidGroup = pygame.sprite.Group()
        self.asteroidGroup.add(A1)
        self.asteroidGroup.add(A2)
        self.asteroidGroup.add(A3)
        self.asteroidGroup.add(A4)

        self.asteroidXYGroup = pygame.sprite.Group()
        self.asteroidXYGroup.add(AXY1)

        self.enemyGroup = pygame.sprite.Group()
        self.enemyGroup.add  # (E1)

    # Function to spawn multiple enemies 1 (Niels)
    def create_multiple_enemies(self, num_enemy_1, num_enemy_2, num_enemy_3):
        # Push as many enemies 1 in a list (Niels)
        self.enemies = []
        number_of_enemies = num_enemy_1
        for num in range(number_of_enemies):
            self.enemies.append(Enemy('alien1', self.enemies))
        for num in range(number_of_enemies):
            self.enemies.append(Enemy('alien2', self.enemies))
        for num in range(number_of_enemies):
            self.enemies.append(Enemy('alien3', self.enemies))

    # Function for what the game needs to run (Niels)
    def run(self):
        # Loops through the enemies list and renders the enemies (Niels)
        for enemies in self.enemies:
            enemies.render()

        # Draws the asteroids on screen (Yong Pok)
        for asteroid in self.asteroidGroup:
            score = asteroid.move()
            asteroid.draw(screen)

        for asteroidXY in self.asteroidXYGroup:
            score = asteroidXY.move()
            asteroidXY.draw(screen)

        self.player.draw(screen)
        self.player.update()

        # for asteroid in self.asteroidGroup:
        #   if pygame.sprite.groupcollide(self.asteroidGroup, self.asteroidXYGroup,False, False):
        #      damage = pygame.mixer.Sound('assets/thud.wav')
        #      damage.play()

        #      pygame.display.update()

        # for asteroid in self.asteroidGroup:
        #    if pygame.sprite.groupcollide(self.asteroidGroup, self.enemyGroup,False , False):
        #     explosion = pygame.mixer.Sound('wav/explosion.wav')
        #     explosion.set_volume(0.5)
        #     explosion.play()
        #     destroyed = True
        #     score = score + 5
        #     asteroid.move(score, destroyed)
        #     screen.blit(asteroid.image, asteroid.rect)

        #     destroyed = False

        # for asteroid in self.asteroidGroup:
        #score = asteroid.move(score, destroyed)
        # asteroid.draw(screen)

     # Diagnoal Asteroids
        # for asteroidXY in self.asteroidXYGroup:
        #     if pygame.sprite.groupcollide(self.asteroidXYGroup,self.asteroidGroup,self.enemyGroup, False):
        #      damage = pygame.mixer.Sound('assets/thud.wav')
        #      damage.play()
        #      pygame.display.update()

        # for asteroidXY in self.asteroidXYGroup:
        #     if pygame.sprite.groupcollide(self.asteroidXYGroup,self.asteroidGroup, self.enemyGroup, False):
        #       explosion = pygame.mixer.Sound('assets/explosion2.wav')
        #       explosion.set_volume(0.5)
        #       explosion.play()
        #       destroyed = True
        #       #score = score + 5
        #       asteroidXY.move#(score, destroyed)
        #       screen.blit(asteroidXY.image, asteroidXY.rect)
        #       destroyed = False

        # for asteroidXY in self.asteroidXYGroup:
        #score = asteroidXY.move(score, destroyed)
        # asteroidXY.draw(screen)

     # Enemy mechanics
        # for enemy in self.enemyGroup:
        #     if pygame.sprite.groupcollide(self.enemyGroup, self.asteroidGroup,False, False):
        #       damage = pygame.mixer.Sound('assets/thud.wav')
        #       damage.play()
        #       pygame.display.update()

        # for enemy in self.enemyGroup:
        #     if pygame.sprite.groupcollide(self.enemyGroup, self.asteroidGroup,False, False):
        #      explosion = pygame.mixer.Sound('wav/explosion.wav')
        #      explosion.set_volume(0.5)
        #      explosion.play()
        #      destroyed = True
        #      score = score + 5
        #      enemy.move(score, destroyed)
        #      screen.blit(enemy.image, enemy.rect)
        #      destroyed = False

        for enemy in self.enemyGroup:
            score = enemy.move(score)  # , destroyed)
            enemy.draw(screen)

    pygame.display.update()
    FramesPerSec.tick(FPS)
