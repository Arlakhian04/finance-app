class transacButton:
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def displayButton(self,pygame,screen,hovered):
        if hovered:
            button = pygame.Rect((self.x,self.y,self.width,self.height))
            pygame.draw.rect(screen,(0,0,0),button,1,40)
        else:
            posX = int(self.x + self.width - (self.height / 2))
            posY = int(self.y + (self.height / 2))
            pygame.gfxdraw.aacircle(screen,posX,posY,int(self.height / 2),(0,0,0))

def buildingAddTransacButton(SCREEN_WIDTH,SCREEN_HEIGHT,footerHeight):
    buttonWidth = max(SCREEN_WIDTH / 100 * 15,100)
    buttonHeight = max(SCREEN_HEIGHT / 100 * 2 + SCREEN_WIDTH / 100 * 3,20)
    buttonPadding = 10
    return transacButton(buttonWidth,buttonHeight,SCREEN_WIDTH - buttonWidth - buttonPadding,SCREEN_HEIGHT - footerHeight - buttonHeight - buttonPadding)