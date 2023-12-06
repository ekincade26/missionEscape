import pygame
import time
from alien import Alien, aliens
from alienLII import AlienLII, aliensLII
from alienLIII import AlienLIII, aliensLIII
from alienLIV import AlienLIV, aliensLIV
from alienLV import AlienLV, aliensLV
from bullet import Bullet, bullets
from heart import Heart, hearts
import random


scr_wid = 1000  # (px)
scr_hgt = 600  # (px)
scr = pygame.display.set_mode((scr_wid, scr_hgt))
fired = 0
lives = 3
PLAYER_SPEED = 4.0
def make_background(surface):

    # load the images
    space = pygame.image.load("space.png").convert()

    #cover screen with water
    for x in range(0,surface.get_width(),space.get_width()):
        for y in range(0,surface.get_height(),space.get_height()):
            surface.blit(space, (x,y))

def make_splash_screen(background,scr):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 80)
    text = custom_font.render("Mission Escape", True, (0, 255, 0))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()
    time.sleep(3)

def make_level1_screen(background,scr):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 100)
    text = custom_font.render("LEVEL 1", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()
    time.sleep(3)

def make_level2_screen(background,scr):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 128)
    text = custom_font.render("LEVEL 2", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()
   # time.sleep(3)

def make_level3_screen(background,scr):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 128)
    text = custom_font.render("LEVEL 3", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()


def make_level4_screen(background,scr):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 128)
    text = custom_font.render("LEVEL 4", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()


def make_level5_screen(background,scr):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 128)
    text = custom_font.render("LEVEL 5", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    # update the display
    pygame.display.flip()



def make_gameover_screen(background,scr,sco,highscore):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 128)
    small = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 80)
    text = custom_font.render("GAME OVER", True, (255, 0, 0))
    score_txt_final = small.render(f"score:{sco}", True, (0, 255, 0))
    hs_txt_final = small.render(f"highcore:{highscore}", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    scr.blit(score_txt_final, (scr.get_width() / 2 - score_txt_final.get_width() / 2,
                               scr.get_height() / 3 + text.get_height() / 2))
    scr.blit(hs_txt_final, (scr.get_width() / 2 - hs_txt_final.get_width() / 2,
                               scr.get_height() / 3 + text.get_height()))
    # update the display
    pygame.display.flip()

def make_winner_screen(background,scr,sco,highscore):
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 128)
    small = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 80)
    text = custom_font.render("YOU WON!", True, (255, 0, 0))
    score_txt_final = small.render(f"score:{sco}", True, (0, 255, 0))
    hs_txt_final = small.render(f"highscore:{highscore}", True, (0, 0, 255))
    scr.blit(background, (0, 0))
    # center the text could need int() around this in some other context
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2,
                    scr.get_height() / 3 - text.get_height() / 2))
    scr.blit(score_txt_final, (scr.get_width() / 2 - score_txt_final.get_width() / 2,
                    scr.get_height() / 3 + text.get_height() / 2))
    scr.blit(hs_txt_final, (scr.get_width() / 2 - hs_txt_final.get_width() / 2,
                            scr.get_height() / 3 + text.get_height()))
    # update the display
    pygame.display.flip()

def create_hearts(num, xo, x):
    for _ in range(num):
        hearts.add(Heart(random.randint(scr_wid+xo, scr_wid+x),random.randint(0, 600)))

def create_aliens(num, x):
    for _ in range(num):
        aliens.add(Alien(random.randint(scr_wid, scr_wid+x),random.randint(0, 600)))
        #19 is hardcoded alien height

def create_aliensLII(num, xo, x):
    for _ in range(num):
        aliensLII.add(AlienLII(random.randint(scr_wid + xo, scr_wid+x),random.randint(0, 600)))

def create_aliensLIII(num, xo, x):
    for _ in range(num):
        aliensLIII.add(AlienLIII(random.randint(scr_wid + xo, scr_wid+x),random.randint(0, 600)))

def create_aliensLIV(num, xo, x):
    for _ in range(num):
        aliensLIV.add(AlienLIV(random.randint(scr_wid + xo, scr_wid+x),random.randint(0, 600)))
def create_aliensLV(num, xo, x):
    for _ in range(num):
        aliensLV.add(AlienLV(random.randint(scr_wid + xo, scr_wid+x),random.randint(0, 600)))
def make_bullet(num):
    for _ in range(num):
        bullets.add(Bullet())
        ######need to make it start at cowwwwww

    print('SPLASH SCREEN!!!!!!!')
    time.sleep(5)

# Screen dimensions




# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Mission Escape')

#make static background
background = scr.copy()
