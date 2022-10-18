import pygame
from lib.button import Button
from lib.game import Game

pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load button images (Rob)
start_img = pygame.image.load(
    'assets/img/SnorcyStartButton.png').convert_alpha()
exit_img = pygame.image.load('assets/img/SnorcyExitButton.png').convert_alpha()
tutorial_image = pygame.image.load(
    "assets/img/SnorcyTutorialButton.png").convert_alpha()
back_image = pygame.image.load(
    "assets/img/SnorcyBackButton.png").convert_alpha()
arrowkeys_image = pygame.image.load(
    "assets/img/SnorcyArrowButton.png").convert_alpha()

# Create button instances (Rob)
start_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)
exit_button = Button(SCREEN_WIDTH/2, 280, exit_img, 1)
restart_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)
tutorial_button = Button(-2, 5, tutorial_image, 1)
back_button = Button(795 - 105, 595 - 62, back_image, 0.8)

font = pygame.font.Font('assets/font/Monocraft.otf', 64)

# Title Game (Rob)
title_surface = font.render('Invaders of Snorcy', False, (219, 13, 13))
title_rect = title_surface.get_rect(midtop=(400, 110))

game = Game()


class Screen():
    def __init__(self):
        pass

    def start_screen():
        # game variables Start menu (Rob)
        start_menu = True
        start_menu_main = "main"

        # Text Tutorial (Rob)
        font_tutorial = pygame.font.Font('assets/font/Pixeltype.ttf', 60)
        tutorial_text_surface = font_tutorial.render(
            "Welcome To Our Game.", False, (252, 194, 3))
        tutorial_rect = tutorial_text_surface.get_rect(center=(400, 60))
        font_tutorial_explain = pygame.font.Font(
            'assets/font/Pixeltype.ttf', 35)
        arrow_text_surface = font_tutorial_explain.render(
            "To Move Around Use W.A.S.D.", False, (255, 255, 255))
        arrow_rect = arrow_text_surface.get_rect(center=(400, 240))
        spacebar_text_surface = font_tutorial_explain.render(
            "To Shoot Lasers Use Your Spacebar", False, (255, 255, 255))
        spacebar_text_rect = spacebar_text_surface.get_rect(center=(400, 375))
        tutorial1 = font_tutorial_explain.render(
            "In This Game You Have One Minute To Eliminate The Aliens.", False, (252, 194, 3))
        tutorial1_rect = tutorial1.get_rect(center=(400, 100))
        tutorial2 = font_tutorial_explain.render(
            "If You Have Survived For One Minute, You Have Won!", False, (252, 194, 3))
        tutorial2_rect = tutorial2.get_rect(center=(400, 130))
        tutorial3 = font_tutorial_explain.render(
            "You Only Have Five Lives So Be Careful!", False, (252, 194, 3))
        tutorial3_rect = tutorial3.get_rect(center=(400, 160))
        tutorial4 = font_tutorial_explain.render(
            "If You Get Hit By An Asteroid Or An Alien Gets Through, One Life Will Be Erased.", False, (252, 194, 3))
        tutorial4_rect = tutorial4.get_rect(center=(400, 190))
        tutorial5 = font_tutorial_explain.render(
            "We Hope You Will Enjoy Our Game!", False, (252, 194, 3))
        tutorial5_rect = tutorial5.get_rect(center=(400, 490))
        tutorial6 = font_tutorial_explain.render(
            "GOOD LUCK!", False, (252, 194, 3))
        tutorial6_rect = tutorial6.get_rect(center=(400, 520))

        # Images Tutorial
        arrowkeys_image = pygame.image.load(
            "assets/img/SnorcyArrowButton.png").convert_alpha()
        arrowkeys_rect = arrowkeys_image.get_rect(center=(400, 300))
        spacebar_image = pygame.image.load(
            "assets/img/SnorcySpaceButton.png").convert_alpha()
        spacebar_rect = spacebar_image.get_rect(center=(400, 420))

        # Background image
        background_menu = pygame.image.load(
            "assets/img/SnorcyMenu.png").convert()

        # Title Game (Rob)
        font = pygame.font.Font('assets/font/Pixeltype.ttf', 120)
        title_surface = font.render(
            'The Return of Thanos', False, (219, 13, 13))
        title_rect = title_surface.get_rect(midtop=(400, 110))

        screen.blit(background_menu, (0, 0))
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

    def winning_screen(self, game_start, game_won, running):
        game_start = game_start
        game_won = game_won
        running = running

        # Title game won (Niels)
        title_win_1 = font.render('You Have Won!', False, (219, 13, 13))
        title_win_1_rect = title_surface.get_rect(center=(550, 120))
        title_win_2 = font.render('Congratulations!', False, (219, 13, 13))
        title_win_2_rect = title_surface.get_rect(center=(500, 225))

        screen.fill((83, 41, 42))
        screen.blit(title_win_1, title_win_1_rect)
        screen.blit(title_win_2, title_win_2_rect)
        if restart_button.draw(screen):
            game_start = True
            # print('yes', game_start)
            game.time = 60
            game.lives = 5
            game.points = 0
            game_won = False

            return game_start, game_won
        if exit_button.draw(screen):
            print('also')
            running = False

            return running

    def losing_screen(self, game_start, game_lose, running):
        game_start = game_start
        game_lose = game_lose
        running = running

        # Title game lost (Niels)
        title_lose_1 = font.render('You Have Lost!', False, (219, 13, 13))
        title_lose_1_rect = title_surface.get_rect(center=(550, 130))
        title_lose_2 = font.render('Try Again', False, (219, 13, 13))
        title_lose_2_rect = title_surface.get_rect(center=(650, 215))

        screen.fill((83, 41, 42))
        screen.blit(title_lose_1, title_lose_1_rect)
        screen.blit(title_lose_2, title_lose_2_rect)

        if restart_button.draw(screen):
            print('yes')
            game_start = True
            game.time = 60
            game.lives = 5
            game.points = 0
            game_lose = False

            return game_start, game_lose

        if exit_button.draw(screen):
            print('also')
            running = False

            return running
