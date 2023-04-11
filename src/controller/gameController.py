import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from model.grid import Grid
from model.player import Player
from view.gameView import GameView
from model.enums.modeGame import ModeGame
from model.enums.page import Page
pygame.init()

class GameController:
    def __init__(self,common):
        self.__common = common
        self.__mode = self.__common["mode"]
        self.__grid = Grid()
        self.createPalyers()
        self.__view = GameView(self.__common,self.__grid.getImg(),self.__players,self.__grid)
        self.__precedentCaseClicked = None

    def setModeGame(self,newMode):
        self.__mode = newMode

    #methods
    def createPalyers(self):
        if self.__mode == ModeGame.HUMAN:
            self.__players = [Player("Player 1"),Player("Player 2")]
        self.__currentPalyer = 0

    def changeCurrentPlayer(self):
        self.__currentPalyer = 1 - self.__currentPalyer
        self.__view.setCurrentSymbol(self.__players[self.__currentPalyer].getSymbol())
    
    def play(self,row,column):
        if not self.__grid.isFull() and self.__grid.addAt(self.__players[self.__currentPalyer].getSymbol(),row,column):
            if not self.detectWinner(): 
                pass
            else:
                self.pointAllocation()
            return True
        return False

    def detectWinner(self):
        grid = self.__grid.getMatrix()
        for i in range(3):
            # Vérifie l'alignement horizontal
            if grid[i][0] == grid[i][1] == grid[i][2] != self.__grid.getEmpty():
                self.__view.setListWinner([(i,0),(i,1),(i,2)])
                return True
            # Vérifie l'alignement vertical
            if grid[0][i] == grid[1][i] == grid[2][i] != self.__grid.getEmpty():
                self.__view.setListWinner([(0,i),(1,i),(2,i)])
                return True
        # Vérifie l'alignement diagonal de gauche à droite
        if grid[0][0] == grid[1][1] == grid[2][2] != self.__grid.getEmpty():
            self.__view.setListWinner([(0,0),(1,1),(2,2)])
            return True
        # Vérifie l'alignement diagonal de droite à gauche
        if grid[0][2] == grid[1][1] == grid[2][0] != self.__grid.getEmpty():
            self.__view.setListWinner([(0,2),(1,1),(2,0)])
            return True
        return False

    def pointAllocation(self):
        self.__players[self.__currentPalyer].addPoint()
        
    def restart(self):
        if not self.__grid.isEmpty():
            self.__players[0].addNbGamePlayed()
            self.__players[1].addNbGamePlayed()
        self.__view.setListWinner([])
        self.__view.setCaseClicked(None)
        self.__grid.clearMatrix()
    
    def currentGame(self):
        self.__precedentCaseClicked = self.__view.getCaseClicked()
        if self.__precedentCaseClicked != None and self.play(self.__precedentCaseClicked[1],self.__precedentCaseClicked[0]):
            self.changeCurrentPlayer()
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or self.__view.getValueBtnRestart():
            self.restart()
            self.__view.setValueBtnRestart()
            
        
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or self.__view.getValueBtnHomeGo():
            self.__common["page"] = Page.HOME
            self.__view.setValueBtnHomeGo()
            return Page.NEXT
    
    def update(self,update):
        self.__common = update

    def run(self):
        while True:
            self.__view.drawAll()
            self.currentGame()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__common
                self.__view.update(event)
    