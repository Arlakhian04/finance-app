class Header:
    def __init__(self,width,height,color,x,y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def displayHeader(self,pygame,screen):
        header = pygame.Rect((self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,self.color,header)

def buildHeader(width,height,color,x,y):
    return Header(width,height,color,x,y)