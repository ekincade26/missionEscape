from parameters import *


class Cow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        png = 'cow.png'
        self.image = pygame.image.load(png)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.y_speed = 0
        self.x_speed = 0


    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def stop(self):
        self.y_speed = 0

    def update(self):
        self.y += self.y_speed
        #set limits to keep cow on the screen
        if self.y < 0:
            self.y = 0
        if self.y > scr_hgt - self.image.get_height():
            self.y = scr_hgt - self.image.get_height()
        self.rect.y = self.y

    def cow_draw(self, scr):
        scr.blit(self.image, (self.x, self.y))