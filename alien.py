import pygame
import random
from parameters import *

class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        alien_img = f'kenney_space-shooter-extension/PNG/Sprites/Station/spaceStation_{num}.png'
        self.alien = pygame.image.load(alien_img).convert()
        self.alien.set_colorkey((0,0,0))
        self.alien_rect = self.alien.get_rect()
        #set to end of screen so they "fly in"
        self.alien_x = x
        #randomize
        self.alien_y = y
        # scr.blit(self.cow, (self.cow_x, self.cow_y)) dont need this here
        #just initizalization of speed will level up and get faster
        self.alien_speed = 2
        self.alien_x_dir = -1
        self.alien_y_dir = 1

    #def create_aliens(self,num):
     #   for _ in range(num):
      #      aliens.add(Alien(random.randint(scr_wid, scr_wid+1000),random.randint(0,scr_hgt-self.alien.get_height())))

    def alien_move(self):
        self.alien_x -= self.alien_speed
    def alien_draw(self,scr):
        scr.blit(self.alien, (self.alien_x, self.alien_y))

   # def check_for_collisions(self, alien_list):
    #    alien_rect_list = []

     #   for alien in alien_list:
      #      alien_rect_list.append(pygame.Rect(alien.alien_x, alien.alien_y, int(self.alien.get_width()), int(self.alien.get_height())))

        #my_rect = pygame.Rect(self.bullet_x, self.bullet_y, int(self.alien.get_width()), int(self.alien.get_height()))

       # my_rect = pygame.Rect(mr_cow.bullet_x, mr_cow.bullet_y, int(self.alien.get_width()), int(self.alien.get_height()))

        #check me against the list of rectangles
        #indices0 = my_rect.collidelistall(alien_rect_list)

      #  if len(indices0) > 0:
       #     print('collision!')
            #pygame.mixer.Sound.play(self.chomp)

       # indices0.sort(reverse=True)

       # for idx in indices0:
        #    alien_list.pop(idx)
            #pygame.mixer.Sound.play(self.chomp)

       # print(indices0)


aliens = pygame.sprite.Group()

