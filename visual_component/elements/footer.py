from elements_constant import FOOTER_BORDER_COLOR_LIGHT,FOOTER_COLOR_LIGHT
class Footer:
    def __init__(self,width,height,border_thickness,x,y):
        self.width = width
        self.height = height
        self.color = FOOTER_COLOR_LIGHT
        self.border_color = FOOTER_BORDER_COLOR_LIGHT
        self.border_thickness = border_thickness
        self.x = x
        self.y = y

    def displayFooter(self,pygame,screen):
        footer = pygame.Rect((self.x,self.y,self.width,self.height))
        footer_border = pygame.Rect((self.x,self.y - self.border_thickness,self.width,self.height + self.border_thickness))
        pygame.draw.rect(screen,self.border_color,footer_border)
        pygame.draw.rect(screen,self.color,footer)

def buildFooter(width,height,border_thickness,x,y):
    return Footer(width,height,border_thickness,x,y)