import pygame

class Pause:
    def __init__(self,screen,Button):
        self.paused = True
        resume_image = pygame.image.load("assets/img/button_resume.png").convert_alpha()
        resume_button = Button(400 - 95.5, 155, resume_image, 1)

        # the loop for pausing
        while self.paused:
            if resume_button.draw(screen):
                start_menu = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False
            pygame.display.update()