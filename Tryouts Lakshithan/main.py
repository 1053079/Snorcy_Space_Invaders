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

#loading images
playerImg = pygame.image.load((os.path.join('Tryouts Lakshithan', 'Assets', 'spaceship.png')))
scaled_PlayerImg = pygame.transform.scale(playerImg,(spaceshipWidth, spaceshipHeight))
laserImg = pygame.image.load((os.path.join('Tryouts Lakshithan', 'Assets', 'Laserbeam.png')))
scaled_laserImg = pygame.transform.scale(laserImg,(10, 10))
background = pygame.image.load(os.path.join('Tryouts Lakshithan','Assets', 'BACKGROUND.png'))
#scaled_background = pygame.transform.scale(laserImg(Width, Height))


def draw_window(player):
    WIN.fill(BLACK)
    WIN.blit(scaled_PlayerImg,(player.x, player.y) )
    pygame.display.update()
    

def main():
    player = pygame.Rect(100, 500, spaceshipWidth, spaceshipHeight)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #player.x += 1
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            player.x -= velocity
        if keys_pressed[pygame.K_d]:
            player.x += velocity




        draw_window(player)
    pygame.QUIT


if __name__ == "__main__":
    main()