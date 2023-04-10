import pygame, sys, os
sys.path.append(os.getcwd())

class Grid:
    def __init__(self):
        self.__nbCol = 3
        self.__nbRow = 3
        self.__empty = "."
        self.__matrix = [[self.__empty for i in range(self.__nbCol)] for j in range(self.__nbRow)]
        self.__image = pygame.image.load("src/ressources/images/game/grid.png")
    
    #Getters
    def getNbCol(self):
        return self.__nbCol
    
    def getNbRow(self):
        return self.__nbRow
    
    def getMatrix(self):
        return self.__matrix
    
    def getEmpty(self):
        return self.__empty
    
    def getImg(self):
        return self.__image
    
    #methods
    def addAt(self,symbol,row,column):
        if self.__matrix[row][column] == self.__empty:
            self.__matrix[row][column] = symbol
            return True
        return False

    def removeAt(self,row,column):
        self.__matrix[row][column] = self.__empty

    def clearMatrix(self):
        self.__matrix = [[self.__empty for i in range(self.__nbCol)] for j in range(self.__nbRow)]

    def isFull(self):
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                if self.__matrix[i][j] == self.__empty:
                    return False
        return True
    