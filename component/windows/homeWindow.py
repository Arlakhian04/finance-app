from component.elements import footer
from component.elements import addTransactionButton
from component.elements.addTransactionButton import buildingAddTransacButton
class homeWindow:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def build(self):
        footerHeight = int(self.width / 100 * 15)
        addTransacButton = buildingAddTransacButton(self.width,self.height,footerHeight)