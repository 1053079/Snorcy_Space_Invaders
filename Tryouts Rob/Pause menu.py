import pygame
import button

pygame.init()

# Create game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNORCY pause Menu")

# game variables
game_paused = False
start_menu_main = "main"

# Define fonts
font = pygame.font.SysFont("arialblack", 40)

# Define colours
text_colour = (255, 255, 255)

# Load button images
resume_image = pygame.image.load("images/button_resume.png").convert_alpha()
quit_image = pygame.image.load("images/button_quit.png").convert_alpha()
turtorial_image = pygame.image.load("images/turtorial2.png").convert_alpha()
back_image = pygame.image.load("images/button_back.png").convert_alpha()

# Create button instances
resume_button = button.Button(304, 125, resume_image, 1)
quit_button = button.Button(336, 375, quit_image, 1)
turtorial_button = button.Button(320, 250, turtorial_image, 1)
back_button = button.Button(320, 250, back_image, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# GAME LOOP
run = True
while run:

    screen.fill((83, 41, 42))

    # Check if game is paused
    if game_paused == True:
        # Check menu state
        if start_menu_main == "main":
            # Draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if turtorial_button.draw(screen):
                start_menu_main = "turtorial"
            if quit_button.draw(screen):
                run = False
        if start_menu_main == "turtorial":
            if back_button.draw(screen):
                start_menu_main = "main"        
    else:
        draw_text("Press ESC to pause", font, text_colour, 180, 250)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
