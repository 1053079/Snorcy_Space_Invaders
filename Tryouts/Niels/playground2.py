from random import random
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)
background = pygame.image.load('Tryouts/Niels/img/background.png')
asteroid = pygame.image.load('Tryouts/Niels/img/asteroid1.png')

# Clock
clock = pygame.time.Clock()


# Asteroid
asteroid_1_img = pygame.image.load('Tryouts/Niels/img/asteroid1.png')
asteroid_1_x = random.randint(0, 300)
asteroid_1_y = random.randint(-75, -5)
asteroid_1_x_speed = 150
asteroid_1_y_speed = 170


counter = random.randint(5, 6)
pygame.time.set_timer(pygame.USEREVENT, 500)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.USEREVENT:
        #     counter -= 1
        #     if counter > 0:
        #         text = str(counter).rjust(3)
        #         print(text)
        #     if counter < 5:
        #         print('now')
            # Asteroid
    # Asteroid
    screen.blit(asteroid_1_img, (asteroid_1_x, asteroid_1_y))
    mili_sec = clock.tick()
    seconds = mili_sec/1000.
    # Astroid movement x direction
    dmx = seconds * asteroid_1_x_speed
    # Asteroid movement y direction
    dmy = seconds * asteroid_1_y_speed

    asteroid_1_x += dmx
    asteroid_1_y += dmy

    pygame.display.update()
