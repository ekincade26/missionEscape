from pygame import mixer
from parameters import *
from alien import aliens
from bullet import bullets
from cow import Cow
from heart import hearts

pygame.init()

level = 1

#make background
make_background(background)
scr.blit(background, (0, 0))
#make splash screen and level one screen
make_splash_screen(background,scr)
make_level1_screen(background,scr)
#make background music
mixer.music.load('Space journey.mp3')
mixer.music.play(-1)
#bg_music = pygame.mixer.Sound('Space journey.mp3')

#make player
mr_cow = Cow(0,300)
#make bonus lives
create_hearts(2, 4000, 6000)
#initailize score HERE
score = 0
#create other game elements
create_aliens(10,1000)
create_aliensLII(12,4000, 5000)
create_aliensLIII(14, 10000,12000)
create_aliensLIV(16, 20000, 24000)
create_aliensLV(30, 40000, 42000)
#need alien list to iterate
enemy_list = [aliens, aliensLII, aliensLIII, aliensLIV, aliensLV]
#game sounds
hurt = mixer.Sound("hurt.wav")
bullet_noise = mixer.Sound("kenney_sci-fi-sounds/Audio/laserRetro_004.ogg")
hit_alien_noise = mixer.Sound("kenney_sci-fi-sounds/Audio/explosionCrunch_000.ogg")
#main game loop
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        #controls for player and bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(mr_cow.x,mr_cow.y)
                #bullet to appear from center of cow, not top
                bullet.rect.x = mr_cow.rect.x + mr_cow.image.get_width()/2
                bullet.rect.y = mr_cow.rect.y + mr_cow.image.get_height()/2
                bullets.add(bullet)
                bullet_noise.play()
            if event.key == pygame.K_UP:
                mr_cow.move_up()
            if event.key == pygame.K_DOWN:
                mr_cow.move_down()
        #stop moving cow
        if event.type == pygame.KEYUP:
            mr_cow.stop()
    make_background(background)
    scr.blit(background, (0, 0))
    #text stuff
    custom_font = pygame.font.Font('kenney_kenney-fonts/Fonts/KenneyFuture.ttf', 30)
    score_text = custom_font.render(f"score:{score}", True, (0, 255, 0))
    lives_text = custom_font.render(f"lives remaining:{lives}", True, (0, 255, 0))
    #show text
    scr.blit(score_text, (scr_wid-score_text.get_width(),0))
    scr.blit(lives_text, (5, 0))


    #update sprites, AKA let them move
    mr_cow.update()
    hearts.update()
    aliens.update()
    aliensLII.update()
    aliensLIII.update()
    aliensLIV.update()
    aliensLV.update()
    bullets.update()

    for bullet in bullets:
        #do not allow bullets to kill aliens prematurely
        if bullet.x <= scr_wid:
            for enemy in enemy_list:
                #check to see if bullet hits enemy
                hit = pygame.sprite.spritecollide(bullet, enemy, True, None)
                #kill aliens that get hit, remove bullet, play noise
                for alien in hit:
                    bullets.remove(bullet)
                    hit_alien_noise.play()
                    score += 1
    for enemy in enemy_list:
        #check to see if enemy abducts cow
        sad = pygame.sprite.spritecollide(mr_cow, enemy, True, None)
        for alien in sad:
            #cow gets hurt
            hurt.play()
            lives -= 1
    #check for collision with bonus life
    newLife = pygame.sprite.spritecollide(mr_cow,hearts,True, None)
    for heart in newLife:
        lives += 1
    #initialize
    total_remaining_aliens = 0
    hidden_aliens = 0
    #count aliens
    for enemy in enemy_list:
        for alien in enemy:
            if alien.x > 0:
                total_remaining_aliens += 1
            if alien.x > scr_wid:
                hidden_aliens += 1

    if total_remaining_aliens == 72 and hidden_aliens == 72:
        make_level2_screen(background, scr)
    if total_remaining_aliens == 60 and hidden_aliens == 60:
        make_level3_screen(background, scr)
    if total_remaining_aliens == 46 and hidden_aliens == 46:
        make_level4_screen(background, scr)
    if total_remaining_aliens == 30 and hidden_aliens == 30:
        make_level5_screen(background, scr)


    #end game checks
    if lives == 0:
        print('game over')
        for enemy in enemy_list:
            for alien in enemy:
                alien.kill()
        for heart in hearts:
            heart.kill()
        mr_cow.x = 100000

        for bullet in bullets:
            bullet.kill()
        #high score file
        with open('highscore.txt', 'r') as score_file:
            e = score_file.readlines()
            highscore = int(e[0])
            if score > highscore:
                with open('highscore.txt','w') as sco_file:
                    sco_file.write(f"{score}")
                    highscore = score
        make_gameover_screen(background,scr,score, highscore)

    if total_remaining_aliens == 0 and lives > 0:
        mr_cow.x = 100000
        for bullet in bullets:
            bullet.kill()
        #high score file
        with open('highscore.txt', 'r') as score_file:
            e = score_file.readlines()
            highscore = int(e[0])
            if score > highscore:
                with open('highscore.txt','w') as sco_file:
                    sco_file.write(f"{score}")
                    highscore = score
        make_winner_screen(background,scr,score,highscore)
    #draw game elements AKA blit them
    hearts.draw(scr)
    aliens.draw(scr)
    aliensLII.draw(scr)
    aliensLIII.draw(scr)
    aliensLIV.draw(scr)
    aliensLV.draw(scr)
    mr_cow.cow_draw(scr)
    bullets.draw(scr)
    #update the display
    pygame.display.flip()
#quit pygame
pygame.quit()