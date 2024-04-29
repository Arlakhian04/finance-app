class Card:
    def __init__(self, width, height,index, sign, value, date, name,x,y):
        self.index = index
        self.sign = sign
        self.value = value
        self.date = date
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def displayCard(self,pygame,screen):
        card = pygame.Rect((self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,(0,0,0),card,2,10)
