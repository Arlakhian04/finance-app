import pygame
from component import txCard
from component import footer

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Finance APP')

player = pygame.Rect((300,250,300,50))
testCard = txCard.Card(index=0,sign="+",value=0,date=0,name="test",width = 200,height = 75,x = 100,y = 100)
footerHeight = 75
testFooter = footer.Footer(SCREEN_WIDTH,footerHeight,(150,150,150),x = 0,y = SCREEN_HEIGHT-footerHeight)

run = True

while run:
    screen.fill((255,255,255))

    pygame.draw.rect(screen,(255,0,0),player,1,10)


    testCard.displayCard(pygame,screen)
    testFooter.displayFooter(pygame,screen)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()