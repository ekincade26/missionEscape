import pygame
import time
import random
pygame.init()
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

    print('SPLASH SCREEN!!!!!!!')
    time.sleep(5)

# Screen dimensions
scr_wid = 1000  # (px)
scr_hgt = 600  # (px)



# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Mission Escape')

#make static background
background = scr.copy()


###make cow
class Cow:
    def __init__(self,scr):
        png = 'cow.png'
        self.cow = pygame.image.load(png).convert()
        #self.cow.set_colorkey((0,0,0)) dont need this, no background of cow png
        ##can i find a crisper cow png?
        self.cow_rect = self.cow.get_rect()
        self.cow_x = 0
        self.cow_y = scr.get_height()/2
        #scr.blit(self.cow, (self.cow_x, self.cow_y)) dont need this here
        self.cow_speed = scr.get_width()/(10*50)
        self.cow_x_dir = 1
        self.cow_y_dir = 1

        bullet_img = 'kenney_alien-ufo-pack/PNG/laserBlue1.png'
        self.bullet = pygame.image.load(bullet_img).convert()
        self.bullet_x = self.cow_x
        self.bullet_y = 0
        self.bullet_speed = 4

        self.space_bar = 'not pressed'

    def move(self, scr, events):
        for event in events:
            #keys
            self.key_up = 'not pressed'
            self.key_down = 'not pressed'
            self.key_right = 'not pressed'
            self.key_left = 'not pressed'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.key_up = 'pressed'
                    #self.fish_y += self.fish_y_spd * self.fish_y_dir
                elif event.key == pygame.K_DOWN:
                    self.key_down = 'pressed'
                elif event.key == pygame.K_RIGHT:
                    self.key_right = 'pressed'
                elif event.key == pygame.K_LEFT:
                    self.key_left = 'pressed'
                #elif to shoot add here?

            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_UP:
                    #self.key_up = 'not pressed'
               # elif event.key == pygame.K_DOWN:
                   # self.key_down = 'not pressed'
        if self.key_up == 'pressed':
            self.cow_y -= self.cow_speed
        elif self.key_down == 'pressed':
            self.cow_y += self.cow_speed
        elif self.key_right == 'pressed':
            self.cow_x += self.cow_speed
        elif self.key_left == 'pressed':
            self.cow_x -= self.cow_speed
        #elif self.key_up == 'pressed' and self.key_right == "pressed":
         #   self.cow_y -= self.cow_speed * self.cow_y_dir
          #  self.cow_x += self.cow_speed * self.cow_x_dir


            #self.fish_img = pygame.transform.flip(self.fish_img, True, False)
        #elif self.key_up == 'not pressed':
         #   self.cow_y += self.cow_speed
        self.update_cow_y = self.cow_y
            #update my fish based on status of my keys
        scr.blit(self.cow, (self.cow_x, self.cow_y))

    def show_bullet(self, scr, events):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space_bar = 'pressed'


        print('this ran')
        if self.space_bar == 'pressed':
            self.bullet_x += self.bullet_speed
            scr.blit(self.bullet, (self.bullet_x, self.update_cow_y))
            self.bullet_y = self.update_cow_y

class Alien(Cow):
    def __init__(self,num,scr):
        super().__init__(scr)
        alien_img = f'kenney_space-shooter-extension/PNG/Sprites/Station/spaceStation_{num}.png'
        self.alien = pygame.image.load(alien_img).convert()
        self.alien.set_colorkey((0,0,0))
        self.alien_rect = self.alien.get_rect()
        #set to end of screen so they "fly in"
        self.alien_x = random.randint(scr_wid, scr_wid+1000)
        #randomize
        self.alien_y = random.randint(0,scr_hgt-self.alien.get_height())
        # scr.blit(self.cow, (self.cow_x, self.cow_y)) dont need this here
        #just initizalization of speed will level up and get faster
        self.alien_speed = 2
        self.alien_x_dir = -1
        self.alien_y_dir = 1
    def alien_move(self,scr):
        self.alien_x -= self.alien_speed
        scr.blit(self.alien, (self.alien_x, self.alien_y))

    def check_for_collisions(self, alien_list):
        alien_rect_list = []

        for alien in alien_list:
            alien_rect_list.append(pygame.Rect(alien.alien_x, alien.alien_y, int(self.alien.get_width()), int(self.alien.get_height())))

        my_rect = pygame.Rect(self.bullet_x, self.bullet_y, int(self.alien.get_width()), int(self.alien.get_height()))

        #check me against the list of rectangles
        indices0 = my_rect.collidelistall(alien_rect_list)

        if len(indices0) > 0:
            print('collision!')
            #pygame.mixer.Sound.play(self.chomp)

        indices0.sort(reverse=True)

        for idx in indices0:
            alien_list.pop(idx)
            #pygame.mixer.Sound.play(self.chomp)

        print(indices0)

class Objects():
    def __init__(self, scr):
        self.object_x = scr_wid
        self.object_y = scr_hgt

class Score():
    def __init__(self, scr):
        self.points = 0
        self.lives = 3
        self.ammo = 10
        


mr_cow = Cow(scr)
#alien_list = [Alien('001',scr), Alien('001',scr)]
#trig = Bullet()
alien_list = []

### change #of aliens based on level &&& their speed!
for i in range(0,8):
    alien_list.append(Alien('001',scr))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    make_background(background)
    scr.blit(background, (0, 0))
    mr_cow.move(scr, events)
    for enemy in alien_list:
        enemy.alien_move(scr)
        enemy.check_for_collisions(alien_list)

    mr_cow.show_bullet(scr, events)



    print('After.')
###need to move splash screen
    #make_splash_screen(background, scr)


    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()


print('End of line')