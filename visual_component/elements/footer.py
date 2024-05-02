class Footer:
    def __init__(self,width,height,color,border_color,border_thickness,x,y):
        self.width = width
        self.height = height
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.x = x
        self.y = y

    def displayFooter(self,pygame,screen):
        footer = pygame.Rect((self.x,self.y,self.width,self.height))
        footer_border = pygame.Rect((self.x,self.y - self.border_thickness,self.width,self.height + self.border_thickness))
        pygame.draw.rect(screen,self.border_color,footer_border)
        pygame.draw.rect(screen,self.color,footer)

def buildFooter(width,height,color,border_color,border_thickness,x,y):
    return Footer(width,height,color,border_color,border_thickness,x,y)