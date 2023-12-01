import pygame
#import cow?????
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.bullet_speed = 2
        self.bullet_x = x
        self.space_bar = 'not  pressed'
        self.bullet_y = y
        bullet_img = 'kenney_alien-ufo-pack/PNG/laserBlue1.png'
        self.bullet = pygame.image.load(bullet_img).convert()
        #self.bullet_x = self.cow_x
        #self.bullet_y = self.cow_y
       # self.bullet_speed = scr.get_width() / (10 * 50)
        self.bullet_list = []
    #def make_bullet(self,num):
     #   for _ in range(num):
      #      bullets.add(Bullet())



    def show_bullet(self, scr, events):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space_bar = 'pressed'
                    self.bullet_y = mr_cow.cow_y
                    self.bullet_list.append('bullet')




        if self.space_bar == 'pressed':
        #need to check that there are bullets left to fire
            if len(bullets)>0:
                self.bullet_x += self.bullet_speed
                scr.blit(self.bullet, (self.bullet_x, self.bullet_y))
            ######why blit after updating x, does this matter?
                self.bullet_list.pop()


bullets = pygame.sprite.Group()
