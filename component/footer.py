class Footer:
    def __init__(self,width,height,color,x,y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def displayFooter(self,pygame,screen):
        footer = pygame.Rect((self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,self.color,footer)