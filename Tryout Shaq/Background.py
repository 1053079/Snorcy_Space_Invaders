import pygame

pygame.init()

#Width And Height Of Screen
WIDTH = 600
HEIGHT = 600

#Display Settings
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Background")

#Display Background Image
background = pygame.image.load('Tryout Shaq/Images/Galaxy2_Smaller.png')
overlap = pygame.image.load('Tryout Shaq/Images/Galaxy2_Smaller.png')

#Position 1st And 2nd Background Image
b_pos = 0
o_pos = -600

#Speed Automatic Scroller
speed = 0.5

#Rotate The Image With Degrees
background = pygame.transform.rotate(background, 90)
overlap = pygame.transform.rotate(overlap, 90)

#Default Value For Level & Lives
level = 1
lives = 5

#Font for text
font = pygame.font.SysFont("Showcard Gothic", 30)

#Draw Text
lives_label = font.render(f"Lives: {lives}", 1, (255, 255, 255))
level_label = font.render(f"Level: {level}", 1, (255, 255, 255))

running = True

#Game Loop
while running:
    if b_pos >= +HEIGHT:
        b_pos = -HEIGHT
    if o_pos >= +HEIGHT:
        o_pos = -HEIGHT

    b_pos += speed
    o_pos += speed

    screen.blit(background, (0, b_pos))
    screen.blit(overlap, (0, o_pos))

    screen.blit(lives_label, (10, 50))
    screen.blit(level_label, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()