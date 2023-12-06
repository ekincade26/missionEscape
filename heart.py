from parameters import *
class Heart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        heart_img = f'heart.png'
        self.x = x
        self.y = y
        self.image = pygame.image.load(heart_img).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dir_y = 1
    def update(self):
        self.x -= 4
        self.rect.x = self.x
        self.y += 2 * self.dir_y
        if self.y < 0:
            self.dir_y = 1
        if self.y > 600 - self.image.get_height():
            self.dir_y = -1
        self.rect.y = self.y


    def draw(self,scr):
        scr.blit(self.image, self.rect)


#create sprite group
hearts = pygame.sprite.Group()