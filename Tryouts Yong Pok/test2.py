import pygame

screen = pygame.display.set_mode((800, 600))

class Background():

    def __init__(self):
         self.bg_img = pygame.image.load('images/background.png')
         self.rectBGimg = self.bg_img.get_rect()

         self.bgY1 = 0
         self.bgX1 = 0

         self.bgY2 = self.rectBGimg.height
         self.bgX2 = 0

         self.moving_speed = 5

    def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -=self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height

    def render(self):
        screen.blit(self.bg_img, (self.bgX1, self.bgY1))
        screen.blit(self.bg_img, (self.bgX2, self.bgY2))

