import pygame

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
