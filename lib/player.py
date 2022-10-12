import pygame
import os

# Load Player ship image
PLAYER_SHIP = pygame.image.load("assets/playership.png")

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock

# Player Class


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ship_img = PLAYER_SHIP
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.y = SCREEN_HEIGHT - 10
        self.mask = pygame.mask.from_surface(self.ship_img)

    def update(self):
        pass

# Player Space Ship
PLAYER_SHIP = pygame.image.load(os.path.join("assets", "playership.png"))

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

#   def shoot(self):
#      if self.cool_down_counter == 0:
#            laser = Laser(x, y, self.laser_img)
#            self.lasers.append(laser)
#            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SHIP
#        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health    

    player_vel = 7

    player = Player(325, 650)


#Game Controls
            
    # keys = pygame.key.get_pressed()

    #     if keys[pygame.K_a] and player.x - player_vel > 0:
    #        player.x -= player_vel
    #     if keys[pygame.K_d] and player.x + player_vel + player.get_width() < SCREEN_WIDTH:
    #        player.x += player_vel
    #     if keys[pygame.K_w] and player.y - player_vel > 0:
    #        player.y -= player_vel 
    #     if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
    #        player.y += player_vel