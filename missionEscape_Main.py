import pygame
from parameters import *
from alien import aliens
from bullet import bullets
from cow import Cow
pygame.init()



###make cow





#class Objects():
 #   def __init__(self, scr):
      #  self.object_x = scr_wid
       # self.object_y = scr_hgt

#class Score():
 #   def __init__(self, scr):
  #      self.points = 0
       # self.lives = 3
   #     self.ammo = 10



mr_cow = Cow()
#alien_list = []
#bullets = pygame.sprite.Group()
#for i in range(5):
 #   bullets.add(Bullet())
    #need to relate bullets to bullet_list
### change #of aliens based on level &&& their speed!
#for i in range(0,8):
 #   alien_list.append(Alien('001'))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet.rect.x = mr_cow.cow_rect.x
                bullet.rect.y = mr_cow.cow_rect.y
                bullets.add(bullet)
    for bullet in bullets:
        hit = pygame.sprite.spritecollide(bullet,aliens,True)
        for alien in hit:
            bullets.remove(bullet)
            fired += 1
            score += 1
            print(fired)
            print(score)





    ######why blit after updating x, does this matter?

    make_background(background)
    scr.blit(background, (0, 0))
    mr_cow.move(scr, events)

    create_aliens(8)
    aliens.alien_move()
    hit = pygame.sprite.spritecollide(bullets,aliens)
    if hit:
        pygame.sprite.groupcollide(aliens, bullets, dokilla=True, dokillb=True)
        #update score
    captured = pygame.sprite.spritecollide(mr_cow, aliens)
    if captured:
        #update lives
        lives = -1
    bullets.update()
    aliens.alien_draw(scr)
    mr_cow.cow_draw(scr)
    bullets.bullet_draw(scr)




    print('After.')
###need to move splash screen
    #make_splash_screen(background, scr)


    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()


print('End of line')