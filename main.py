import pygame
from pygame import gfxdraw
from component.transactionElement import txCard
from component.elements import footer
from component.elements import addTransactionButton
from component.elements.addTransactionButton import buildingAddTransacButton
from component.windows import homeBackgroundWindow
from component.windows.homeBackgroundWindow import buildBackground

pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)

pygame.display.set_caption('Finance APP')

testCard = txCard.Card(index=0,sign="+",value=0,date=0,name="test",width = 200,height = 75,x = 100,y = 100)
background = buildBackground(SCREEN_WIDTH,SCREEN_HEIGHT,(150,150,150))
testButton = buildingAddTransacButton(SCREEN_WIDTH=SCREEN_WIDTH,SCREEN_HEIGHT=SCREEN_HEIGHT,footerHeight=background.getFooterHeight())

#Useful variable
run = True
timer = 0
while run:
    #Screen reset
    screen.fill((255,255,255))

    #Displaying elements
    background.displayBackground(pygame,screen)
    testCard.displayCard(pygame,screen)
    testButton.displayButton(pygame,screen)

     
    #Key event handler
    key = pygame.key.get_pressed()
    if key[pygame.K_t] and timer >= 300:
        testButton.setHovered(not testButton.getHovered())
        timer = 0

    #Quit handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            SCREEN_HEIGHT = screen.get_height()
            SCREEN_WIDTH = screen.get_width()
            background = buildBackground(SCREEN_WIDTH,SCREEN_HEIGHT,(150,150,150))
            testButton = buildingAddTransacButton(SCREEN_WIDTH=SCREEN_WIDTH,SCREEN_HEIGHT=SCREEN_HEIGHT,footerHeight=background.getFooterHeight())

    timer += 1

    pygame.display.update()

pygame.quit()