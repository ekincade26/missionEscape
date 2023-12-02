import pygame
import time
from alien import Alien, aliens
from bullet import Bullet, bullets
import random

scr_wid = 1000  # (px)
scr_hgt = 600  # (px)
fired = 0
score = 0
def make_background(surface):

    # load the images
    space = pygame.image.load("space.png").convert()

    #cover screen with water
    for x in range(0,surface.get_width(),space.get_width()):
        for y in range(0,surface.get_height(),space.get_height()):
             surface.blit(space, (x,y))

def make_splash_screen(background,scr):
    custom_font = pygame.font.Font('Black_crayon.ttf', 128)
    text = custom_font.render("Mission Escape", True, (53, 94, 59))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()

def create_aliens(num):
    for _ in range(num):
        aliens.add(Alien(random.randint(scr_wid, scr_wid+1000),random.randint(0,scr_hgt-19)))
        #19 is hardcoded alien height
def make_bullet(num):
    for _ in range(num):
        bullets.add(Bullet())

    print('SPLASH SCREEN!!!!!!!')
    time.sleep(5)

# Screen dimensions




# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Mission Escape')

#make static background
background = scr.copy()
