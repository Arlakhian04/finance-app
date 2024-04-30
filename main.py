import pygame
from pygame import gfxdraw
from component.transactionElement import txCard
from component.elements import footer
from component.elements import addTransactionButton
from component.elements.addTransactionButton import buildingAddTransacButton
from component.windows import homeBackgroundWindow
from component.windows.homeBackgroundWindow import buildBackground
from component.windows import homeWindow
from component.windows.homeWindow import build


pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
testPortfolioCard = pygame.Surface((300,200))
testPortfolioCard.fill((0,0,0))
screen.blit(testPortfolioCard,(300,300))
pygame.display.set_caption('Finance APP')

testCard = txCard.Card(index=0,sign="+",value=0,date=0,name="test",width = 200,height = 75,x = 100,y = 100)
background = buildBackground(SCREEN_WIDTH,SCREEN_HEIGHT,(150,150,150))
#testButton = buildingAddTransacButton(SCREEN_WIDTH=SCREEN_WIDTH,SCREEN_HEIGHT=SCREEN_HEIGHT,footerHeight=background.getFooterHeight())
home = build(SCREEN_WIDTH,SCREEN_HEIGHT,background.getFooterHeight())

#Useful variable
run = True
timer = 0
while run:
    #Screen reset
    screen.fill((255,255,255))
    screen.blit(testPortfolioCard,(300,300))    
    #Displaying elements
    background.displayBackground(pygame,screen)
    testCard.displayCard(pygame,screen)
    home.display(pygame,screen)
    transacButton = home.getTransacButton()

     
    #Key event handler
    key = pygame.key.get_pressed()
    if key[pygame.K_t] and timer >= 300:
        transacButton.setHovered(not transacButton.getHovered())
        timer = 0

    #Quit handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            SCREEN_HEIGHT = screen.get_height()
            SCREEN_WIDTH = screen.get_width()
            background = buildBackground(SCREEN_WIDTH,SCREEN_HEIGHT,(150,150,150))
            #testButton = buildingAddTransacButton(SCREEN_WIDTH=SCREEN_WIDTH,SCREEN_HEIGHT=SCREEN_HEIGHT,footerHeight=background.getFooterHeight())
            home = build(SCREEN_WIDTH,SCREEN_HEIGHT,background.getFooterHeight)

    timer += 1

    pygame.display.update()

pygame.quit()