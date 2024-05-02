import pygame
from pygame import gfxdraw
import numpy as np

from visual_component.transactionElement import txCard
from visual_component.elements import footer
from visual_component.elements import addTransactionButton
from visual_component.elements.addTransactionButton import buildingAddTransacButton
from visual_component.transactionElement import portfolioCard
from visual_component.transactionElement.portfolioCard import PortfolioCard
from visual_component.windows import homeBackgroundWindow
from visual_component.windows.homeBackgroundWindow import buildBackground
from visual_component.windows import homeWindow
from visual_component.windows.homeWindow import build


pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('Finance APP')

background = buildBackground(SCREEN_WIDTH,SCREEN_HEIGHT,(0,0,0))
home = build(SCREEN_WIDTH,SCREEN_HEIGHT,background.footer_height,background.header_height)

#Useful variable
run = True
start_time = pygame.time.get_ticks()
color = (255,255,255)


while run:
    #Screen reset
    screen.fill(color) 

    #Displaying elements
    home.display(pygame,screen)
    background.displayBackground(pygame,screen)
    transacButton = home.transacButton
     
    #Key event handler
    key = pygame.key.get_pressed()
    if key[pygame.K_t] and (pygame.time.get_ticks() - start_time > 2000):
        transacButton.setHovered(not transacButton.hovered)
        start_time = pygame.time.get_ticks()
    
    #Quit handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            index = home.mouseCollideCards(mouse_position)
            home = build(SCREEN_WIDTH,SCREEN_HEIGHT,background.footer_height,background.header_height)

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            SCREEN_HEIGHT = screen.get_height()
            SCREEN_WIDTH = screen.get_width()
            background = buildBackground(SCREEN_WIDTH,SCREEN_HEIGHT,(0,0,0))
            home = build(SCREEN_WIDTH,SCREEN_HEIGHT,background.footer_height,background.header_height) #Faire setter pour la height et width de chaque element pour pas avoir à tout rebuild à chaque fois
            portfolio_card_width = int(SCREEN_WIDTH / 100 * 40) 
            portfolio_card_height = int(SCREEN_HEIGHT / 100 * 25)
            previousY = 0

    pygame.display.update()

pygame.quit()