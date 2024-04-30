class PortfolioCard:
    def __init__(self,width,height,x,y,isDisplayed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.isDisplayed = isDisplayed

    def displayPortfolioCard(self,pygame,screen):


    #Method to know if a portfolio card is displayed
    def isDisplayed(self):
        return self.isDisplayed
    
    def setIsDisplay(self,isDisplayed):
        self.isDisplayed = isDisplayed