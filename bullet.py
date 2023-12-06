import pygame
#import cow?????
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        bullet_img = 'kenney_alien-ufo-pack/PNG/laserBlue1.png'
        self.image = pygame.image.load(bullet_img).convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.x += 4
        self.rect.x = self.x
        ### dont want bullet to hit future aliens too early, need to set limit
        #####NEED BLIT??????????
    def draw(self,scr):
        scr.blit(self.image, self.rect)


bullets = pygame.sprite.Group()




