import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

moving_rect = pygame.Rect(350, 250, 50, 50)
x_speed, y_speed = 5, 4

other_rect = pygame.Rect(300, 400, 300, 50)
other_speed = 2


def bouncing_rect():
    global x_speed, y_speed, other_speed

    moving_rect.x += x_speed
    moving_rect.y += y_speed

    # Collision with screen borders
    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
        y_speed *= -1

    # Moving the other rect
    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_speed *= -1

    # Collision with rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1

    pygame.draw.rect(screen, (255, 255, 255), moving_rect)
    pygame.draw.rect(screen, (255, 0, 0), other_rect)


running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
