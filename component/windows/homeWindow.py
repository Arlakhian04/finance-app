from component.elements.addTransactionButton import buildingAddTransacButton
class homeWindow:
    def __init__(self,width,height,transacButton):
        self.width = width
        self.height = height
        self.transacButton = transacButton

    def display(self,pygame,screen):
        self.transacButton.displayButton(pygame,screen)

    def getTransacButton(self):
        return self.transacButton
    

def build(width,height,footer_height):
    addTransacButton = buildingAddTransacButton(width,height,footer_height)
    return homeWindow(width,height,addTransacButton)