import pygame

from parameters import *
import random


class AlienLII(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        alien_img = f'kenney_space-shooter-extension/PNG/Sprites/Station/spaceStation_001.png'

        self.image = pygame.image.load(alien_img).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # set to end of screen so they "fly in"
        self.x = x
        # randomize
        self.y = y

        # just initizalization of speed will level up and get faster
        self.alien_speed = 6
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.alien_speed
        self.rect.x = self.x

    def draw(self, scr):
        scr.blit(self.image, self.rect)

aliensLII = pygame.sprite.Group()







