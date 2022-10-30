import pygame
import random


alien4 = pygame.image.load("assets/img/alien4.png")
alien5 = pygame.image.load("assets/img/alien5.png")
alien6 = pygame.image.load("assets/img/alien6.png")
alien7 = pygame.image.load("assets/img/alien7.png")

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Enemy(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        if self.image == 1:
            self.image = alien4
        if self.image == 2:
            self.image = alien5
        else:
            self.image = alien6
                  
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(
            center=(random.randint(32, 600), (random.randint(-100, 0))))
        self.destroyed = False

      
    def move(self):
        self.rect.move_ip(0, random.randint(1,3 ))
        if (self.rect.bottom > 620) or self.destroyed == True:
            self.rect.center = (random.randint(32, 600),
                                (random.randint(-100, 0)))
            self.destroyed = False
    

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    #     self.image = pygame.image.load(f'assets/img/{alien}.png')

    #     # Initial placement
    #     self.pos = [random.randint(
    #         0, (SCREEN_WIDTH - 60)), random.randint(-250, -100)]

    #     self.rect = self.image.get_rect(center=self.pos)
    #     self.old_rect = self.rect.copy()

    #     # Making a list of enemies without self (Niels)
    #     self.obstacles_without_self = []
    #     for obstacle in obstacles:
    #         if obstacle != self:
    #             self.obstacles_without_self.append(obstacle)

    #     # Makes the enemies wait for so many seconds until respawn (Niels)
    #     self.TRIGGER = pygame.USEREVENT + 1
    #     pygame.time.set_timer(self.TRIGGER, 8500)

    # def move(self):
    #     # Function for random movement of enemies (Niels)
    #     # Movement speed randomizer (Niels)
    #     self.vel = random.randint(3, 10) / 2

    #     random_num = random.randint(1, 7)
    #     # Right
    #     if random_num == 1:
    #         self.pos[0] += self.vel
    #     # Left
    #     if random_num == 2:
    #         self.pos[0] -= self.vel
    #     # Down and right
    #     if random_num == 3 or random_num == 4:
    #         self.pos[0] += self.vel
    #         self.pos[1] += self.vel
    #     # Down and right
    #     if random_num == 5 or random_num == 6:
    #         self.pos[0] -= self.vel
    #         self.pos[1] += self.vel

    # def collision(self):
    #     # Function for collision (Niels)
    #     collision_sprite = pygame.sprite.spritecollide(
    #         self, self.obstacles_without_self, False)

    #     if collision_sprite and self.pos[1] <= 0:
    #         self.pos = [random.randint(
    #             -10, (SCREEN_WIDTH - 60)), random.randint(-250, -100)]
    #         self.move()

    # def render(self):
    #     # Function that draws everything on the screen (Niels)
    #     screen.blit(self.image, (self.pos))
    #     self.move()
    #     self.collision()
