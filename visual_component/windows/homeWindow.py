from visual_component.elements.addTransactionButton import buildingAddTransacButton
from visual_component.transactionElement.portfolioCard import PortfolioCard
import numpy as np
class homeWindow:
    def __init__(self,width,height,transacButton,portfolio_array):
        self.width = width
        self.height = height
        self.transacButton = transacButton
        self.portfolio_array = portfolio_array

    def display(self,pygame,screen,screen_width,screen_height,header_height):
        self.transacButton.displayButton(pygame,screen)
        self.displayCards(pygame,screen,screen_width,screen_height,header_height)

    def getTransacButton(self):
        return self.transacButton
    
    def displayCards(self,pygame,screen,screen_width,screen_height,header_height):
        for i in range(6):
            self.portfolio_array[i].displayPortfolioCard(pygame,screen)

def build(width,height,footer_height,header_height):
    """

    Args:
        width (int): width of the window
        height (int): height of the window
        footer_height (int): height of the footer
        header_height (int): height of the header

    Returns:
        an object of type homeWindow
    """
    number_cards = 6
    portfolio_card_array = np.empty(number_cards,dtype = object)
    portfolio_card_width = int(width / 100 * 40)
    portfolio_card_height = int(height / 100 * 25)
    padding = 20
    card_y = padding + header_height
    previousY = 0
    display = True
    for i in range(number_cards):
        card_x = width / 2 - portfolio_card_width / 2
        portfolio_card_array[i] = PortfolioCard(portfolio_card_width, portfolio_card_height, 
                                                            card_x,card_y,previousY,i,display,(0,0,0),(255,255,255))
        if (display and ((previousY + portfolio_card_height) >= (height - footer_height))):
            display = False
        previousY = card_y
        card_y += portfolio_card_height + padding
        print(display)
    addTransacButton = buildingAddTransacButton(width,height,footer_height)
    return homeWindow(width,height,addTransacButton,portfolio_card_array)