import pygame
from lib.button import Button
from lib.game import Game
from lib.screens import Screen

pygame.init()

# Background Music (Rhandell)
pygame.mixer.music.load("assets/bgm.mp3")
pygame.mixer.music.play(-1)

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()

# game variables Start menu (Rob)
start_menu = True
start_menu_main = "main"

# Load button images (Rob)
start_img = pygame.image.load('images/SnorcyStartButton.png').convert_alpha()
exit_img = pygame.image.load('images/SnorcyExitButton.png').convert_alpha()
tutorial_image = pygame.image.load(
    "images/SnorcyTutorialButton.png").convert_alpha()
back_image = pygame.image.load("images/SnorcyBackButton.png").convert_alpha()
arrowkeys_image = pygame.image.load("images/arrows.png").convert_alpha()

# Caption and icon (Rob)
pygame.display.set_caption("Snorcy: Shooter Game")
icon = pygame.image.load('images/Snow1.png').convert()
pygame.display.set_icon(icon)

# Title Game (Rob)
font = pygame.font.Font('assets/Pixeltype.ttf', 120)
title_surface = font.render('The Return of Thanos', False, (219, 13, 13))
title_rect = title_surface.get_rect(midtop=(400, 110))

# Text Tutorial (Rob)
font_tutorial = pygame.font.Font('assets/Pixeltype.ttf', 60)
tutorial_text_surface = font_tutorial.render(
    "Welcome to our game.", False, (252, 194, 3))
tutorial_rect = tutorial_text_surface.get_rect(center=(400, 60))
font_tutorial_explain = pygame.font.Font('assets/Pixeltype.ttf', 35)
arrow_text_surface = font_tutorial_explain.render(
    "To Move Around Use The Arrowkeys Or W.A.S.D.", False, (255, 255, 255))
arrow_rect = arrow_text_surface.get_rect(center=(400, 240))
spacebar_text_surface = font_tutorial_explain.render(
    "To Shoot Lasers Use Your Spacebar", False, (255, 255, 255))
spacebar_text_rect = spacebar_text_surface.get_rect(center=(400, 375))
tutorial1 = font_tutorial_explain.render(
    "In This Game You Have One Minute To Eliminate The Aliens'.", False, (252, 194, 3))
tutorial1_rect = tutorial1.get_rect(center=(400, 100))
tutorial2 = font_tutorial_explain.render(
    "If You Have Survived For One Minute, You Have Won!", False, (252, 194, 3))
tutorial2_rect = tutorial2.get_rect(center=(400, 130))
tutorial3 = font_tutorial_explain.render(
    "You Only Have Five Lives So Be Carfull!", False, (252, 194, 3))
tutorial3_rect = tutorial3.get_rect(center=(400, 160))
tutorial4 = font_tutorial_explain.render(
    "If You Get Hit By A Astroid Or A Alien Get Through One Life Will Be Earesd.", False, (252, 194, 3))
tutorial4_rect = tutorial4.get_rect(center=(400, 190))
tutorial5 = font_tutorial_explain.render(
    "We Hope You Will Enjoy Our Game!", False, (252, 194, 3))
tutorial5_rect = tutorial5.get_rect(center=(400, 490))
tutorial6 = font_tutorial_explain.render("GOOD LUCK!", False, (252, 194, 3))
tutorial6_rect = tutorial6.get_rect(center=(400, 520))

# Images Tutorial
arrowkeys_image = pygame.image.load("images/arrows2.png").convert_alpha()
arrowkeys_rect = arrowkeys_image.get_rect(center=(400, 300))
spacebar_image = pygame.image.load("images/spacebar2.png").convert_alpha()
spacebar_rect = spacebar_image.get_rect(center=(400, 420))

# pause menu (Rob)
font_pause = pygame.font.Font('assets/Pixeltype.ttf', 30)
pause_text_surface = font_pause.render(
    "Press Esc to pause", False, (252, 194, 3))
pause_rect = pause_text_surface.get_rect(
    center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

# Create button instances (Rob)
start_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)
exit_button = Button(SCREEN_WIDTH/2, 280, exit_img, 1)
restart_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)
tutorial_button = Button(-2, 5, tutorial_image, 1)
back_button = Button(795 - 105, 595 - 62, back_image, 0.8)

destroyed = False

running = True
game_start = False
game_finish = False
game_lose = False

game = Game()
screens = Screen(game.time, game.points, game.lives)

while running:

    if start_menu == True:
        screen.fill((83, 41, 42))
        if start_menu_main == "main":
            screen.blit(title_surface, title_rect)
            if exit_button.draw(screen):
                running = False
            if tutorial_button.draw(screen):
                start_menu_main = "tutorial"
            if start_button.draw(screen):
                start_menu = False
                game_start = True
        if start_menu_main == "tutorial":
            screen.blit(arrowkeys_image, arrowkeys_rect)
            screen.blit(tutorial_text_surface, tutorial_rect)
            screen.blit(arrow_text_surface, arrow_rect)
            screen.blit(spacebar_image, spacebar_rect)
            screen.blit(spacebar_text_surface, spacebar_text_rect)
            screen.blit(tutorial1, tutorial1_rect)
            screen.blit(tutorial2, tutorial2_rect)
            screen.blit(tutorial3, tutorial3_rect)
            screen.blit(tutorial4, tutorial4_rect)
            screen.blit(tutorial5, tutorial5_rect)
            screen.blit(tutorial6, tutorial6_rect)
            if back_button.draw(screen):
                start_menu_main = "main"
    if game_start:

        game.run()

        if game.time == 0:
            game_start = False
            game_finish = True
        if game.lives == 0:
            game_start = False
            game_lose = True

    if game_lose:
        screens.losing_screen(game_start, game_finish, running)
    if game_finish:
        screens.winning_screen(game_start, game_finish, running)
        # screen.fill((83, 41, 42))
        # screen.blit(title_surface, title_rect)
        # if restart_button.draw(screen):
        #     game_start = True
        #     time = 60
        #     lives = 5
        #     points = 0
        #     game_finish = False
        # if exit_button.draw(screen):
        #     running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # Respawns enemies every 7.5 seconds (Niels)
            game.create_multiple_enemies(2, 2, 2)
        if event.type == pygame.USEREVENT and start_menu == False:
            time_label = font.render(f"Time: {game.time}", 1, (255, 255, 255))
            game.time -= 1

    # Puts game on 60fps (Niels)
    clock.tick(60)

    # Update the screen (Niels)
    pygame.display.update()

pygame.quit()
