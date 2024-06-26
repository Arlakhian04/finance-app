from visual_component.elements import footer
from visual_component.elements.footer import buildFooter
from visual_component.elements import header
from visual_component.elements.header import buildHeader

#Class that represents the whole background from the home window which are not elements that we can interact with
class HomeBackground:
    def __init__(self,width,height,footer,footer_height,header,header_height):
        self.width = width
        self.height = height
        self.footer = footer
        self.footer_height = footer_height
        self.header = header
        self.header_height = header_height
        
    def displayBackground(self,pygame,screen):
        self.footer.displayFooter(pygame,screen)
        self.header.displayHeader(pygame,screen)
    


def buildBackground(width,height,elements_color):
    footer_width = width
    footer_height = int(max(height / 100 * 10,20))
    footer_border_color = (255,255,255)
    footer_border_thickness = 1
    footer = buildFooter(footer_width,footer_height,(elements_color),footer_border_color,footer_border_thickness,0,height - footer_height)
    header_height = int(max(height / 100 * 3, 7))
    header_width = width
    header = buildHeader(header_width,header_height,(elements_color),0,0)
    return HomeBackground(width,height,footer,footer_height,header,header_height)