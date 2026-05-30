import pygame
import random

pygame.init()

# configuration
SCREEN_HEIGHT = 650
SCREEN_WIDTH = 600
PIPE_SPACE = 200

# pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# classes
#class is mod your self
class Bird:
    def __init__(self):
        self.height = SCREEN_HEIGHT / 2
        self.speed = 0
        self.alive = True
    
    def jump(self):
        self.speed = -4.5
    
    def fall(self):
        self.height = self.height + self.speed
        self.speed = self.speed + 0.2
        if self.height < 0 + 20:
            self.alive = False
            self.speed = 0 + 40
            self.height = 0 + 20
        if self.height > 630 - 20:
            self.alive = False
            self.height = 630 - 20

    def draw(self):
        pygame.draw.circle(screen, "yellow", (SCREEN_WIDTH / 3, self.height), 20)

class Pipe:
    def __init__(self, x_position):
        self.height = random.randint(35, SCREEN_HEIGHT - 35 - PIPE_SPACE) 
        self.pos = x_position
    
    def move(self):
        self.pos -= 1.5
        if self.pos < -67:
            self.pos = SCREEN_WIDTH
            self.height = random.randint(35, SCREEN_HEIGHT - 35 - PIPE_SPACE) 

    def draw(self):
        pygame.draw.rect(screen, "#00BE00", (
            self.pos,
            0,
            67, #67!
            self.height
        ))

        pygame.draw.rect(screen, "#00BE00", (
            self.pos,
            self.height + PIPE_SPACE,
            67, #67!
            SCREEN_HEIGHT - self.height - PIPE_SPACE
        ))

# game state
bird = Bird()
pipe1 = Pipe(400)
pipe2 = Pipe(700)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and bird.alive == True:
            bird.jump()
        if event.type == pygame.MOUSEBUTTONDOWN and bird.alive == True:
            bird.jump()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("sky blue") 

    # RENDER YOUR GAME HERE
    bird.draw()
    pipe1.draw()
    pipe2.draw()

    # grass
    pygame.draw.rect(screen, "green", (
        0,
        SCREEN_HEIGHT - 20,
        SCREEN_WIDTH,
        20
    ))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    bird.fall()
    pipe1.move()
    pipe2.move()

pygame.quit()