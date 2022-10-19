import pygame

pygame.init()

red = (0, 0, 255,)
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed = -8):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
    
   
    def update(self):
        self.rect.y += self.speed

