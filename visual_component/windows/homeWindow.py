from visual_component.elements.addTransactionButton import buildingAddTransacButton
from visual_component.transactionElement.portfolioCard import PortfolioCard
import numpy as np
class homeWindow:
    def __init__(self,width,height,transacButton,portfolio_array,display_index):
        self.width = width
        self.height = height
        self.transacButton = transacButton
        self.portfolio_array = portfolio_array
        self.display_index = display_index

    def display(self,pygame,screen):
        self.transacButton.displayButton(pygame,screen)
        self.displayCards(pygame,screen)

    def getTransacButton(self):
        return self.transacButton
    
    def displayCards(self,pygame,screen):
        for i in range(6):
            self.portfolio_array[i].displayPortfolioCard(pygame,screen)

    def modifyCard(self,index):
        #faire un getter pour tous les éléments dûne portfolio card comme ça on peut modifier tous les éléments tout en gardant des bases
        modifying_value = 30
        self.portfolio_array[index] = PortfolioCard(self.portfolio_array[index].width + modifying_value,self.portfolio_array[index].height + modifying_value,
                                                    self.portfolio_array[index].x - int(modifying_value / 2),self.portfolio_array[index].y - int(modifying_value / 2),
                                                    self.portfolio_array[index].previousY,self.portfolio_array[index].index,self.portfolio_array[index].isDisplayed,
                                                    self.portfolio_array[index].color, self.portfolio_array[index].border_color,modified = True)

    def mouseCollideCards(self,mouse_position):
        for card in self.portfolio_array:
            if card.isDisplayed:
                index = card.mouseCollide(mouse_position)
                if index != -1:
                    return index
            
        return -1
        """
        

        Faire une liste avec les index des displayed comme ça pas besoin d itérer sur toute la liste à chaque fois

        """ 
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
        card_y += portfolio_card_height + padding

    addTransacButton = buildingAddTransacButton(width,height,footer_height)
    return homeWindow(width,height,addTransacButton,portfolio_card_array,display_index)