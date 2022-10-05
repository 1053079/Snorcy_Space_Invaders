import pygame
import button

pygame.init()

# Create game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNORCY Main Menu")

# game variables
game_paused = False
menu_state = "main"

# Define fonts
font = pygame.font.SysFont("arialblack", 40)

# Define colours
text_colour = (255, 255, 255)

# Load button images
resume_image = pygame.image.load("images/button_resume.png").convert_alpha()
options_image = pygame.image.load("images/button_options.png").convert_alpha()
quit_image = pygame.image.load("images/button_quit.png").convert_alpha()
video_image = pygame.image.load("images/button_video.png").convert_alpha()
audio_image = pygame.image.load("images/button_audio.png").convert_alpha()
keys_image = pygame.image.load("images/button_keys.png").convert_alpha()
back_image = pygame.image.load("images/button_back.png").convert_alpha()


# Create button instances
resume_button = button.Button(304, 125, resume_image, 1)
options_button = button.Button(297, 250, options_image, 1)
quit_button = button.Button(336, 375, quit_image, 1)
video_button = button.Button(226, 75, video_image, 1)
audio_button = button.Button(225, 200, audio_image, 1)
keys_button = button.Button(246, 325, keys_image, 1)
back_button = button.Button(332, 450, back_image, 1)


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
        if menu_state == "main":
            # Draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        # Check if the options menu is open
        if menu_state == "options":
            # Draw the different options buttons
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
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
