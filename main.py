
from lib.enemy import Enemy
from lib.asteroid import Asteroid
from lib.button import Button


pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()

# Start menu (Rob)
start_menu = True


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load button images (Rob)
start_img = pygame.image.load('images/start-button2.png').convert_alpha()
exit_img = pygame.image.load('images/exit_button.png').convert_alpha()


class Game():
    def __init__(self):
        # Initial enemy spawn (Niels)
        self.create_multiple_enemies(2, 2, 2)

    # Function to spawn multiple enemies 1 (Niels)
    def create_multiple_enemies(self, num_enemy_1, num_enemy_2, num_enemy_3):
        # Push as many enemies 1 in a list (Niels)
        self.enemies_1 = []
        number_of_enemies = num_enemy_1
        for num in range(number_of_enemies):
            self.enemies_1.append(Enemy('alien1'))

        # Push as many enemies 2 in a list (Niels)
        self.enemies_2 = []
        number_of_enemies = num_enemy_2
        for num in range(number_of_enemies):
            self.enemies_2.append(Enemy('alien2'))

        # Push as many enemies 3 in a list (Niels)
        self.enemies_3 = []
        number_of_enemies = num_enemy_3
        for num in range(number_of_enemies):
            self.enemies_3.append(Enemy('alien3'))

    # Function for what the game needs to run (Niels)
    def run(self):
        # Loops through the enemy 1 list and renders the enemies (Niels)
        for enemies in self.enemies_1:
            enemies.render()
        # Loops through the enemy 2 list and renders the enemies (Niels)
        for enemies in self.enemies_2:
            enemies.render()
        # Loops through the enemy 3 list and renders the enemies (Niels)
        for enemies in self.enemies_3:
            enemies.render()


# Create button instances
start_button = button.Button(100, 240, start_img, 1)
exit_button = button.Button(450, 240, exit_img, 1)


game = Game()
running = True

while running:
    screen.fill((BLACK))
    screen.fill((83, 41, 42))

    if start_menu == True:
        if exit_button.draw(screen):
            running = False
        if start_button.draw(screen):
            start_menu = False
    else:

        #     Keybindings (Rhandell)
        #    keys = pygame.key.get_pressed()
        # if keys[pygame.K_a] and player.x - player_vel > 0: # Left
        #    player.x -= player_vel
        # if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # Right
        #    player.x += player_vel
        # if keys[pygame.K_w] and player.y - player_vel > 0: # Up
        #    player.y -= player_vel
        # if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # Down
        #    player.y += player_vel

        game.run()

    # Puts game on 60fps (Niels)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # Respawns enemies every 7.5 seconds (Niels)
            game.create_multiple_enemies(2, 2, 2)

    # Update the screen (Niels)
    pygame.display.update()

pygame.quit()
