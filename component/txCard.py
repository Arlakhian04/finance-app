import pygame

class Card:
    def __init__(self, index, sign, value, date, name):
        self.index = index
        self.sign = sign
        self.value = value
        self.date = date
        self.name = name

def displayCard(pygame,screen,x,y):
    card = pygame.Rect((x,y,200,50))
    pygame.draw.rect(screen,(0,0,0),card,2,10)