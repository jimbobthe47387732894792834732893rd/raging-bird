import pygame
import random

pygame.init()

# configuration
SCREEN_HEIGHT = 650
SCREEN_WIDTH = 600
PIPE_SPACE = 200
DABIRD_PHOTO = pygame.image.load("ragingbird-photo-bad.png")
DABIRD_HEIGHT = DABIRD_PHOTO.get_height()
DABIRD_X = SCREEN_WIDTH / 3 - DABIRD_HEIGHT * 0.69

# pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# classes
#class is mod your self
class Bird:
    def __init__(self):
        self.y = SCREEN_HEIGHT / 2
        self.speed = 0
        self.alive = True
    
    def jump(self):
        self.speed = -4.5
    
    def fall(self):
        self.y = self.y + self.speed
        self.speed = self.speed + 0.2
        if self.y < 0 + DABIRD_HEIGHT:
            self.alive = False
            self.speed = 0 + 40
            self.y = 0 + DABIRD_HEIGHT
        if self.y > 630 - DABIRD_HEIGHT:
            self.alive = False
            self.y = 630 - DABIRD_HEIGHT

    def draw(self):
        screen.blit(DABIRD_PHOTO, (DABIRD_X, self.y - DABIRD_HEIGHT/2))

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
    
    def is_bird_dead(self, dabird):
        # top pipe
        if (
            DABIRD_X >= self.pos - (DABIRD_HEIGHT * 0.75) * 2 and
            DABIRD_X <= self.pos + 67 and
            dabird.y >= 0 - DABIRD_HEIGHT and
            dabird.y <= 0 + self.height
        ):
            dabird.alive = False
        
        # bottom pipe
        if (
            DABIRD_X >= self.pos - (DABIRD_HEIGHT * 0.75) * 2 and
            DABIRD_X <= self.pos + 67 and
            dabird.y >= self.height + PIPE_SPACE - DABIRD_HEIGHT and
            dabird.y <= self.height + PIPE_SPACE + SCREEN_HEIGHT - self.height - PIPE_SPACE
        ):
            dabird.alive = False

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
    pipe1.draw()
    pipe2.draw()
    bird.draw()

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
    if bird.alive == True:
        pipe1.move()
        pipe2.move()
    pipe1.is_bird_dead(bird)
    pipe2.is_bird_dead(bird)

pygame.quit()