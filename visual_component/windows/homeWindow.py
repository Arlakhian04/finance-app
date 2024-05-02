from visual_component.elements.addTransactionButton import buildingAddTransacButton
from visual_component.transactionElement.portfolioCard import PortfolioCard
from visual_component.elements.footer import buildFooter
from visual_component.elements.header import buildHeader
import numpy as np
class homeWindow:
    def __init__(self,width,height,transacButton,portfolio_array,footer,header,display_index):
        self.width = width
        self.height = height
        self.transacButton = transacButton
        self.portfolio_array = portfolio_array
        self.display_index = display_index
        self.footer = footer
        self.header = header

    def display(self,pygame,screen):
        self.transacButton.displayButton(pygame,screen)
        self.displayCards(pygame,screen)
    
    def displayCards(self,pygame,screen):
        for i in range(6):
            self.portfolio_array[i].displayPortfolioCard(pygame,screen)

    def mouseCollideCards(self,mouse_position):
        for card in self.portfolio_array:
            if card.isDisplayed:
                index = card.mouseCollide(mouse_position)
                if index != -1:
                    return index
            
        return -1

    def resize(self,width,height):
        scale_X = width / self.width
        scale_Y = height / self.height
        self.width = width
        self.height = height

def build(width,height):
    """

    Args:
        width (int): width of the window
        height (int): height of the window
        footer_height (int): height of the footer
        header_height (int): height of the header

    Returns:
        an object of type homeWindow
    """
    footer_width = width
    footer_height = int(max(height / 100 * 10,20))
    footer_border_thickness = 1
    footer = buildFooter(footer_width,footer_height,footer_border_thickness,0,height - footer_height)
    header_height = int(max(height / 100 * 3, 7))
    header_width = width
    header = buildHeader(header_width,header_height,0,0)
    number_cards = 6
    portfolio_card_array = np.empty(number_cards,dtype = object)
    portfolio_card_width = int(width / 100 * 40)
    portfolio_card_height = int(height / 100 * 25)
    padding = 20
    card_y = 2 * padding + header_height
    previousY = 0
    display = True
    display_index = np.empty(6)
    for i in range(number_cards):
        card_x = width / 2 - portfolio_card_width / 2
        portfolio_card_array[i] = PortfolioCard(portfolio_card_width, portfolio_card_height, 
                                                            card_x,card_y,previousY,i,display,(0,0,0),(192,192,192), modified= False)
        if display:
            display_index[i] = i
        if (display and ((previousY + portfolio_card_height) >= (height - footer_height))):
            display = False
        previousY = card_y
        card_y += portfolio_card_array[i].height + padding

    transacButton = buildingAddTransacButton(width,height,footer_height)
    return homeWindow(width=width,height=height,transacButton=transacButton,portfolio_array=portfolio_card_array,footer=footer,header=header,display_index=display_index)