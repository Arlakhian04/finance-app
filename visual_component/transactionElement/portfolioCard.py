#Class to make protfolio card
from visual_component.random import aafilledRoundedRect
from visual_component.random.aafilledRoundedRect import AAfilledRoundedRect
from transaction_constant import PORTFOLIO_CARD_COLOR
from transaction_constant import PORTFOLIO_CARD_BORDER_COLOR
class PortfolioCard:
    def __init__(self,width,height,x,y,previousY,index,isDisplayed,modified):
        """Initialize an object PortfolioCard
        Args:
            width (int): width of the card
            height (int): height of the card
            x (int): position x of the card
            y (int): position y of the card
            previousY (int): position y of the previous card
            index (int): index of the portfolio in portfolio list
            isDisplayed (bool): boolean to indicate if the card should be displayed
            color (tuple): color of the card
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.previousY = previousY
        self.index = index
        self.isDisplayed = isDisplayed
        self.color = PORTFOLIO_CARD_COLOR
        self.border_color = PORTFOLIO_CARD_BORDER_COLOR
        self.modified = modified
    

    def displayPortfolioCard(self,pygame,screen):
        """Display the portfolio card
        Args:
            pygame (pygame): element to use the pygame methods
            screen (pygame.Surface): surface where we display the card
        """
        if self.isDisplayed:
            modifying_value = 30
            border_thickness = 2
            if self.modified:
                new_x = self.x - int(modifying_value / 2)
                new_y = self.y
                new_width = self.width + modifying_value
                new_height = self.height + modifying_value
                border = pygame.Rect((new_x - int(border_thickness / 2),new_y - int(border_thickness / 2),
                                    new_width + border_thickness, new_height + border_thickness))
                card = pygame.Rect((new_x,new_y,new_width,new_height))
                self.rect = AAfilledRoundedRect(screen, border,self.border_color)
                AAfilledRoundedRect(screen,card,self.color)
            else:
                border = pygame.Rect((self.x - int(border_thickness / 2),self.y - int(border_thickness / 2),
                                    self.width + border_thickness, self.height + border_thickness))
                card = pygame.Rect((self.x,self.y,self.width,self.height))
                AAfilledRoundedRect(screen, border,self.border_color)
                self.rect = AAfilledRoundedRect(screen,card,self.color)
        
    def mouseCollide(self,mouse_position):
        if self.rect.collidepoint(mouse_position[0],mouse_position[1]):
            self.modified = True
            return self.index
        
        self.modified = False
        return -1