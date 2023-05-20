import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text, Button

pygame.init()

class UnavailableView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Pag indisponnible"
        self.__window = self.__shared["window"]
        self.__icons = self.__shared["icons"]
        self.createAll()
    
    def getValueBtnHome(self):
        return self.__btnHomeGo.isActive()
    
    def setValueBtnHome(self):
        self.__btnHomeGo.notActive()

    def createAll(self):
        self.createBg()
        self.__btnHomeGo = Button(self.__window,"Home",position=(280,180))
        self.__btnHomeGo.setIcon(self.__icons[3])
        self.__tInfo = Text(self.__window,"Page indisponnible, revenez plus tard",(160,115),"red")
        pygame.display.update()
    
    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.__btnHomeGo.draw()
        pygame.draw.rect(self.__window,"white",[(150,100),(400,50)])
        self.__tInfo.draw()
        pygame.display.update()

    def update(self,event):
        self.__btnHomeGo.update(event)

    def createBg(self):
        bgImg = pygame.image.load(self.__shared["bg"])
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()
