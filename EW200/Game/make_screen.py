import pygame

#initialize pygame
pygame.init()

print('hi')

#screen dimensions
screen_width = 800
screen_height = 600

#colors
blue = (0,0,225)
brown = (139,69,19)

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen with blue
    screen.fill(blue)

    #draw the brown rectangle at the bottom
    rectangle_height = 180
    pygame.draw.rect(screen, brown, (0,screen_height - rectangle_height, screen_width, rectangle_height))

    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()


print('End of line')