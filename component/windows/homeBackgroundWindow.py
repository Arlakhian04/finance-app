from component.elements import footer
from component.elements.footer import buildFooter

#Class that represents the whole background from the home window which are not elements that we can interact with
class HomeBackground:
    def __init__(self,width,height,footer,footer_height):
        self.width = width
        self.height = height
        self.footer = footer
        self.footer_height = footer_height
        
    def displayBackground(self,pygame,screen):
        self.footer.displayFooter(pygame,screen)

    def getFooterHeight(self):
        return self.footer_height

def buildBackground(width,height,elements_color):
    footer_width = width
    footer_height = int(max(height / 100 * 10,50))
    footer = buildFooter(footer_width,footer_height,(elements_color),0,height - footer_height)
    return HomeBackground(width,height,footer,footer_height)