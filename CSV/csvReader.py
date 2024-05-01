import numpy as np

class csvReader:
    def __init__(self,jsp):
        self.jsp = jsp

    def allPortfolioReader(self,csvFilename):
        #Read a csv file with the list of portfolio and creates objects for each of them and return an array containing all the portfolio
        return 