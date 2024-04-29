import pygame
from pygame import gfxdraw
from component.transactionElement import txCard
from component.elements import footer
from component.elements import addTransactionButton
from component.elements.addTransactionButton import buildingAddTransacButton

pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)

pygame.display.set_caption('Finance APP')

player = pygame.Rect((300,250,300,50))
testCard = txCard.Card(index=0,sign="+",value=0,date=0,name="test",width = 200,height = 75,x = 100,y = 100)
footerHeight = 75
testFooter = footer.Footer(SCREEN_WIDTH,footerHeight,(150,150,150),x = 0,y = SCREEN_HEIGHT-footerHeight)
testButton = buildingAddTransacButton(SCREEN_WIDTH=SCREEN_WIDTH,SCREEN_HEIGHT=SCREEN_HEIGHT,footerHeight=footerHeight)

run = True
hover = False
timer = 0
while run:
    #Screen reset
    screen.fill((255,255,255))

    pygame.draw.rect(screen,(255,0,0),player,1,10)

    #Displaying elements
    testCard.displayCard(pygame,screen)
    testFooter.displayFooter(pygame,screen)
    testButton.displayButton(pygame,screen,hover)

     
    #Key event handler
    key = pygame.key.get_pressed()
    if key[pygame.K_t] and timer >= 500:
        hover = not hover
        timer = 0
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)

    #Quit handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            SCREEN_HEIGHT = screen.get_height()
            SCREEN_WIDTH = screen.get_width()
            testFooter = footer.Footer(SCREEN_WIDTH,footerHeight,(150,150,150),x = 0,y = SCREEN_HEIGHT-footerHeight)
            testButton = buildingAddTransacButton(SCREEN_WIDTH=SCREEN_WIDTH,SCREEN_HEIGHT=SCREEN_HEIGHT,footerHeight=footerHeight)
    timer += 1

    pygame.display.update()

pygame.quit()