import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text, Button

pygame.init()

class LauncherGameSoloView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Salon pour jouer tout seul"
        self.__window = self.__shared["window"]
        self.__fonts = self.__shared["fonts"]
        self.createAll()
    
    def getValueBtnHome(self):
        return self.__btnHomeGo.isActive()
    
    def getValueBtnStart(self):
        return self.__btnStartGo.isActive()
    
    def setValueBtnHome(self):
        self.__btnHomeGo.notActive()
    
    def setValueBtnStart(self):
        self.__btnStartGo.notActive()

    def createAll(self):
        self.createBg()
        self.createButtons()
        self.createTexts()
        pygame.display.update()
    
    def createTexts(self):
        self.__colorTextTitle = "black"
        self.__tTitle = Text(self.__window,"Salle d'attente",(250,20))
        self.__tTitle.setFont(self.__fonts[1])
        self.__tInfo = Text(self.__window,"Page indisponnible, revenez plus tard",(160,200),"red")
    
    def createButtons(self):
        btnsPosY = 330
        self.__btnHomeGo = Button(self.__window,"[H]",position=(10,btnsPosY))
        self.__btnStartGo = Button(self.__window,"JOUER",position=(570,btnsPosY))

    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawButtons()
        self.drawTexts()
        pygame.display.update()

    def drawTexts(self):
        pygame.draw.rect(self.__window,"white",[(150,185),(400,50)])
        self.__tInfo.draw()
        self.__tTitle.draw()
        self.__tTitle.setColor(self.__colorTextTitle)
    
    def doEvent(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.__colorTextTitle == "White":
                self.__colorTextTitle = "black"
            else:
                self.__colorTextTitle = "White"

    def drawButtons(self):
        self.__btnHomeGo.draw()
        #self.__btnStartGo.draw()

    def update(self,event):
        self.updateButtons(event)
        self.doEvent(event)

    def updateButtons(self, event):
        self.__btnHomeGo.update(event)
        #self.__btnStartGo.update(event)

    def createBg(self):
        bgImg = pygame.image.load(self.__shared["bg"])
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()
