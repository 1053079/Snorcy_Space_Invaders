
import pygame
import random
import math

# initialize the Game
pygame.init()

sw = 800
sh = 600

# Load images
bg = pygame.image.load('images/background.png')
alienIMG = pygame.image.load('images/ufo.png')
PlayerRocket = pygame.image.load('images/reimu.png')
asteroid32 = pygame.image.load('AsteroidPics/Asteroid32.png')
asteroid64 = pygame.image.load('AsteroidPics/Asteroid64.png')
asteroid128 = pygame.image.load('AsteroidPics/Asteroid128.png')

# Bullet and volume settings
shoot = pygame.mixer.Sound('wav/pew.wav')
bangLargeSound = pygame.mixer.Sound('wav/explosion2.wav')
bangSmallSound = pygame.mixer.Sound('wav/explosion.wav')
shoot.set_volume(.25)
bangLargeSound.set_volume(.25)
bangSmallSound.set_volume(.25)

# Width settings and clock 
pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

# Mechanics
gameover = False
lives = 3
score = 0
rapidFire = False
rfStart = -1
isSoundon = True
highScore = 0

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def move(self):
    self.x += self.xv
    self.y -= self.yv


def updateLocation(self):
     def __init__(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = 0
        elif self.y < -50:
             self.y = sh
        elif self.y > sh + 50:
             self.y = 0

class Bullet(object):
     def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.c * 10

class Player(object):
    def __init__(self):
        self.img = PlayerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw // 2
        self.y = sh // 2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def draw(self, win):
        win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)


class Asteroid(object):
    def __init__(self, rank):
        self.x = sw // 2
        self.y = sh // 2
        self.rank = rank
        if self.rank == 1:
             self.image = asteroid32
        elif self.rank == 2:
            self.image = asteroid64
        else:
            self.image = asteroid128
            self.w = 50 * rank
            self.h = 50 * rank
            self.ranPoint = random.choice([(random.randrange(0, sw-self.w), random.choice([-1 * self.h - 5, sh + 5]),
                                            (random.choice(-1 * self.w - 5, sw + 5)),
                                            random.randrange(0, sh - self.h))])
            self.x, self.y = self.ranPoint
        if  self.x < sw // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        if  self.y < sh // 2:
            self.ydir = 1
        else:
            self.ydir = -1
            self.xvel = self.xdir * random.randrange(1, 3)
            self.yvel = self.ydir * random.randrange(1, 3)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


def redrawGameWindow():
    win.blit(bg, (0, 0))
    font = pygame.font.Font('BungeeSpice.ttf', 64)
    livesText = font.render('Lives' + str(lives), 1, WHITE)
    playAgainText = font.render('Press tab to play again', 1, WHITE)
    scoreText = font.render('Score:' + str(score), 1, WHITE)
    highScoreText = font.render('High Score:' + str(highScore), 1, WHITE)

    player.draw(win)
    for a in Asteroid:
        a.draw(win)

    if gameover:
        win.blit(playAgainText,
                    (sw // 2 - playAgainText.get_width() // 2, sh // 2 - playAgainText.get_height() // 2))
        win.blit(scoreText, (sw - scoreText.get_width() - 25, 25))
        win.blit(livesText, (25, 25))
        win.blit(highScoreText, (sw - highScoreText.get_width() - 25, 35 + scoreText.get_height()))
        pygame.display.update()


bg = pygame.image.load('images/background.png')
alienImg = pygame.image.load('images/ufo.png')
playerRocket = pygame.image.load('images/spaceship.png')
star = pygame.image.load('images/player.png')
asteroid50 = pygame.image.load('AsteroidPics/asteroid32.png')
asteroid100 = pygame.image.load('AsteroidPics/asteroid64.png')
asteroid150 = pygame.image.load('AsteroidPics/asteroid128.png')

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((sw, sh))

clock = pygame.time.Clock()

gameover = False


class Player(object):
    def __init__(self):
        self.img = playerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def draw(self, win):
        #win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)

def redrawGameWindow():
    win.blit(bg, (0,0))
    player.draw(win)
    for a in asteroids:
        a.draw(win)

    pygame.display.update()


player = Player()
asteroids = []
count = 0
run = True
while run:
    clock.tick(60)
    count += 1
    if not gameover:
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,2,3])
            asteroids.append((Asteroid)(ran))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForward()

        for a in asteroids:
            a.x += a.xv
            a.y += a.yv

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


redrawGameWindow()
pygame.quit()
