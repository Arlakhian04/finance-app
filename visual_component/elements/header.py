from elements_constant import HEADER_BORDER_COLOR_LIGHT,HEADER_COLOR_LIGHT

class Header:
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.color = HEADER_COLOR_LIGHT
        self.border_color = HEADER_BORDER_COLOR_LIGHT
        self.x = x
        self.y = y

    def displayHeader(self,pygame,screen):
        header = pygame.Rect((self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,self.color,header)

def buildHeader(width,height,x,y):
    return Header(width,height,x,y)