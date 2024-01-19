import pygame
import sys
from pygame.locals import *

# initialize Pygame
pygame.init()

# window settings
width = 1380 
height = 800
dispSurf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Oma peli")

transparent = (0,0,0,0)

# load background and images
level = pygame.image.load("space.jpg").convert()
# space image by upklyak on Freepik
bee = pygame.image.load("bee.png").convert_alpha()
# bee image by brgfx on Freepik
beeDirection = bee
rightBee = pygame.transform.flip(bee, True, False)
jellyfish1 = pygame.image.load("jellyfish1.png").convert_alpha()
jellyfish1 = pygame.transform.scale(jellyfish1, (63, 75))
jellyfish2 = pygame.image.load("jellyfish2.png").convert_alpha()
jellyfish2 = pygame.transform.scale(jellyfish2, (70, 75))
# jellyfish images by pch.vector on Freepik

# blit images onto the display surface
dispSurf.blit(level, (0,0))
dispSurf.blit(jellyfish1, (0,0))
dispSurf.blit(jellyfish2, (1000,200))
dispSurf.blit(bee, (500, 100))

pygame.display.flip()

# get rectangles for collision detection
jellyfish1Area = jellyfish1.get_rect()
jellyfish2Area = jellyfish2.get_rect()
beeArea = bee.get_rect()

# set initial positions
beeArea.left = 500
beeArea.top = 100
jellyfish2Area.left = 1000
jellyfish2Area.top = 200

# set speeds and initialize flags for fellyfish death
speed1 = [1,1]
speed2 = [-1,1]
dead1 = False
dead2 = False

# load music (Neptunea by Scanglobe, freemusicarchive.org CC BY-NC-SA) and sounds
pygame.mixer.music.load("Scanglobe_Neptunea.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)
slurp = pygame.mixer.Sound("slurp.mp3")

pygame.display.flip()

# gameplay loop
while True:

    # quitting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit() 

    # move jellyfish
    jellyfish1Area.move_ip(speed1)
    jellyfish2Area.move_ip(speed2)

    # check collisions with bee and make jellyfish disappear when eaten
    if beeArea.colliderect(jellyfish1Area):
        if not dead1:
            pygame.mixer.Sound.play(slurp)
            jellyfish1.fill(transparent)
            dead1 = True

    if beeArea.colliderect(jellyfish2Area):
        if not dead2:
            pygame.mixer.Sound.play(slurp)
            jellyfish2.fill(transparent)
            dead2 = True
            
    # bounce jellyfish off the moving area walls
    if jellyfish1Area.left < -200 or jellyfish1Area.right > width + 200:
        speed1[0] = -speed1[0]
    if jellyfish1Area.top < -200 or jellyfish1Area.bottom > height + 200:
        speed1[1] = -speed1[1]
    if jellyfish2Area.left < -200 or jellyfish2Area.right > width + 200:
        speed2[0] = -speed2[0]
    if jellyfish2Area.top < -200 or jellyfish2Area.bottom > height + 200:
        speed2[1] = -speed2[1]

    # handle key presses for moving the bee
    pressings = pygame.key.get_pressed()
    
    if pressings[K_LEFT]:
        beeDirection = bee
        if beeArea.left < 0:
            beeArea.move_ip((0,0))
        else:
            beeArea.move_ip((-1,0))
        
    if pressings[K_RIGHT]:
        beeDirection = rightBee
        if beeArea.right > width:
            beeArea.move_ip((0,0))
        else:
            beeArea.move_ip((1,0))
        
    if pressings[K_DOWN]:
        if beeArea.bottom > height:
            beeArea.move_ip((0,0))
        else:
            beeArea.move_ip((0,1))
            
    if pressings[K_UP]:
        if beeArea.top < 0:
            beeArea.move_ip((0,0))
        else:
            beeArea.move_ip((0,-1))

    # update the display surface
    dispSurf.blit(level, (0,0))
    dispSurf.blit(jellyfish1, jellyfish1Area)
    dispSurf.blit(jellyfish2, jellyfish2Area)
    dispSurf.blit(beeDirection, beeArea)

    pygame.display.flip()
