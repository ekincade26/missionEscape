import pygame
from parameters import *


class Cow(pygame.sprite.Sprite):
    def __init__(self, x=0, y=scr.get_height()/2):
        super().__init__()
        #want to inher from bullet sprite group
        png = 'cow.png'
        self.cow = pygame.image.load(png)
        #self.cow.set_colorkey((0,0,0)) dont need this, no background of cow png
        ##can i find a crisper cow png?
        self.cow_rect = self.cow.get_rect()
        self.cow_rect.center = (x + self.cow.get_width()/2, y)
        self.cow_x = x
        self.cow_y = y
        self.cow_speed = scr.get_width()/(10*50)
        self.cow_x_dir = 1
        self.cow_y_dir = 1
        #self.bullets = bullets
        #self.bullet_speed = bullet_speed
        self.key_up = 'not pressed'
        self.key_down = 'not pressed'
        self.key_right = 'not pressed'
        self.key_left = 'not pressed'
        self.update_cow_y = None





    def move(self, scr, events):
        for event in events:
            #keys
           # self.key_up = 'not pressed'
           # self.key_down = 'not pressed'
           # self.key_right = 'not pressed'
           # self.key_left = 'not pressed'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.key_up = 'pressed'
                elif event.key == pygame.K_DOWN:
                    self.key_down = 'pressed'
                elif event.key == pygame.K_RIGHT:
                    self.key_right = 'pressed'
                elif event.key == pygame.K_LEFT:
                    self.key_left = 'pressed'

        if self.key_up == 'pressed':
            self.cow_y -= self.cow_speed
        elif self.key_down == 'pressed':
            self.cow_y += self.cow_speed
        elif self.key_right == 'pressed':
            self.cow_x += self.cow_speed
        elif self.key_left == 'pressed':
            self.cow_x -= self.cow_speed

        self.update_cow_y = self.cow_y

    def cow_draw(self):
        scr.blit(self.cow, (self.cow_x, self.cow_y))