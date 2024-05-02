#Class to make protfolio card
from visual_component.random import aafilledRoundedRect
from visual_component.random.aafilledRoundedRect import AAfilledRoundedRect
class PortfolioCard:
    def __init__(self,width,height,x,y,previousY,index,isDisplayed,color,border_color,modified):
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
        self.color = color
        self.border_color = border_color
        self.modified = modified

    def getWidth(self):
        return self.width
    
    def getWidth(self):
        return self.width
    

    def displayPortfolioCard(self,pygame,screen):
        """Display the portfolio card
        Args:
            pygame (pygame): element to use the pygame methods
            screen (pygame.Surface): surface where we display the card
        """
        if self.isDisplayed:
            border_thickness = 2
            border = pygame.Rect((self.x - int(border_thickness / 2),self.y - int(border_thickness / 2),
                                  self.width + border_thickness, self.height + border_thickness))
            card = pygame.Rect((self.x,self.y,self.width,self.height))
            AAfilledRoundedRect(screen, border,self.border_color)
            self.rect = AAfilledRoundedRect(screen,card,self.color)
        
    def mouseCollide(self,mouse_position):
        print("collide")
        if self.rect.collidepoint(mouse_position[0],mouse_position[1]):
            return self.index
        
        return -1

    #Getter for y
    def getY(self):
        return self.y

    #Setter for y
    def setY(self,y):
        self.y = y

    #Method to know if a portfolio card is displayed
    def isDisplayed(self):
        return self.isDisplayed
    
    #Setter for isDisplay
    def setIsDisplay(self,isDisplayed):
        self.isDisplayed = isDisplayed