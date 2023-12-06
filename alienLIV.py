from parameters import *



class AlienLIV(pygame.sprite.Sprite):
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
        self.alien_speed = 12
        self.rect.center = (x, y)

    def update(self):
        #self.x -= self.alien_speed
        #self.y = math.sin(self.x)*100
        #self.rect.x = self.x

        #t = pygame.time.get_ticks()  # scale and loop time
        #self.x = t
       # self.y = math.sin(t/100) * 250 + 300 # scale sine wave
       # self.y = int(self.y)  # needs to be int
       # self.rect.y = self.y
        self.x -= self.alien_speed
        self.rect.x = self.x

    def draw(self, scr):
        scr.blit(self.image, self.rect)


#make sprite group
aliensLIV = pygame.sprite.Group()







