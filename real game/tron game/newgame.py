from sys import exit
import pygame
from pygame.locals import *

pygame.init()

#setting up the screen 
screen_width = 1000
screen_height = 1000
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('platformer')
clock = pygame.time.Clock()

#load images
background = pygame.image.load()
#setting up loop variable
run = True
#main game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()