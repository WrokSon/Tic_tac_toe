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
        self.__precedentCaseClicked = None
    #methods
    def changeCurrentPlayer(self):
        self.__cuurentPalyer = 1 - self.__cuurentPalyer
    
    def play(self,row,column):
        if not self.__grid.isFull():
            self.__grid.addAt(self.__players[self.__cuurentPalyer].getSymbol(),row,column)
            if not self.detectWinner(): 
                pass
            else:
                self.pointAllocation()
            return True
        print("la grille est pleine")
        return False

    def detectWinner(self):
        grid = self.__grid.getMatrix()
        for i in range(3):
            # Vérifie l'alignement horizontal
            if grid[i][0] == grid[i][1] == grid[i][2] != self.__grid.getEmpty():
                return True
            # Vérifie l'alignement vertical
            if grid[0][i] == grid[1][i] == grid[2][i] != self.__grid.getEmpty():
                return True
        # Vérifie l'alignement diagonal de gauche à droite
        if grid[0][0] == grid[1][1] == grid[2][2] != self.__grid.getEmpty():
            return True
        # Vérifie l'alignement diagonal de droite à gauche
        if grid[0][2] == grid[1][1] == grid[2][0] != self.__grid.getEmpty():
            return True
        return False

    def pointAllocation(self):
        self.__players[self.__cuurentPalyer].addPoint()
        
    def restart(self):
        self.__grid.clearMatrix()
    
    def runGame(self):
        caseClicked = self.__view.getCaseClicked()
        if caseClicked != self.__precedentCaseClicked and self.play(caseClicked[1],caseClicked[0]):
            self.__precedentCaseClicked = caseClicked
            self.changeCurrentPlayer()
    
    def run(self):
        while True and not self.endGame():
            self.__view.drawAll(self.__players[0].getSymbol(),self.__players[1].getSymbol())
            self.runGame()
            for event in pygame.event.get():
                self.__view.update(event)
                self.endGame()
            
    def endGame(self):
        return self.__grid.isFull() or self.detectWinner() 
    
    