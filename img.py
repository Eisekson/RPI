
import pygame
from math import pi
from pygame.locals import *
from sys import exit

pygame.init()
size = [ 400, 300 ]
pygame.display.set_caption("gg")
# screen = pygame.display.set_mode(size,FULLSCREEN,32)
screen = pygame.display.set_mode((640, 480), 0, 32)

WHITE = (255,255,255)
GREEN = (0,255,0)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key == 'q'):
                done = True
        if event.type == pygame.QUIT: # If user clicked close
            done= True # Flag that we are done so we exit this loop
    screen.fill(GREEN)
    pygame.draw.line(screen,GREEN, [0,0],[50,30],5)
    pygame.display.flip()


pygame.quit()

# 1.169.213.237

# 1.169.214.131