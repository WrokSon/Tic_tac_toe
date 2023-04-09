import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from model.grid import Grid
from model.player import Player
from view.gameView import GameView
pygame.init()

class GameController:
    def __init__(self,window):
        self.__players = [Player("Player 1"),Player("Player 2")]
        self.__cuurentPalyer = 0
        self.__grid = Grid()
        self.__view = GameView(window,self.__grid.getImg(),self.__players[0].getImg(),
                               self.__players[1].getImg(),self.__grid.getMatrix())
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
                if grid[i][j] != self.__grid.getEmpty():
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
    
    def runGame(self):
        caseClicked = self.__view.getCaseClicked()
        if caseClicked != None and self.play(caseClicked[0],caseClicked[1]):
            return
    
    def run(self):
        while True and not self.endGame():
            self.__view.drawAll()
            self.runGame()
            for event in pygame.event.get():
                self.__view.update(event)
            pygame.display.update()  
            
    def endGame(self):
        return self.__grid.isFull() and self.detectWinner() 
    
    