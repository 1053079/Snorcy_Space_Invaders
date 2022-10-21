import pygame

class Pause:
    def __init__(self,screen,Button):
        self.paused = True
        # Load button images (Rob)
        resume_image = pygame.image.load("assets/img/button_resume.png").convert_alpha()
        quit_image = pygame.image.load("assets/img/button_quit.png").convert_alpha()

        # Create button instances (Rob)
        resume_button = Button(400 - 95.5, 155, resume_image, 1)
        quit_button = Button(400 - 95.5, 355, quit_image, 1)

        # the loop for pausing
        while self.paused:
            if resume_button.draw(screen):
                self.paused = False
            if quit_button.draw(screen):
                pygame.quit()
                quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False
            pygame.display.update()