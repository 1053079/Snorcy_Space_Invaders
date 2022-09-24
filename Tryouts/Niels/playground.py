import pygame

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY = 169, 169, 169
LIGHT_GREY = 211, 211, 211

# Font
score_font = pygame.font.Font('freesansbold.ttf', 32)
intro_font = pygame.font.Font('freesansbold.ttf', 64)
over_font = pygame.font.Font('freesansbold.ttf', 64)
button_font = pygame.font.Font('freesansbold.ttf', 32)
# Buttons


class Button:
    def __init__(self, text, width, height, pos, elevation, screen, action=None):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_x_position = pos[0]
        self.original_y_position = pos[1]
        self.action = action
        self.screen = screen

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = WHITE

        # Botton rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = LIGHT_GREY

        # Text
        self.text_surf = button_font.render(text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_position - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color,
                         self.bottom_rect, border_radius=10)

        pygame.draw.rect(screen, self.top_color,
                         self.top_rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = GREY
            # Logic so button get pressed once
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = WHITE


button_start = Button('Start', 225, 40, (325, 300), 6, screen, "play")
button_high_score = Button('High Scores', 225, 40,
                           (325, 360), 6, screen, "high_scores")
button_quit = Button('Quit', 225, 40, (325, 420), 6, screen, "quit")


# Start screen loop
def start():
    game_intro = True
    while game_intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((BLACK))
        button_start.draw()
        button_high_score.draw()
        button_quit.draw()
        intro_text = intro_font.render("Space Invader", True, WHITE)
        screen.blit(intro_text, (200, 200))

        pygame.display.update()
