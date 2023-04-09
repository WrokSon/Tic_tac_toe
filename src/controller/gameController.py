from src.model.grid import Grid
from src.model.player import Player
 
class GameController:
    def init(self):
        self.__players = [Player("Player 1"),Player("Player 2")]
        self.__cuurentPalyer = 0
        self.__grid = Grid()
        self.__score = [0,0]
        self.__nbPointToWin = 3
    
    #methods
    def changeCurrentPlayer(self):
        if self.__cuurentPalyer == 0 :
            self.__cuurentPalyer = 1
            return
        self.__cuurentPalyer = 0
    
    def play(self,row,column):
        if not self.__grid.isFull():
            self.__grid.addAt(self.__players[self.__cuurentPalyer],row,column)
            if not self.detectWinner(): 
                self.changeCurrentPlayer()
            else:
                self.pointAllocation()
            return True
        print("la grille est pleine")
        return False

    def detectWinner(self):
        grid = self.__grid.getMatrix()
        for i in range(len(grid)):
            for j in range(len(grid[i])-2):
                # Vérifie l'alignement horizontal
                if grid[i][j] == grid[i][j+1] == grid[i][j+2]:
                    return True
                # Vérifie l'alignement vertical
                if grid[i][j] == grid[j+1][i] == grid[j+2][i]:
                    return True
                # Vérifie l'alignement diagonal de gauche à droite
                if grid[i][j] == grid[i+1][j+1] == grid[i+1][j+2]:
                    return True
                # Vérifie l'alignement diagonal de droite à gauche
                if grid[i][j+1] == grid[i-1][j+1] == grid[i-2][j]:
                    return True
        return False

    def pointAllocation(self):
        self.__players[self.__cuurentPalyer].addPoint()
        
    def restart(self):
        self.__grid.clearMatrix()
        
        