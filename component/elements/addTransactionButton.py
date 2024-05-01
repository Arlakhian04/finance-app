class transacButton:
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.hovered = False

    #Displaying the button on the screen
    def displayButton(self,pygame,screen):
        if self.hovered:
            button = pygame.Rect((self.x,self.y,self.width,self.height))
            pygame.draw.rect(screen,(0,0,0),button,1,40)
        else:
            posX = int(self.x + self.width - (self.height / 2))
            posY = int(self.y + (self.height / 2))
            pygame.gfxdraw.aacircle(screen,posX,posY,int(self.height / 2),(0,0,0))

    #Getter of the state of the button
    def getHovered(self):
        return self.hovered
    
    #Setter to change the state of the button when the mouse pass on it
    def setHovered(self,state):
        self.hovered = state

#Builder
def buildingAddTransacButton(SCREEN_WIDTH,SCREEN_HEIGHT,footerHeight):
    buttonWidth = max(SCREEN_WIDTH / 100 * 15,100)
    buttonHeight = max(SCREEN_HEIGHT / 100 * 2 + SCREEN_WIDTH / 100 * 3,20)
    buttonPadding = 10
    return transacButton(buttonWidth,buttonHeight,int(SCREEN_WIDTH - buttonWidth - buttonPadding),int(SCREEN_HEIGHT - footerHeight - buttonHeight - buttonPadding))