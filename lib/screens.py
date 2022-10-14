import pygame
from lib.button import Button

pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title Game (Rob)
font = pygame.font.Font('assets/Pixeltype.ttf', 120)
title_surface = font.render('The Return of Thanos', False, (219, 13, 13))
title_rect = title_surface.get_rect(midtop=(400, 110))
# Title game won (Niels)
title_win_1 = font.render('You Have Won!', False, (219, 13, 13))
title_win_1_rect = title_surface.get_rect(center=(550, 120))
title_win_2 = font.render('Congratulations!', False, (219, 13, 13))
title_win_2_rect = title_surface.get_rect(center=(500, 225))
# Title game lost (Niels)
title_lose_1 = font.render('You Have Lost!', False, (219, 13, 13))
title_lose_1_rect = title_surface.get_rect(center=(550, 130))
title_lose_2 = font.render('Try Again', False, (219, 13, 13))
title_lose_2_rect = title_surface.get_rect(center=(650, 215))

# Load button images (Rob)
start_img = pygame.image.load('images/SnorcyStartButton.png').convert_alpha()
exit_img = pygame.image.load('images/SnorcyExitButton.png').convert_alpha()

# Create button instances (Rob)
start_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)
exit_button = Button(SCREEN_WIDTH/2, 280, exit_img, 1)
restart_button = Button(SCREEN_WIDTH / 8, 280, start_img, 1)


class Screen():
    def __init__(self, time, points, lives):
        self.time = time
        self.points = points
        self.lives = lives

    def winning_screen(self, game_start, game_finish, running):
        game_start = game_start
        game_finish = game_finish
        running = running

        screen.fill((83, 41, 42))
        screen.blit(title_win_1, title_win_1_rect)
        screen.blit(title_win_2, title_win_2_rect)
        if restart_button.draw(screen):
            game_start = True
            print('yes', game_start)
            self.time = 60
            self.lives = 5
            self.points = 0
            game_finish = False

            return game_start, game_finish
        if exit_button.draw(screen):
            print('also')
            running = False

            return running

    def losing_screen(self, game_start, game_finish, running):
        game_start = game_start
        game_finish = game_finish
        running = running

        screen.fill((83, 41, 42))
        screen.blit(title_lose_1, title_lose_1_rect)
        screen.blit(title_lose_2, title_lose_2_rect)

        if restart_button.draw(screen):
            print('yes')
            game_start = True
            self.time = 60
            self.lives = 5
            self.points = 0
            game_finish = False

            return game_start, game_finish

        if exit_button.draw(screen):
            print('also')
            running = False

            return running
