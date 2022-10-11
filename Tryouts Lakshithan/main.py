from tkinter import W
import pygame
import os

pygame.init()

pygame.display.set_caption("SNORCY")

#window, color, variabels
Width = 800
Height = 600
WIN = pygame.display.set_mode((Width, Height),)
BLACK = (0, 0, 0)
spaceshipWidth = 30
spaceshipHeight = 30
velocity = 3
laser_Speed = 6
bullet_list = [ ]

#loading images
playerImg = pygame.image.load((os.path.join('Tryouts Lakshithan', 'Assets', 'spaceship.png')))
scaled_PlayerImg = pygame.transform.scale(playerImg,(spaceshipWidth, spaceshipHeight))
laserImg = pygame.image.load((os.path.join('Tryouts Lakshithan', 'Assets', 'Laserbeam.png')))
scaled_laserImg = pygame.transform.scale(laserImg,(10, 10))
background = pygame.image.load(os.path.join('Tryouts Lakshithan','Assets', 'BACKGROUND.png'))
#scaled_background = pygame.transform.scale(laserImg(Width, Height))


class Lasers(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_laserImg
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self):
        self.rect.y -= 5

        if self.rect.x >= Width + 200:
            self.kill()
    

def draw_window(player):
    WIN.fill(BLACK)
    WIN.blit(scaled_PlayerImg,(player.x, player.y))
    pygame.display.update()
    


def main():
    player = pygame.Rect(100, 500, spaceshipWidth, spaceshipHeight)

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #player.x += 2
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            player.x -= velocity
        if keys_pressed[pygame.K_d]:
            player.x += velocity
        if keys_pressed[pygame.K_w]:
            player.y -= velocity
        if keys_pressed[pygame.K_s]:
            player.y += velocity
            
        if keys_pressed[pygame.K_SPACE]:
            bullet_list.append([player.x + 15, player.y - 20])



        

        draw_window(player)

        for bullet in bullet_list:
            pygame.draw.rect(WIN, (100, 100, 0),
                        [*bullet, 20, 20])
            bullet[1] -= 5

        for bullet in bullet_list[:]:
            if bullet[1] < 0:
                bullet_list.remove(bullet)
        pygame.display.update()
    pygame.QUIT



if __name__ == "__main__":
    main()