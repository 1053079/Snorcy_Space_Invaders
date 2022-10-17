import pygame
from lib.laser import Laser

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player Class


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/playership.png")
        self.rect = self.image.get_rect(midbottom=pos)
        self.vel = 7
        # self.rect.centerx = SCREEN_WIDTH/2
        # self.rect.y = SCREEN_HEIGHT - 10
        # self.mask = pygame.mask.from_surface(self.ship_img)
        # self.cool_down_counter = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def movement(self):
        keys = pygame.key.get_pressed()
        # Left
        if keys[pygame.K_a]:
            self.rect.x -= self.vel
        # Right
        if keys[pygame.K_d]:
            self.rect.x += self.vel
        # Up
        if keys[pygame.K_w]:
            self.rect.y -= self.vel
        # Down
        if keys[pygame.K_s]:
            self.rect.y += self.vel
        # Shoot
        if keys[pygame.K_SPACE]:
            Player.shoot()

    def constraint(self):
        # Constraint left
        if self.rect.left <= 0:
            self.rect.left = 0
        # Constraint right
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        # Constraint top
        if self.rect.top <= 0:
            self.rect.top = 0
        # Constraint bottom
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self):
        # screen.blit(self.image, SCREEN_WIDTH/2)
        self.constraint()
        self.movement()

        # screen.blit(self.ship_img, (self.x, self.y))

    # def cooldown(self):
    #     if self.cool_down_counter >= self.COOLDOWN:
    #         self.cool_down_counter = 0
    #     elif self.cool_down_counter > 0:
    #         self.cool_down_counter += 1

#   def shoot(self):
#      if self.cool_down_counter == 0:
#            laser = Laser(x, y, self.laser_img)
#            self.lasers.append(laser)
#            self.cool_down_counter = 1
