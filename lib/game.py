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

        # Display Background Image (Shaq)
        self.background = pygame.image.load(
            'assets/img/SnorcyGameBackground.png')
        self.overlap = pygame.image.load(
            'assets/img/SnorcyGameBackground.png')
        # Rotate The Image With Degrees (Shaq)
        # self.background = pygame.transform.rotate(self.background, 90)
        # self.overlap = pygame.transform.rotate(self.overlap, 90)

        # Position 1st And 2nd Background Image (Shaq)
        self.b_pos = 0
        self.o_pos = -600
        # Speed Automatic Scroller (Shaq)
        self.speed = 1

        # Default Value For Level & Lives (Shaq)
        self.points = 0
        self.lives = 5
        # Time
        self.time = 60
        TIMER = pygame.USEREVENT
        pygame.time.set_timer(TIMER, 1000)
        # Font for text (Shaq)
        self.font = pygame.font.SysFont("Showcard Gothic", 30)
        # Draw Text (Shaq)
        self.lives_label = self.font.render(
            f"Lives: {self.lives}", 1, (255, 255, 255))
        self.points_label = self.font.render(
            f"Points: {self.points}", 1, (255, 255, 255))

    # Function to spawn multiple enemies(Niels)

    def create_multiple_enemies(self, num_enemy_1, num_enemy_2, num_enemy_3):
        # Push as many enemies 1 in a list (Niels)
        self.enemies = []
        num_of_enemies_1 = num_enemy_1
        num_of_enemies_2 = num_enemy_2
        num_of_enemies_3 = num_enemy_3
        for num in range(num_of_enemies_1):
            self.enemies.append(Enemy('alien4', self.enemies))
        for num in range(num_of_enemies_2):
            self.enemies.append(Enemy('alien7', self.enemies))
        for num in range(num_of_enemies_3):
            self.enemies.append(Enemy('alien6', self.enemies))

    # Function for the moving background
    def moving_background(self):
        # Background Slider (Shaq)
        if self.b_pos >= +SCREEN_HEIGHT:
            self.b_pos = -SCREEN_HEIGHT
        if self.o_pos >= +SCREEN_HEIGHT:
            self.o_pos = -SCREEN_HEIGHT

        # Speed Of Slider (Shaq)
        self.b_pos += self.speed
        self.o_pos += self.speed

        # Draw Background Image On Screen (Shaq)
        screen.blit(self.background, (0, self.b_pos))
        screen.blit(self.overlap, (0, self.o_pos))

    def hud(self):
        # Draw Text On Screen (Shaq)
        screen.blit(self.lives_label, (10, 10))
        screen.blit(self.points_label, (10, 40))

        time_label = self.font.render(f"Time: {self.time}", 1, (255, 255, 255))
        screen.blit(time_label, (10, 70))

    def laser_collision(self):
        if self.player.sprite.lasers:
            for lasers in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(lasers, self.asteroidGroup, True):
                    lasers.kill()
                # if pygame.sprite.spritecollide(lasers, self.enemies, True):
                #     lasers.kill()
                if pygame.sprite.spritecollide(lasers, self.asteroidXYGroup, True):
                    lasers.kill()



    # Function for what the game needs to run (Niels)
    def run(self):
        self.moving_background()
        self.player.sprite.lasers.draw(screen)

        # Loops through the enemies list and renders the enemies (Niels)
        for enemies in self.enemies:
            enemies.render()

        # Draws the asteroids on screen (Yong Pok)
        score = 0
        destroyed = False

        for asteroid in self.asteroidGroup:
            score = asteroid.move(score, destroyed)
            asteroid.draw(screen)

        for asteroidXY in self.asteroidXYGroup:
            score = asteroidXY.move(score, destroyed)
            asteroidXY.draw(screen)

        self.player.draw(screen)
        self.player.update()
        self.laser_collision()
        self.hud()
        # Asteroid Collision + soundFX (Yong Pok)
        for asteroid in self.asteroidGroup:
          if pygame.sprite.groupcollide(self.asteroidGroup, self.player,False, False):
             damage = pygame.mixer.Sound('assets/sounds/thud.wav')
             damage.set_volume(0.1)
             damage.play()
             self.lives -= 1
             
             pygame.display.update()

        for asteroid in self.asteroidGroup:
           if pygame.sprite.groupcollide(self.asteroidGroup, self.player,False , False):
            explosion = pygame.mixer.Sound('assets/sounds/explosion2.wav')
            explosion.set_volume(0.1)
            explosion.play()
            destroyed = True
            self.points = self.points + 1
            asteroid.move(score, destroyed)
            screen.blit(asteroid.image, asteroid.rect)

            destroyed = False

        for asteroid in self.asteroidGroup:
         self.score = asteroid.move(score, destroyed)
         asteroid.draw(screen)

       # Diagonal Asteroids collision + SoundFX (Yong Pok)
        for asteroidXY in self.asteroidXYGroup:
            if pygame.sprite.groupcollide(self.asteroidXYGroup,self.player,False, False):
             damage = pygame.mixer.Sound('assets/sounds/thud.wav')
             damage.set_volume(0.1)
             damage.play()
             pygame.display.update()

        for asteroidXY in self.asteroidXYGroup:
            if pygame.sprite.groupcollide(self.asteroidXYGroup,self.player,False, False):
              explosion = pygame.mixer.Sound('assets/sounds/explosion2.wav')
              explosion.set_volume(0.1)
              explosion.play()
              destroyed = True
              self.points = self.points + 1
              asteroidXY.move(score, destroyed)
              screen.blit(asteroidXY.image, asteroidXY.rect)
              destroyed = False

        for asteroidXY in self.asteroidXYGroup:
         self.score = asteroidXY.move(score, destroyed)
         asteroidXY.draw(screen)

    # Enemy mechanics
        # for enemy in self.enemyGroup:
        #     if pygame.sprite.groupcollide(self.enemyGroup, self.asteroidGroup,False, False):
        #       damage = pygame.mixer.Sound('assets/sounds/thud.wav')
        #       damage.play()
        #       pygame.display.update()

        # for enemy in self.enemyGroup:
        #     if pygame.sprite.groupcollide(self.enemyGroup, self.asteroidGroup,False, False):
        #      explosion = pygame.mixer.Sound('assets/sounds/explosion.wav')
        #      explosion.set_volume(0.5)
        #      explosion.play()
        #      destroyed = True
        #      #score = score + 5
        #      enemy.move(score, destroyed)
        #      screen.blit(enemy.image, enemy.rect)
        #      destroyed = False

        # for enemy in self.enemyGroup:
        #     #score = enemy.move(score, destroyed)
        #     enemy.draw(screen)

    pygame.display.update()
    FramesPerSec.tick(FPS)
