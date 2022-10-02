import math
import random

import pygame
from pygame import mixer
from pygame.surface import Surface, SurfaceType

# initialise the game
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))


# background
background = pygame.image.load('background.png')

# caption and icon
pygame.display.set_caption("poultry farm")
icon = pygame.image.load('farm tool.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('farmer.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
enemyImg = pygame.image.load('fox.png')
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 0.4
enemyY_change = 40
num_of_enemies = 6


def player(x, y):
    screen.blit(playerimg, (x, y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

 # Game loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # this is a event of keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.type == pygame.KEYUP:
                if event.key != pygame.K_LEFT or event.key != pygame.K_RIGHT:
                     playerX_change = 0

    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    enemyX+=enemyX_change
    if enemyX<=0:
        enemyX_change=0.4
        enemyY+=enemyY_change
    if enemyX>=736:
        enemyX_change=-0.4
        enemyY+=enemyY_change


    player(playerx, playery)
    enemy(enemyX, enemyY)
    pygame.display.update()