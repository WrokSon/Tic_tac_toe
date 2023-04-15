import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text

class PresentationView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__window = self.__shared["window"]
        self.__windowTitle = "Tic Tac Toe | Presentation"
        self.__transitionNum = 1
        self.createAll()

    def getTransitionNum(self):
        return self.__transitionNum

    def createAll(self):
        color = "white"
        dimName =(30,30)
        self.__posNameY = 350 
        #scene 1
        self.__logo = pygame.image.load("src/resources/images/presentation/logo-jeu-video.png")
        self.__logo = pygame.transform.scale(self.__logo,(250,250))
        #scene 2
        self.__tPresente = Text(self.__window,"présente",(300,180),color)
        #scene 3
        self.__title = pygame.image.load("src/resources/images/presentation/title.png")
        self.__title = pygame.transform.scale(self.__title,(450,450))
        self.__tName = Text(self.__window,"par Williame MASSONDI",(400,self.__posNameY),color)
        self.__leftName = pygame.image.load("src/resources/images/presentation/player1.png")
        self.__leftName = pygame.transform.scale(self.__leftName,dimName)
        self.__rightName = pygame.image.load("src/resources/images/presentation/player2.png")
        self.__rightName = pygame.transform.scale(self.__rightName,dimName)

    def changeView(self):
        self.__transitionNum += 1

    def drawAll(self):
        pygame.display.set_caption(self.__windowTitle)
        pygame.draw.rect(self.__window,"black",[(0,0),pygame.display.get_surface().get_size()])
        self.drawAllScenes()
        pygame.display.update()

    def drawAllScenes(self):
        if self.__transitionNum == 1 : self.scene1()
        if self.__transitionNum == 2 : self.scene2()
        if self.__transitionNum == 3 : self.scene3()

    def update(self,event):
        pass

    def createBg(self):
        pass

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()
    
    def scene1(self):
        self.__window.blit(self.__logo,(220,60))
    
    def scene2(self):
        self.__tPresente.draw()
    
    def scene3(self):
        self.__window.blit(self.__title,(150,-100))
        self.__window.blit(self.__leftName,(360,self.__posNameY))
        self.__window.blit(self.__rightName,(650,self.__posNameY))
        self.__tName.draw()
